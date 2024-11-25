import tkinter as tk


class App(tk.Tk):

    def __init__(self):

        super().__init__()

        SUDOKU_TEST_TEXT = "Sudoku Test Print"
        RELATIVE_SIZE = 0.5
        MINIMUM_SIZE = 0.25
        ASPECT_RATIO = 5/4

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        #set the window size relative to the screen size
        self.window_height = int(self.screen_height*RELATIVE_SIZE)
        self.window_width = int(self.window_height*ASPECT_RATIO)

        self.title(SUDOKU_TEST_TEXT)

        self.configure(bg="#1f1f1f")

        self.set_window_size(RELATIVE_SIZE, MINIMUM_SIZE, ASPECT_RATIO)

        #self.iconbitmap('./assets/images/sudoku.ico')


        self.sudoku_frame = tk.Frame(self)
        self.sudoku_frame.configure(borderwidth=5)

        # App Grid Configuration
        #self.grid_columnconfigure((0,3), weight=1)
        #self.grid_rowconfigure((0,3), weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)


        # Frame Grid Configuration
        

        self.sudoku_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.sudoku_frame.grid_rowconfigure( (0,1,2,3,4,5,6,7,8), weight=1)

        self.sudoku_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2) 

        class SudokuField(tk.Text):

            def __init__(self, master, row, column, window_height, scale):      


                self.entry_variable = tk.StringVar()          
                super().__init__(master,  
                                 background="#1f1f1f",
                                 foreground="white",
                                 font=("Arial", 30), 
                                 width=30,
                                 textvariable=self.entry_variable, 
                                 justify="center"
                                )
                # self.configure(borderwidth=1)
                self.grid(row=row, column=column, sticky="nsew")
                self.entry_variable.trace_add("write", self.callback)


            def callback(self , *args):

                #pass
                if len(self.entry_variable.get()) > 1:
                    self.entry_variable.set(self.entry_variable.get()[:1])

                if not self.entry_variable.get().isdigit():
                    self.entry_variable.set("")



        self.sudoku_field = []
        for i in range(9*9):

            # sticky = ""

            # if i//9 == 0: 
            #     sticky += "n"
            # elif i//9 == 8:
            #     sticky += "s"


            # if i%9 == 0:
            #     sticky += "w"
            # elif i%9 == 8:
            #     sticky += "e"


            # print(sticky)

            self.sudoku_field.append(SudokuField(self.sudoku_frame, i//9, i%9, self.window_height, 0.15))



        self.sudoku_button_frame = tk.Frame(self)


        self.button1 = tk.Button(self.sudoku_button_frame, text="Click Me!", command=self.button_callback)
        self.button1.grid(row = 0, column = 0, padx=10, pady=10, sticky="ew")


        self.clear_button = tk.Button(self.sudoku_button_frame, text="Clear", command=self.clearbutton_callback)
        self.clear_button.grid(row = 0, column = 1, padx=10, pady=10, sticky="ew")


        self.toggle_button = tk.Button(self.sudoku_button_frame, text="Toggle Test", command=self.togglebutton_callback)
        self.toggle_state = True
        self.toggle_button.grid(row = 0, column = 2, padx=10, pady=10, sticky="ew")


        self.sudoku_button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.sudoku_button_frame.grid_columnconfigure((0,2), weight=1)
        self.sudoku_button_frame.grid_rowconfigure(0, weight=1)
        # self.sudoku_button_frame.configure(borderwidth=3)



        self.label = tk.Label(self, text="", font=("Arial", 20), justify="center")
        self.label.grid(row = 1, column = 1, padx=10, pady=10, sticky="ew")
        #self.label.configure(bg_color="darkblue")


        self.labelTopright = tk.Label(self, text="TEST", font=("Arial", 20), justify="center")
        # self.labelTopright.grid(row = 0, column = 1, padx=10, pady=10, sticky="ew")
        # self.labelTopright.configure(bg_color="darkblue")


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

    def set_window_size(self, relative_size, minimum_size, aspect_ratio):

        # find the center point of the screen
        center_x = int(self.screen_width/2 - self.window_width/2)
        center_y = int(self.screen_height/2 - self.window_height/2)

        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        # set the minimum size of the window
        minimum_height = int(self.screen_height*minimum_size)
        minimum_width = int(minimum_height*aspect_ratio)
        self.minsize(minimum_width, minimum_height)
    



root = App()

# entry = SudokuEntry(root)

root.sudoku_field[1].entry_variable.set("1")
root.sudoku_field[1].configure(state="disabled")

root.sudoku_field[2].entry_variable.set("2")
root.sudoku_field[2].configure(state="disabled")

root.mainloop()