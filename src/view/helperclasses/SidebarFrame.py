import tkinter as tk
import customtkinter as ctk

from view.customframes.ButtonFrame import ButtonFrame
from view.customframes.CheckboxFrame import CheckboxFrame
        
class SidebarFrame(ctk.CTkFrame):
    
    def __init__(self, parent):
                
        # Sidebar Frame 1x5 Grid
        super().__init__(parent)
        
        self.parent = parent
          
        self.grid_columnconfigure(0, weight=1)
        
        self.file_frame = self.init_file_frame()
        self.file_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        self.generate_frame = self.init_generate_frame()
        self.generate_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
    
    def init_file_frame(self):
        
         # File Load Frame Configuration
        file_frame = ctk.CTkFrame(self)
        
        # File Button Frame
        self.file_button_frame = ButtonFrame(file_frame, rows = 1, columns = 2, sticky="ew")   
        self.file_button_frame.buttons[0].configure(text="Save", command = self.parent.savebutton_callback)
        self.file_button_frame.buttons[1].configure(text="Load", command = self.parent.loadbutton_callback)
           
        # File Selection Dropdown and Label
        self.load_label = ctk.CTkLabel(file_frame, text="Select File", font=("Arial", 16), justify="center")
        self.load_dropdown = ctk.CTkComboBox(file_frame, font=("Arial", 16), dropdown_font=("Arial", 14), justify="center", values=[""], command=self.parent.dropdown_callback, state="readonly")
        
        # Gridding
        self.load_label.grid(row=0, column=0, padx=25, pady=10, sticky="ew")
        self.load_dropdown.grid(row=1, column=0, padx=25, pady=25, sticky="ew")
        self.file_button_frame.grid(row=2, column=0, padx=25, pady=10, sticky="nsew")
        
        # Grid weight configuration
        file_frame.grid_columnconfigure(0, weight=1)
        
        return file_frame
    
    def init_generate_frame(self):
        
        # Sudoku Generation Frame
        generate_frame = ctk.CTkFrame(self)
        
        # Generate Title
        generate_frame_title = ctk.CTkLabel(generate_frame, text="Sudoku Generation", font=("Arial", 16), justify="center")
        
        # Generate Button Frame
        self.generate_button_frame = ButtonFrame(generate_frame, rows = 1, columns = 2, sticky="ew")
        self.generate_button_frame.buttons[0].configure(text="Generate", command = self.parent.generatebutton_callback)
        self.generate_button_frame.buttons[1].configure(text="Clear", command = self.parent.clearbutton_callback)
        
        # Generate Slider
        self.generate_slider_frame = ctk.CTkFrame(generate_frame)
        self.generate_slider_label = ctk.CTkLabel(self.generate_slider_frame, text="Difficulty = Medium", font=("Arial", 16), justify="center")
        self.generate_slider = ctk.CTkSlider(self.generate_slider_frame, from_=0.3, to=0.7, orientation="horizontal", number_of_steps=8, command=self.parent.generateslider_callback)  
        self.generate_slider_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.generate_slider.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.generate_slider_frame.grid_columnconfigure(0, weight=1)
        
        
        # Gridding
        generate_frame_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.generate_button_frame.grid(row=1, column=0, padx=25, pady=10, sticky="nsew")
        self.generate_slider_frame.grid(row=2, column=0, padx=25, pady=10, sticky="nsew")

        # Grid weight configuration
        generate_frame.grid_columnconfigure(0, weight=1)
        
        return generate_frame