import customtkinter as ctk
from model.DummyImplementation import DummyImplementation as Model
from view.view import View
from controller.controller import Controller


class App(ctk.CTk):

    def __init__(self, sudoku_test_text = "Sudoku Test", relative_size = 0.5, minimum_size = 0.5, aspect_ratio = 5/4):

        super().__init__()

        self.sudoku_test_text = sudoku_test_text
        self.relative_size = relative_size
        self.minimum_size = minimum_size
        self.aspect_ratio = aspect_ratio

        

        self.set_window_parameters()

        # set the icon of the window
        self.iconbitmap('./assets/images/sudoku.ico')

        self.title("Sudoku MVC Test")

        model = Model()

        view = View()

        controller = Controller(model, view)



    def set_window_parameters(self):
        '''Sets the parameters of the window'''

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