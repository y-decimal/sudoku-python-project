import customtkinter as ctk
from model.DummyImplementation import DummyImplementation as Model
from view.view import View
from controller.controller import Controller


class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.sudoku_test_text = "Sudoku MVC Test"
        self.relative_size = 0.55
        self.minimum_size = self.relative_size
        self.aspect_ratio = 5/4

        # set window title, window size and aspect ratio
        self.set_window_parameters()

        # set the icon of the window
        self.iconbitmap('./assets/images/sudoku.ico')


        self.model = Model()

        self.view = View(self)
        self.view.pack(fill="both", expand=True)

        self.controller = Controller(self.model, self.view)
        
        self.view.set_controller(self.controller)



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



if __name__ == "__main__":
    
    app = App()
    app.mainloop()