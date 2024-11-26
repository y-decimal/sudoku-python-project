import tkinter as tk
import SudokuGridHelper
import customtkinter as ctk


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
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0,1), weight=1)




        # Frame Grid Configuration
        self.sudoku_frame = SudokuGridHelper.SudokuGameFrame(self, self.window_height*0.90)
        self.sudoku_frame.configure(padding=5)

        self.sudoku_frame.grid(row=0, column=0, padx=10, columnspan=1) 



        self.sudoku_button_frame = ctk.CTkFrame(self)
        self.sudoku_button_frame_border_color = "#FFFFAA"

        self.button1 = ctk.CTkButton(self.sudoku_button_frame, text="Click Me!", command=self.button_callback)
        self.button1.grid(row = 0, column = 0, padx=10, pady=10, sticky="ew")
        self.button1.configure(border_color=self.sudoku_button_frame_border_color, border_width=1)

        self.clear_button = ctk.CTkButton(self.sudoku_button_frame, text="Clear", command=self.clearbutton_callback)
        self.clear_button.grid(row = 0, column = 1, padx=10, pady=10, sticky="ew")
        self.clear_button.configure(border_color=self.sudoku_button_frame_border_color, border_width=1)


        self.sudoku_button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ns")
        self.sudoku_button_frame.grid_columnconfigure((0,1), weight=1)
        self.sudoku_button_frame.grid_rowconfigure(0, weight=1)
        self.sudoku_button_frame.configure(border_color=self.sudoku_button_frame_border_color, border_width=3)



        self.label = ctk.CTkLabel(self, text="", font=("Arial", 20), justify="center")
        #self.label.grid(row = 1, column = 1, padx=10, pady=10, sticky="ew")
        #self.label.configure(bg_color="darkblue")





    def button_callback(self):
        self.label.configure(text="Button Clicked!")


    def clearbutton_callback(self):
        self.label.configure(text="")
        

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
        
        
    



root = SudokuApp()

# root.sudoku_field[0].entry_variable.set("1")
# root.sudoku_field[0].configure(status="disabled")

root.mainloop()