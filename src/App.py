from pathlib import Path

import customtkinter as ctk
from tkinter import ttk
from model.model import Model
from view.view import View
from controller.controller import Controller

basedir = str(Path(__file__).parent.parent)

icon_path = "/assets/images/sudoku.ico"

runtime_icon_path = basedir + icon_path

class App(ctk.CTk):
    
    model = None
    view = None
    controller = None

    def __init__(self):

        super().__init__()
        
        self.sudoku_test_text = "Sudoku MVC Test"
        self.relative_size = 0.6
        self.minimum_size = self.relative_size
        self.aspect_ratio = 14/9

        # set window title, window size and aspect ratio
        self.set_window_parameters()

        # set the icon of the window
        self.iconbitmap(runtime_icon_path)


        self.model = Model()


        self.view = View(self)
        self.view.pack(fill="both", expand=True)

        self.controller = Controller(self.model, self.view)
        
        self.view.set_controller(self.controller)
        self.controller.set_mode("debug")
        
        self.update_window_height()
        
        self.bind("<Configure>", self.update_window_height)


    def set_window_parameters(self):
        '''Sets window title, window size and aspect ratio'''

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



    def update_window_height(self, *args):
        '''Updates the window height and width'''
    
        self.prev_window_height = self.window_height
        self.prev_window_width = self.window_width
        
        self.window_height = self.winfo_height()
        self.window_width = self.winfo_width()
        
        if self.prev_window_height != self.window_height and self.prev_window_width != self.window_width:
            self.view.update_field_size(self.window_height)

        


if __name__ == "__main__":
    
    app = App()
    app.mainloop()