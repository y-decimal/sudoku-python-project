import tkinter as tk
import customtkinter as ctk

from view.SudokuView import SudokuView
from view.SettingsView import SettingsView

class View(ctk.CTkFrame):

    parent = None
    controller = None
    sudoku_view = None
    settings_view = None

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.sudoku_view = SudokuView(self)
        self.settings_view = SettingsView(self)
        
        self.view_toggle = ctk.CTkSegmentedButton(self, values=["Sudoku", "Settings"], font=("Arial", 14), command=self.toggle_view)
        self.view_toggle.pack(padx=10, pady=10, fill="x", anchor="n")
        self.view_toggle.set("Sudoku")
        self.show_sudoku_view()


    def set_controller(self, controller):
        self.controller = controller
        self.sudoku_view.set_controller(self.controller)
        self.settings_view.set_controller(self.controller)
        
    def show_sudoku_view(self):
        self.sudoku_view.pack(fill="both", expand=True)
        
    def hide_sudoku_view(self):
        self.sudoku_view.pack_forget()
        
    def show_settings_view(self):
        self.settings_view.pack(fill="both", expand=True)
    
    def hide_settings_view(self):
        self.settings_view.pack_forget()
        
    
    def toggle_view(self, *args):
        if self.view_toggle.get() == "Sudoku":
            self.show_sudoku_view()
            self.hide_settings_view()
        else:
            self.show_settings_view()
            self.hide_sudoku_view()
            
            
