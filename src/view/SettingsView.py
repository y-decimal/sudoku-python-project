import customtkinter as ctk
from view.customframes.SwitchFrame import SwitchFrame
from view.Settings import Settings
from view.Settings import Colors
from view.customframes.ColorPicker import ColorPicker
from view.customframes.ButtonFrame import ButtonFrame


class SettingsView(ctk.CTkFrame):
    
    parent = None

    controller = None
    
    def __init__(self, parent):
        
        super().__init__(parent)
        
        self.parent = parent
        
        
        
        self.debug_frame = ctk.CTkFrame(self)
        self.debug_frame.title = ctk.CTkLabel(self.debug_frame, text="Debug Mode", font=("Arial", 18), justify="right")
        self.debug_frame.switch = ctk.CTkSwitch(self.debug_frame, text="", command=self.set_mode)
        self.debug_frame.title.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.debug_frame.switch.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.debug_frame.grid_rowconfigure(0, weight=1)

        
        self.appearance_frame = ctk.CTkFrame(self)
        self.appearance_frame.title = ctk.CTkLabel(self.appearance_frame, text="Appearance", font=("Arial", 18), justify="right")
        self.appearance_frame.setting = ctk.CTkSegmentedButton(self.appearance_frame, values=["System","Dark", "Light"], font=("Arial", 14), command=self.set_appearance)
        self.appearance_frame.title.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.appearance_frame.setting.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.appearance_frame.grid_rowconfigure(0, weight=1)
        
        
        self.scale_frame = ctk.CTkFrame(self)
        self.scale_frame.label = ctk.CTkLabel(self.scale_frame, text=f"Scale", font=("Arial", 18), justify="right")
        self.scale_frame.scale = ctk.CTkSlider(self.scale_frame, from_=0.5, to=2.0, number_of_steps=15, orientation="horizontal", command=self.set_scale)
        self.scale_frame.scale_value = ctk.CTkLabel(self.scale_frame, text="100%", font=("Arial", 18), justify="right")
        self.scale_frame.label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.scale_frame.scale_value.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        self.scale_frame.scale.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.scale_frame.grid_rowconfigure(0, weight=1)
        
        self.color_picker = SudokuColorSettings(self)
        
        self.reset_button = ctk.CTkButton(self, text="Reset to defaults", command=self.reset_settings)
        
        self.debug_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.appearance_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.scale_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.color_picker.pack(padx=10, pady=10, fill="both", anchor="e")
        self.reset_button.pack(padx=10, pady=10, fill="both", anchor="e")
        
   
   
    def set_controller(self, controller):
        self.controller = controller
        self.load_settings()
   
   
    def set_mode(self, *args):
        mode = self.debug_frame.switch.get()
        if mode:
            self.controller.set_mode("debug")
            Settings.mode="debug"
        else: 
            self.controller.set_mode("normal")
            Settings.mode="normal"
        self.save_settings()


    def set_scale(self, *args):
        scale = round(self.scale_frame.scale.get(), 2)
        self.controller.set_scale(scale)
        self.scale_frame.scale_value.configure(text=f"{round(scale*100)}%")
        Settings.scale = scale
        self.save_settings()


    def set_appearance(self, *args):
        self.controller.set_appearance(self.appearance_frame.setting.get())
        self.color_picker.set_appearance_mode(self.appearance_frame.setting.get())
        Settings.appearance = self.appearance_frame.setting.get()
        self.save_settings()

    
    
    def load_settings(self):
        self.controller.load_settings()
        settings = Settings.get_settings()
        if settings["mode"] == "debug":
            self.debug_frame.switch.select()
        else:
            self.debug_frame.switch.deselect()
        self.set_mode()
        
        self.appearance_frame.setting.set(settings["appearance"])
        self.set_appearance()
        
        self.scale_frame.scale.set(float(settings["scale"]))
        self.set_scale()
  
    
    def save_settings(self):
        self.controller.save_settings(Settings.get_settings())
        
        
    def reset_settings(self):
        Settings.set_settings(Settings.get_default_settings())
        self.save_settings()
        self.load_settings()
        
    
    
    
    
