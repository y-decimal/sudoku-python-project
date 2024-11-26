import customtkinter as ctk
import tkinter as tk
from abc import ABC, abstractmethod

class GameEntryField(ABC):

            def __init__(self, master, row, column, entry_dimensions):      

                self.entry_variable = ctk.StringVar()       

                self.entry = ctk.CTkEntry(master, 
                                 width= entry_dimensions, 
                                 height = entry_dimensions, 
                                 font = ("Arial", 20), 
                                 textvariable=self.entry_variable, 
                                 justify="center"
                                )

                self.entry.grid(row=row, column=column, sticky="nsew")
                self.entry.configure(border_color="lightgreen", border_width=1)
                self.entry_variable.trace_add("write", self.callback)

            @abstractmethod
            def callback(self , *args): 
                                      
                    if len(self.entry_variable.get()) > 1:
                        self.entry_variable.set(self.entry_variable.get()[:1])



class SquareGameFrame(tk.ttk.Frame, ABC):

    def initialize_game_frame(self, master, gridsize, frame_height):

        super().__init__(master)

        self.gridsize = gridsize    

        # Frame Grid Configuration


        self.grid_columnconfigure([i for i in range(self.gridsize)], weight=1)
        self.grid_rowconfigure( [i for i in range(self.gridsize)], weight=1)
        
        self.game_entry_dimension = frame_height/gridsize 
      
        self.game_field = []

        for i in range(gridsize**2):
            self.set_game_field(i)

    @abstractmethod
    def set_game_field(self, i):
        pass

