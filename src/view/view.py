import tkinter as tk
import customtkinter as ctk

from view.gridhelpers.GameGridHelper import SudokuGameFrame
from view.customframes import ButtonFrame, CheckboxFrame



class View(ctk.CTkFrame):


    def __init__(self, master):

        super.__init__(self, master)

       
        # App Grid Configuration
        #self.grid_columnconfigure((0,3), weight=1)
        #self.grid_rowconfigure((0,3), weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_columnconfigure((1), weight=2)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure((1,2), weight=1)



        # Frame Grid Configuration
        self.sudoku_frame = SudokuGameFrame(self, self.window_height*0.90, seperator_spacing=1)
        self.sudoku_frame.grid(row=0, column=1, padx=10, columnspan=1) 


        self.sudoku_button_frame = ButtonFrame.ButtonFrame(self, 1, 2)
        self.sudoku_button_frame_border_color = "#FFFFAA"


        self.sudoku_button_frame.buttons[0].configure(text="Submit", command=lambda: self.submitbutton_callback(self))
        self.sudoku_button_frame.buttons[1].configure(text="Fetch", command=lambda: self.fetchbutton_callback(self))


        self.sudoku_button_frame.grid(row=2, column=1, padx=10, pady=10, sticky="s")




    	# Label Configuration
        self.label = ctk.CTkLabel(self, text="", font=("Arial", 20), justify="center")
        self.label.grid(row = 1, column = 1, padx=10, pady=10, sticky="nsew")

        # #Checkbox Configuration
        # self.checkbox_frame = CheckboxFrame.CheckboxFrame(self, 9, 1)
        # self.checkbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", rowspan=3)
        # self.rowconfigure(0, weight=2)




    def fetchbutton_callback(self, master):
        print("Fetch Button Clicked")
        
        

    def submitbutton_callback(self, master):
        print("Submit Button Clicked")
       
        

    def togglebutton_callback(self):
        if self.toggle_state:
            self.labelTopright.grid(row = 0, column = 1, padx=10, pady=10, sticky="ew")
            self.toggle_state = False
        elif not self.toggle_state:
            self.labelTopright.grid_forget()
            self.toggle_state = True



    def set_field_not_editable(self, row: int, column: int):
        self.sudoku_frame.game_field[row*9 + column].configure(state="disabled")
        self.sudoku_frame.game_field[row*9 + column].configure(fg_color="#303032")
        self.sudoku_frame.game_field[row*9 + column].configure(text_color="#9cdcf1")


    def set_field_value(self, row: int, column: int, value: int):

        if (value != 0):
            self.sudoku_frame.game_field[row*9 + column].entry_variable.set(str(value))


    def get_field_value(self, row: int, column: int) -> int:
        return int(self.sudoku_frame.game_field[row*9 + column].entry_variable.get())