class SudokuColorSettings(ctk.CTkFrame):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        
        self.parent = parent
        self.current_mode = ctk.get_appearance_mode()
        self.pickers = []
        
        self.top_frame = ctk.CTkFrame(self)
        self.title = ctk.CTkLabel(self.top_frame, text="Colors", font=("Arial", 18), justify="left")
        self.confirm_button = ctk.CTkButton(self.top_frame, text="Confirm all", width=30, command=self.confirm)
        self.reset_button = ctk.CTkButton(self.top_frame, text="Reset all", width=30, command=self.reset)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.confirm_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.reset_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        
        self.enabled_color = ColorPicker(self, "Editable", Colors.enabled_bg_color[1], Colors.enabled_text_color[1])
        self.pickers.append(self.enabled_color)
        self.enabled_color.update_button(["Background", "Text"])
        self.disabled_color = ColorPicker(self, "Given", Colors.disabled_bg_color[1], Colors.disabled_text_color[1])
        self.pickers.append(self.disabled_color)
        self.disabled_color.update_button(["Background", "Text"]) 
        self.invalid_color = ColorPicker(self, "Invalid", Colors.invalid_bg_color[1], Colors.invalid_text_color[1])
        self.pickers.append(self.invalid_color)
        self.invalid_color.update_button(["Background", "Text"]) 
        
        self.highlight_color = ColorPicker(self, "Highlight", Colors.highlight_color_enabled[1], Colors.highlight_color_disabled[1])
        self.pickers.append(self.highlight_color)
        self.adjacent_color = ColorPicker(self, "Adjacent", Colors.adjacent_color_enabled[1], Colors.adjacent_color_disabled[1])
        self.pickers.append(self.adjacent_color)
        self.number_highlight_color = ColorPicker(self, "Number Highlight", Colors.number_highlight_color_enabled[1], Colors.number_highlight_color_disabled[1])
        self.pickers.append(self.number_highlight_color)

        
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=6)
        self.enabled_color.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.disabled_color.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.invalid_color.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.highlight_color.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
        self.adjacent_color.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")
        self.number_highlight_color.grid(row=1, column=5, padx=10, pady=10, sticky="nsew")
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        
        
    def set_appearance_mode(self, mode_string):
        mode = 0 if mode_string == "Light" else 1
        for picker in self.pickers:
            ...
        
    def confirm(self):
        mode = 0 if self.current_mode == "Light" else 1
        
        temp_list = list(Colors.enabled_bg_color)
        temp_list[mode] = self.enabled_color.color_var1
        Colors.enabled_bg_color = tuple(temp_list)
        
        temp_list = list(Colors.enabled_text_color)
        temp_list[mode] = self.enabled_color.color_var2
        Colors.enabled_text_color = tuple(temp_list)
        
        temp_list = list(Colors.disabled_bg_color)
        temp_list[mode] = self.disabled_color.color_var1
        Colors.disabled_bg_color = tuple(temp_list)
        
        temp_list = list(Colors.disabled_text_color)
        temp_list[mode] = self.disabled_color.color_var2
        Colors.disabled_text_color = tuple(temp_list)
        
        temp_list = list(Colors.invalid_bg_color)
        temp_list[mode] = self.invalid_color.color_var1
        Colors.invalid_bg_color = tuple(temp_list)
        
        temp_list = list(Colors.invalid_text_color)
        temp_list[mode] = self.invalid_color.color_var2
        Colors.invalid_text_color = tuple(temp_list)
        
        temp_list = list(Colors.highlight_color_enabled)
        temp_list[mode] = self.highlight_color.color_var1
        Colors.highlight_color_enabled = tuple(temp_list)
        
        temp_list = list(Colors.highlight_color_disabled)
        temp_list[mode] = self.highlight_color.color_var2
        Colors.highlight_color_disabled = tuple(temp_list)
        
        temp_list = list(Colors.adjacent_color_enabled)
        temp_list[mode] = self.adjacent_color.color_var1
        Colors.adjacent_color_enabled = tuple(temp_list)
        
        temp_list = list(Colors.adjacent_color_disabled)
        temp_list[mode] = self.adjacent_color.color_var2
        Colors.adjacent_color_disabled = tuple(temp_list)
        
        temp_list = list(Colors.number_highlight_color_enabled)
        temp_list[mode] = self.number_highlight_color.color_var1
        Colors.number_highlight_color_enabled = tuple(temp_list)
        
        temp_list = list(Colors.number_highlight_color_disabled)
        temp_list[mode] = self.number_highlight_color.color_var2
        Colors.number_highlight_color_disabled = tuple(temp_list)

        self.parent.save_settings()
        self.parent.controller.update_colors()
        
    def reset(self):
        for picker in self.pickers:
            picker.reset_both_colors()