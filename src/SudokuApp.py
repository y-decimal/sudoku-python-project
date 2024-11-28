import tkinter as tk
import customtkinter as ctk
import random

import customframes.ButtonFrame
from gridhelpers.GameGridHelper import SudokuGameFrame
from customframes import ButtonFrame, CheckboxFrame



class SudokuApp(ctk.CTk):


    def __init__(self, sudoku_test_text = "Sudoku Test", relative_size = 0.5, minimum_size = 0.5, aspect_ratio = 5/4):

        ctk.CTk.__init__(self)


        self.sudoku_test_text = sudoku_test_text
        self.relative_size = relative_size
        self.minimum_size = minimum_size
        self.aspect_ratio = aspect_ratio

        self.set_window_parameters()

        # set the icon of the window
        self.iconbitmap('./assets/images/sudoku.ico')
        

       
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


        self.sudoku_button_frame.buttons[0].configure(text="Click Me!", command=lambda: self.restorebutton_callback(self.sudoku_frame))
        self.sudoku_button_frame.buttons[1].configure(text="Clear", command=lambda: self.clearbutton_callback(self.sudoku_frame))


        self.sudoku_button_frame.grid(row=2, column=1, padx=10, pady=10, sticky="s")




    	# Label Configuration
        self.label = ctk.CTkLabel(self, text="", font=("Arial", 20), justify="center")
        self.label.grid(row = 1, column = 1, padx=10, pady=10, sticky="nsew")

        #Checkbox Configuration
        self.checkbox_frame = CheckboxFrame.CheckboxFrame(self, 9, 1)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", rowspan=3)
        self.rowconfigure(0, weight=2)






    def clearbutton_callback(self, master):

        master.previous_grid_info = master.grid_info()
        print(master.previous_grid_info)
        master.grid_forget()
        


    def restorebutton_callback(self, master):

        if master.previous_grid_info == None:
            print("No previous grid info")
            return
        
        # print("Row: " + str(master.previous_grid_info.get("row")))
        # print("Column: " + str(master.previous_grid_info.get("column")))

        master.grid(row = master.previous_grid_info.get("row"),
                    column = master.previous_grid_info.get("column"), 
                    padx = master.previous_grid_info.get("padx"), 
                    pady = master.previous_grid_info.get("pady"), 
                    sticky = master.previous_grid_info.get("sticky"))
        
        master.previous_grid_info = None
        

    def togglebutton_callback(self):
        if self.toggle_state:
            self.labelTopright.grid(row = 0, column = 1, padx=10, pady=10, sticky="ew")
            self.toggle_state = False
        elif not self.toggle_state:
            self.labelTopright.grid_forget()
            self.toggle_state = True


    def set_window_parameters(self):

         # get the screen width and height
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # set the window size relative to the screen size
        self.window_height = int(self.screen_height*self.relative_size)
        self.window_width = int(self.window_height*self.aspect_ratio)

        # find the center point of the screen
        center_x = int(self.screen_width/2 - self.window_width/2)
        center_y = int(self.screen_height/2 - self.window_height/2)

        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        # set the minimum size of the window
        minimum_height = int(self.screen_height*self.minimum_size)
        minimum_width = int(minimum_height*self.aspect_ratio)
        self.minsize(minimum_width, minimum_height)

        # set the title of the window
        self.title(self.sudoku_test_text)
        
        
    



root = SudokuApp(minimum_size=0.6, aspect_ratio=5/4)

# Fucked and not final 
# def callback(var, indx, mode):
#     try: print(f"Value {int(root.sudoku_frame.game_field[int(var[-2:])].entry_variable.get()[1])} changed at index {int(var[-2:])}")
#     except IndexError: print(f"Value at index {int(var[-2:])} empty")
    

# for i in range(81):
#     root.sudoku_frame.game_field[i].entry_variable.trace("w", callback)



# Just for testing
for i in range(81):
    if (i % random.randint(1,9) == 0):
        root.sudoku_frame.game_field[i].entry_variable.set(str(random.randint(1,9)))
        root.sudoku_frame.game_field[i].configure(state="disabled")
        root.sudoku_frame.game_field[i].configure(fg_color="#303032")
        root.sudoku_frame.game_field[i].configure(text_color="#9cdcf1")



root.mainloop()