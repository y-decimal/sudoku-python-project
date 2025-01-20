import tkinter as tk
import customtkinter as ctk

from view.SudokuView import SudokuView

class View(ctk.CTkFrame):

    parent = None
    controller = None


    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

    def set_controller(self, controller):
        self.controller = controller
        
    def init_sudoku_view(self):
        self.sudoku_view = SudokuView(self)
        self.sudoku_view.set_controller(self.controller)
        self.show_sudoku_view()
    
    def show_sudoku_view(self):
        self.sudoku_view.pack(fill="both", expand=True)