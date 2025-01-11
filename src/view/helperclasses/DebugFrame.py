import tkinter as tk
import customtkinter as ctk

from view.customframes.CheckboxFrame import CheckboxFrame

class DebugFrame(ctk.CTkFrame):

    def __init__(self, parent):
        
        super().__init__(parent)
        
        self.parent = parent

        # Grid Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        # Frame Title
        self.debug_frame_title = ctk.CTkLabel(self, text="Debugging Tools", font=("Arial", 16), justify="center")
        
        self.checkbox_frame = self.init_debug_checkbox_frame()
    
        self.debug_context_frame = self.init_debug_context_frame()
        
        # Debug Frame Gridding
        self.debug_frame_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")


        # Grid weight configuration

    def init_debug_checkbox_frame(self):
        
        checkbox_frame = CheckboxFrame(self, 2, 1)
        checkbox_frame.checkboxes[0].configure(text="Save Locally", command = lambda *args, widget = checkbox_frame.checkboxes[0]: self.parent.localsave_callback(widget))
        checkbox_frame.checkboxes[0].select()   
        checkbox_frame.checkboxes[1].configure(text="Edit Mode", command =  self.parent.set_edit_mode)
        
        return checkbox_frame
        
    def init_debug_context_frame(self):
        
        # Debug Context Frame
        debug_context_frame = ctk.CTkFrame(self)
        debug_context_frame.grid_columnconfigure(0, weight=1)
        
        # Context Frame Edit Mode
        self.debug_button = ctk.CTkButton(debug_context_frame, text="Toggle fields", command = self.parent.toggle_all_fields)
        
        return debug_context_frame