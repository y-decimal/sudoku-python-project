import tkinter as tk
import customtkinter as ctk

from view.customframes.SudokugridFrame import SudokuFrame
from view.customframes import ButtonFrame, CheckboxFrame



class View(ctk.CTkFrame):


    disabled_color = ("#303032", "#9cdcf1")
    enabled_color = ("#343638", "#FFFFFF")

    def __init__(self, parent):
        
        super().__init__(parent)

       
        # App Grid Configuration (3x3 Grid)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure((1,2), weight=1)




        # Frame Grid Configuration
        
        # Sudoku Frame
        self.sudoku_frame = SudokuFrame(self, 9)
        print("Sudoku Frame initialized")
        self.sudoku_frame.grid(row=0, column=1, padx=10) 


        # Button Frame
        self.sudoku_button_frame = ButtonFrame.ButtonFrame(self, 1, 5)
        self.sudoku_button_frame_border_color = "#FFFFAA"

        self.sudoku_button_frame.buttons[0].configure(text="Fetch", command = self.fetchbutton_callback)
        self.sudoku_button_frame.buttons[1].configure(text="Push", command = self.pushbutton_callback)
        self.sudoku_button_frame.buttons[2].configure(text="Generate", command = self.generatebutton_callback)
        self.sudoku_button_frame.buttons[3].configure(text="Save", command = self.savebutton_callback)
        self.sudoku_button_frame.buttons[4].configure(text="Load", command = self.loadbutton_callback)
        

        self.sudoku_button_frame.grid(row=2, column=1, padx=10, pady=10, sticky="s")



    	# Label Configuration
        self.label = ctk.CTkLabel(self, text="", font=("Arial", 20), justify="center")
        self.label.grid(row = 1, column = 1, padx=10, pady=10, sticky="nsew")



    def set_controller(self, controller):
        '''Sets the controller of the view'''
        self.controller = controller



    def fetchbutton_callback(self):
        if self.controller: self.controller.fetch()
        

    def pushbutton_callback(self):
        if self.controller: self.controller.push()
       
    
    def generatebutton_callback(self):
        if self.controller: self.controller.generate()

    def savebutton_callback(self):
        if self.controller: self.controller.save()
        
    def loadbutton_callback(self):
        if self.controller: self.controller.load()
    
    def set_field_not_editable(self, row: int, column: int):
        # Note: the .configure method is very slow, so we need to check if updating is necessary first
        if self.sudoku_frame.game_field[row][column].cget("state") == "normal":      
            self.sudoku_frame.game_field[row][column].configure(state="disabled")
            self.sudoku_frame.game_field[row][column].configure(fg_color=self.disabled_color[0])
            self.sudoku_frame.game_field[row][column].configure(text_color=self.disabled_color[1])
        
    

    def set_field_editable(self, row: int, column: int):
        # Note: the .configure method is very slow, so we need to check if updating is necessary first
        if self.sudoku_frame.game_field[row][column].cget("state") == "disabled":
            self.sudoku_frame.game_field[row][column].configure(state="normal")
            self.sudoku_frame.game_field[row][column].configure(fg_color=self.enabled_color[0])
            self.sudoku_frame.game_field[row][column].configure(text_color=self.enabled_color[1])



    def set_field_value(self, row: int, column: int, value: int):
        
        if (value > 0 and value < 10):
            self.sudoku_frame.game_field[row][column].entry_variable.set(str(value))
            
        elif (value == 0):
            self.sudoku_frame.game_field[row][column].entry_variable.set("")



    def get_field_value(self, row: int, column: int) -> int:
        
        value = self.sudoku_frame.game_field[row][column].entry_variable.get()
        if value == "":
            return 0
        else:
            return int(value)



