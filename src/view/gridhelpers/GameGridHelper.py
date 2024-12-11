import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class GameEntryField(ctk.CTkEntry, ABC):

            def __init__(self, master, entry_dimensions, function = None):      

                self.entry_variable = ctk.StringVar()       

                super().__init__(master, 
                                 width= entry_dimensions, 
                                 height = entry_dimensions, 
                                 font = ("Arial", 34), 
                                 textvariable=self.entry_variable, 
                                 justify="center"
                                )

                #self.configure(border_color="lightgreen", border_width=1)
                self.entry_variable.trace_add("write", self.callback)

            @abstractmethod
            def callback(self , *args): 
                                      
                    if len(self.entry_variable.get()) > 1:
                        self.entry_variable.set(self.entry_variable.get()[:1])



class SudokuEntryField(GameEntryField):

    def __init__(self, master, entry_dimensions):
        super().__init__(master, entry_dimensions)

    def callback(self, *args):

        if len(self.entry_variable.get()) > 1:

            self.entry_variable.set(self.entry_variable.get()[1:])
        if (not self.entry_variable.get().isdigit() or self.entry_variable.get() == "0"):
            self.entry_variable.set("")
            




class SquareGameFrame(ctk.CTkFrame, ABC):

    def initialize_game_frame(self, master, game_gridsize, frame_height, separator_spacing):

        super().__init__(master)

        self.gridsize = game_gridsize+(game_gridsize//separator_spacing-1)
        self.configure_grid()
        self.initialize_fields(frame_height, game_gridsize)
        self.add_horizontal_separators()
        self.add_vertical_separators()



    def configure_grid(self):
        self.grid_columnconfigure([i for i in range(self.gridsize)], weight=1)
        self.grid_rowconfigure([i for i in range(self.gridsize)], weight=1)

    def initialize_fields(self, frame_height, game_gridsize):
        self.game_entry_dimension = frame_height / game_gridsize
        self.game_field = []
        self.iterator = 0
        self.separator_style = ttk.Style()
        self.separator_style.configure("TSeparator", background="lightgreen")

        for row in range(self.gridsize):
            if row % 2 == 0:
                for column in range(self.gridsize):
                    if column % 2 == 0:
                        self.game_field.append(self.set_game_field())
                        self.game_field[self.iterator].grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
                        self.iterator += 1

    def add_horizontal_separators(self):
        for row in range(self.gridsize):
            if row % 2 != 0 and (row + 1) % 3 == 0:
                ctk.CTkFrame(self, height=4, fg_color="#505070", corner_radius=2).grid(row=row, column=0, columnspan=self.gridsize, sticky="ew", pady=3)

    def add_vertical_separators(self):
        for col in range(self.gridsize):
            if col % 2 != 0 and (col + 1) % 3 == 0:
                ctk.CTkFrame(self, width=4, fg_color="#505070", corner_radius=2).grid(row=0, column=col, rowspan=self.gridsize, sticky="ns", padx=3)
                
            
    @abstractmethod
    def set_game_field(self):
        pass



class SudokuGameFrame(SquareGameFrame):

    SUDOKUGRIDSIZE = 9

    def __init__(self, master, frame_height, seperator_spacing = 0):
        self.initialize_game_frame(master, self.SUDOKUGRIDSIZE, frame_height, seperator_spacing)

    def set_game_field(self):
        return SudokuEntryField(master=self, entry_dimensions=self.game_entry_dimension)

