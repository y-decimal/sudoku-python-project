import customtkinter as ctk
from view.Settings import Colors

class ColorPicker(ctk.CTkFrame):
    
    def __init__(self, parent, color_var, color_name):
        
        super().__init__(parent)
        
        self.parent = parent
        self.color = None
        
        self.title = ctk.CTkLabel(self, text=color_name, font=("Arial", 18), justify="left")
        self.color_entry = ctk.CTkEntry(self, textvariable=self.color, font=("Arial", 14), justify="left")
        
        self.title.pack(padx=10, pady=10, fill="both", anchor="w")
        self.color_entry.pack(padx=10, pady=10, fill="both", anchor="w")
