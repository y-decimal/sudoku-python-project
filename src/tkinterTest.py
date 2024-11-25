import tkinter as tk
import customtkinter as ctk



class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        SUDOKU_TEST_TEXT = "Sudoku Test Print"       
        RELATIVE_SIZE = 0.5
        MINIMUM_SIZE = 0.525
        ASPECT_RATIO = 5/4


        self.title(SUDOKU_TEST_TEXT)

        self.set_window_size(RELATIVE_SIZE, MINIMUM_SIZE, ASPECT_RATIO)

        self.iconbitmap('./assets/images/sudoku.ico')


        self.sudoku_frame = ctk.CTkFrame(self)

        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.sudoku_frame.grid_columnconfigure((0,8), weight=1)
        self.sudoku_frame.grid_rowconfigure((0,8), weight=1)
        self.sudoku_frame.grid(row=0, column=1, padx=10, pady=10) 

        class SudokuField(ctk.CTkEntry):
            def __init__(self, master, row, column, sticky):      
                self.entry_variable = ctk.StringVar()          
                super().__init__(master, width=50, height=50, font=("Arial", 30), textvariable=self.entry_variable, justify="center")
                self.grid(row=row, column=column, padx=10, pady=10, sticky=sticky)
                self.entry_variable.trace_add("write", self.callback)

            def callback(self , *args):
                if len(self.entry_variable.get()) > 1:
                    self.entry_variable.set(self.entry_variable.get()[:1])
                if not self.entry_variable.get().isdigit():
                    self.entry_variable.set("")



        self.sudoku_field = []
        for i in range(9*9):

            sticky = ""

            if i//9 == 0: 
                sticky += "s"
            elif i//9 == 8:
                sticky += "n"
            if i%9 == 0:
                sticky += "e"
            elif i%9 == 8:
                sticky += "w"

            #print(sticky)

            self.sudoku_field.append(SudokuField(self.sudoku_frame, i//9, i%9, sticky))



        self.button = ctk.CTkButton(self, text="Click Me!", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.label = ctk.CTkLabel(self, text="", font=("Arial", 20), justify="center")
        self.label.grid(row = 2, column = 1, padx=10, pady=10, sticky="ew")


    def button_callback(self):
        self.label.configure(text="Button Clicked!")

    def set_window_size(self, relative_size, minimum_size, aspect_ratio):

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        #set the window size relative to the screen size
        window_height = int(screen_height*relative_size)
        window_width = int(window_height*aspect_ratio)

        # find the center point of the screen
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # set the minimum size of the window
        minimum_height = int(screen_height*minimum_size)
        minimum_width = int(minimum_height*aspect_ratio)
        self.minsize(minimum_width, minimum_height)



root = App()


root.mainloop()