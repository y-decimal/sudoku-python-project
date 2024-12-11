import tkinter as tk
import customtkinter as ctk

from view.gridhelpers.GameGridHelper import SudokuGameFrame
from view.customframes import ButtonFrame, CheckboxFrame



class View(ctk.CTkFrame):


    def __init__(self, parent):

        super().__init__(parent)

       
        # App Grid Configuration
        #self.grid_columnconfigure((0,3), weight=1)
        #self.grid_rowconfigure((0,3), weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_columnconfigure((1), weight=2)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure((1,2), weight=1)




        # Frame Grid Configuration
        
        # Sudoku Frame
        self.sudoku_frame = SudokuGameFrame(self, 600, seperator_spacing=1)
        self.sudoku_frame.grid(row=0, column=1, padx=10, columnspan=1) 


        # Button Frame
        self.sudoku_button_frame = ButtonFrame.ButtonFrame(self, 1, 2)
        self.sudoku_button_frame_border_color = "#FFFFAA"

        self.sudoku_button_frame.buttons[0].configure(text="Fetch", command = self.fetchbutton_callback)
        self.sudoku_button_frame.buttons[1].configure(text="Submit", command = self.submitbutton_callback)
        

        self.sudoku_button_frame.grid(row=2, column=1, padx=10, pady=10, sticky="s")



    	# Label Configuration
        self.label = ctk.CTkLabel(self, text="", font=("Arial", 20), justify="center")
        self.label.grid(row = 1, column = 1, padx=10, pady=10, sticky="nsew")


    def set_controller(self, controller):
        '''Sets the controller of the view'''
        self.controller = controller


    def fetchbutton_callback(self):
        if self.controller: self.controller.fetch_button_clicked()
        
        

    def submitbutton_callback(self):
        if self.controller: self.controller.submit_button_clicked()
       
        


    def set_field_not_editable(self, row: int, column: int):
        self.sudoku_frame.game_field[row*9 + column].configure(state="disabled")
        self.sudoku_frame.game_field[row*9 + column].configure(fg_color="#303032")
        self.sudoku_frame.game_field[row*9 + column].configure(text_color="#9cdcf1")


    def set_field_value(self, row: int, column: int, value: int):
        if (value > 0 and value < 10):
            self.sudoku_frame.game_field[row*9 + column].entry_variable.set(str(value))
        elif (value == 0):
            self.sudoku_frame.game_field[row*9 + column].entry_variable.set("")


    def get_field_value(self, row: int, column: int) -> int:
        
        value = self.sudoku_frame.game_field[row*9 + column].entry_variable.get()
        if value == "":
            return 0
        else:
            return int(value)



