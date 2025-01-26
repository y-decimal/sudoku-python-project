import customtkinter as ctk
import tkinter as tk
from view.Settings import Colors
from DebugLog import Debug

class ColorPicker(ctk.CTkFrame):
    
    def __init__(self, parent, color_name, color_var1, color_var2=None):
    
        
        super().__init__(parent)
        
    
        self.parent = parent
        self.original_values = [color_var1, color_var2]
        self.color_var1 = color_var1
        self.color_var2 = color_var2
        self.current_color_value = color_var1
        self.values = ["Editable", "Given"]

                
        self.title = ctk.CTkLabel(self, text=color_name, font=("Arial", 18), justify="left")
        
        self.toggle = ctk.CTkSegmentedButton(self, values=self.values, font=("Arial", 14), command=self.toggle_color)
        self.toggle.set(self.values[0])
        
        self.color_slider_frame = ctk.CTkFrame(self)

        self.color_slider_red = ctk.CTkSlider(self.color_slider_frame, from_=0, to=255, number_of_steps=255, progress_color="#FF0000",
                                              orientation="horizontal", command=self.update_color)
        self.color_slider_green = ctk.CTkSlider(self.color_slider_frame, from_=0, to=255, number_of_steps=255, progress_color="#00FF00",
                                                orientation="horizontal", command=self.update_color)
        self.color_slider_blue = ctk.CTkSlider(self.color_slider_frame, from_=0, to=255, number_of_steps=255, progress_color="#0000FF",
                                               orientation="horizontal", command=self.update_color)
        
        # self.reset_button = ctk.CTkButton(self, text="Reset", command=self.reset_color)
        
        self.color_slider_red.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.color_slider_green.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.color_slider_blue.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        self.color_slider_frame.rowconfigure((0,1,2), weight=1)
        self.color_slider_frame.columnconfigure(0, weight=1)
        
        self.color_slider_red.set(int(self.current_color_value[1:3], 16))
        self.color_slider_green.set(int(self.current_color_value[3:5], 16))
        self.color_slider_blue.set(int(self.current_color_value[5:], 16))

        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.configure(fg_color="#999999")
        self.color_display = ctk.CTkLabel(self.display_frame, text=" ", font=("Arial", 14), justify="left", fg_color=self.current_color_value)
        self.color_display.pack(padx=3, pady=3, fill="both", anchor="w")
        
        self.reset_button = ctk.CTkButton(self, text="Reset", command=self.reset_color, width=50)
        
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        if color_var2 != None:
            self.toggle.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        self.color_slider_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        self.display_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.reset_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        self.grid_rowconfigure((0,1,2,3), weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)

    def update_color(self, *args):
        color = "#{:02X}{:02X}{:02X}".format(
            int(self.color_slider_red.get()), 
            int(self.color_slider_green.get()), 
            int(self.color_slider_blue.get())
            )
        
        self.current_color_value = color
        
        if self.toggle.get() == self.values[0]:
            self.color_var1 = color
        else:
            self.color_var2 = color
        
        self.color_display.configure(fg_color=self.current_color_value)
        
    def toggle_color(self, *args):
        
        if self.toggle.get() == self.values[0]:
            self.current_color_value = self.color_var1
        else:
            self.current_color_value = self.color_var2
        
        self.color_slider_red.set(int(self.current_color_value[1:3], 16))
        self.color_slider_green.set(int(self.current_color_value[3:5], 16))
        self.color_slider_blue.set(int(self.current_color_value[5:], 16))
        self.color_display.configure(fg_color=self.current_color_value)
        
    def update_button(self, values):
        self.toggle.configure(values=values)
        self.toggle.set(values[0])
        self.values = values
        self.toggle_color()

    def reset_color(self):
        if self.toggle.get() == self.values[0]:
            self.color_var1 = self.original_values[0]
            self.current_color_value = self.color_var1
        else:
            self.color_var2 = self.original_values[1]
            self.current_color_value = self.color_var2
            
        self.toggle_color()

    def reset_both_colors(self):
        self.color_var1 = self.original_values[0]
        self.color_var2 = self.original_values[1]
        self.reset_color()
        
    
    def load_new_colors(self, color1, color2):
        self.color_var1 = color1
        self.color_var2 = color2
        self.original_values = [color1, color2]
        self.reset_color()