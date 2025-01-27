import customtkinter as ctk
from tkinter import messagebox
from view.customframes.SwitchFrame import SwitchFrame
from view.Settings import Settings
from view.Settings import Colors
from view.customframes.ColorPicker import ColorPicker


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
        self.debug_only_test_button = ctk.CTkButton(self, text="See what changed from defaults", command=self.difference_default_settings)
        
        self.debug_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.appearance_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.scale_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.color_picker.pack(padx=10, pady=10, fill="both", anchor="e")
        self.reset_button.pack(padx=10, pady=10, fill="x", anchor="s")
        
   
   
    def set_controller(self, controller):
        self.controller = controller
        self.load_settings()
   
   
    def set_mode(self, *args):
        mode = self.debug_frame.switch.get()
        if mode:
            self.controller.set_mode("debug")
            self.debug_frame.switch.select()
            self.debug_only_test_button.pack(padx=10, pady=10, fill="x", anchor="s")    
            Settings.mode="debug"
        else: 
            self.controller.set_mode("normal")
            self.debug_frame.switch.deselect()
            self.debug_only_test_button.pack_forget()
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
        self.color_picker.current_mode = Settings.appearance
        self.color_picker.load_settings()
        self.save_settings()

    
    
    def load_settings(self):
        settings = self.controller.load_settings()
        Settings.set_settings(settings)
        
        if settings["mode"] == "debug":
            self.debug_frame.switch.select()
        else:
            self.debug_frame.switch.deselect()
        self.set_mode()
        
        self.appearance_frame.setting.set(settings["appearance"])
        self.set_appearance()
        
        self.scale_frame.scale.set(float(settings["scale"]))
        self.set_scale()
        
        self.color_picker.load_settings()
  
    
    def save_settings(self):
        self.controller.save_settings(Settings.get_settings())
        
        
    def reset_settings(self):
        Settings.set_settings(Settings.get_default_settings())
        self.save_settings()
        self.load_settings()
        
    
    def difference_default_settings(self):
        changes = []
        if Settings.DEFAULT_MODE != Settings.mode:
            changes.append(f"mode: {Settings.DEFAULT_MODE} -> {Settings.mode}")
        if Settings.DEFAULT_APPEARANCE != Settings.appearance:
            changes.append(f"appearance: {Settings.DEFAULT_APPEARANCE} -> {Settings.appearance}")
        if Settings.DEFAULT_SCALE != Settings.scale:
            changes.append(f"scale: {Settings.DEFAULT_SCALE} -> {Settings.scale}")
        if Colors.DEFAULT_ADJACENT_COLOR_DISABLED[0] != Colors.adjacent_color_disabled[0] or Colors.DEFAULT_ADJACENT_COLOR_DISABLED[1] != Colors.adjacent_color_disabled[1]:
            changes.append(f"adjacent color disabled: {Colors.DEFAULT_ADJACENT_COLOR_DISABLED} -> {Colors.adjacent_color_disabled}")
        if Colors.DEFAULT_ADJACENT_COLOR_ENABLED[0] != Colors.adjacent_color_enabled[0] or Colors.DEFAULT_ADJACENT_COLOR_ENABLED[1] != Colors.adjacent_color_enabled[1]:
            changes.append(f"adjacent color enabled: {Colors.DEFAULT_ADJACENT_COLOR_ENABLED} -> {Colors.adjacent_color_enabled}")
        if Colors.DEFAULT_DISABLED_BG_COLOR[0] != Colors.disabled_bg_color[0] or Colors.DEFAULT_DISABLED_BG_COLOR[1] != Colors.disabled_bg_color[1]:
            changes.append(f"disabled bg color: {Colors.DEFAULT_DISABLED_BG_COLOR} -> {Colors.disabled_bg_color}")
        if Colors.DEFAULT_DISABLED_TEXT_COLOR[0] != Colors.disabled_text_color[0] or Colors.DEFAULT_DISABLED_TEXT_COLOR[1] != Colors.disabled_text_color[1]:
            changes.append(f"disabled text color: {Colors.DEFAULT_DISABLED_TEXT_COLOR} -> {Colors.disabled_text_color}")
        if Colors.DEFAULT_ENABLED_BG_COLOR[0] != Colors.enabled_bg_color[0] or Colors.DEFAULT_ENABLED_BG_COLOR[1] != Colors.enabled_bg_color[1]:
            changes.append(f"enabled bg color: {Colors.DEFAULT_ENABLED_BG_COLOR} -> {Colors.enabled_bg_color}")
        if Colors.DEFAULT_ENABLED_TEXT_COLOR[0] != Colors.enabled_text_color[0] or Colors.DEFAULT_ENABLED_TEXT_COLOR[1] != Colors.enabled_text_color[1]:
            changes.append(f"enabled text color: {Colors.DEFAULT_ENABLED_TEXT_COLOR} -> {Colors.enabled_text_color}")
        if Colors.DEFAULT_HIGHLIGHT_COLOR_DISABLED[0] != Colors.highlight_color_disabled[0] or Colors.DEFAULT_HIGHLIGHT_COLOR_DISABLED[1] != Colors.highlight_color_disabled[1]:
            changes.append(f"highlight color disabled: {Colors.DEFAULT_HIGHLIGHT_COLOR_DISABLED} -> {Colors.highlight_color_disabled}")
        if Colors.DEFAULT_HIGHLIGHT_COLOR_ENABLED[0] != Colors.highlight_color_enabled[0] or Colors.DEFAULT_HIGHLIGHT_COLOR_ENABLED[1] != Colors.highlight_color_enabled[1]:
            changes.append(f"highlight color enabled: {Colors.DEFAULT_HIGHLIGHT_COLOR_ENABLED} -> {Colors.highlight_color_enabled}")
        if Colors.DEFAULT_INVALID_BG_COLOR[0] != Colors.invalid_bg_color[0] or Colors.DEFAULT_INVALID_BG_COLOR[1] != Colors.invalid_bg_color[1]:
            changes.append(f"invalid bg color: {Colors.DEFAULT_INVALID_BG_COLOR} -> {Colors.invalid_bg_color}")
        if Colors.DEFAULT_INVALID_TEXT_COLOR[0] != Colors.invalid_text_color[0] or Colors.DEFAULT_INVALID_TEXT_COLOR[1] != Colors.invalid_text_color[1]:
            changes.append(f"invalid text color: {Colors.DEFAULT_INVALID_TEXT_COLOR} -> {Colors.invalid_text_color}")
        if Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_DISABLED[0] != Colors.number_highlight_color_disabled[0] or Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_DISABLED[1] != Colors.number_highlight_color_disabled[1]:
            changes.append(f"number highlight color disabled: {Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_DISABLED} -> {Colors.number_highlight_color_disabled}")
        if Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_ENABLED[0] != Colors.number_highlight_color_enabled[0] or Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_ENABLED[1] != Colors.number_highlight_color_enabled[1]:
            changes.append(f"number highlight color enabled: {Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_ENABLED} -> {Colors.number_highlight_color_enabled}")
        
        
        if len(changes) == 0:
            messagebox.showinfo("No changes", "There are no changes from the default settings")
        else:
            messagebox.showinfo("Changed default settings", f"These settings have been changed from their defaults:\n\n" + "\n".join(changes))
        
        

        
    
    
    
    
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
        
        if self.current_mode == "Light":
            Colors.enabled_bg_color = (self.enabled_color.color_var1, Colors.enabled_bg_color[1])
            Colors.enabled_text_color = (self.enabled_color.color_var2, Colors.enabled_text_color[1])
            Colors.disabled_bg_color = (self.disabled_color.color_var1, Colors.disabled_bg_color[1])
            Colors.disabled_text_color = (self.disabled_color.color_var2, Colors.disabled_text_color[1])
            Colors.invalid_bg_color = (self.invalid_color.color_var1, Colors.invalid_bg_color[1])
            Colors.invalid_text_color = (self.invalid_color.color_var2, Colors.invalid_text_color[1])
            Colors.highlight_color_enabled = (self.highlight_color.color_var1, Colors.highlight_color_enabled[1])
            Colors.highlight_color_disabled = (self.highlight_color.color_var2, Colors.highlight_color_disabled[1])
            Colors.adjacent_color_enabled = (self.adjacent_color.color_var1, Colors.adjacent_color_enabled[1])
            Colors.adjacent_color_disabled = (self.adjacent_color.color_var2, Colors.adjacent_color_disabled[1])
            Colors.number_highlight_color_enabled = (self.number_highlight_color.color_var1, Colors.number_highlight_color_enabled[1])
            Colors.number_highlight_color_disabled = (self.number_highlight_color.color_var2, Colors.number_highlight_color_disabled[1])
        else:         
            Colors.enabled_bg_color = (Colors.enabled_bg_color[0], self.enabled_color.color_var1)
            Colors.enabled_text_color = (Colors.enabled_text_color[0], self.enabled_color.color_var2)
            Colors.disabled_bg_color = (Colors.disabled_bg_color[0], self.disabled_color.color_var1)
            Colors.disabled_text_color = (Colors.disabled_text_color[0], self.disabled_color.color_var2)
            Colors.invalid_bg_color = (Colors.invalid_bg_color[0], self.invalid_color.color_var1)
            Colors.invalid_text_color = (Colors.invalid_text_color[0], self.invalid_color.color_var2)
            Colors.highlight_color_enabled = (Colors.highlight_color_enabled[0], self.highlight_color.color_var1)
            Colors.highlight_color_disabled = (Colors.highlight_color_disabled[0], self.highlight_color.color_var2)
            Colors.adjacent_color_enabled = (Colors.adjacent_color_enabled[0], self.adjacent_color.color_var1)
            Colors.adjacent_color_disabled = (Colors.adjacent_color_disabled[0], self.adjacent_color.color_var2)
            Colors.number_highlight_color_enabled = (Colors.number_highlight_color_enabled[0], self.number_highlight_color.color_var1)
            Colors.number_highlight_color_disabled = (Colors.number_highlight_color_disabled[0], self.number_highlight_color.color_var2)
        

        self.parent.save_settings()
        self.load_settings()
        
    def reset(self):
        Colors.reset_colors()
        self.load_settings()
            
    
    def load_settings(self):
        if self.current_mode == "Light":
            self.enabled_color.load_new_colors(Colors.enabled_bg_color[0], Colors.enabled_text_color[0])
            self.disabled_color.load_new_colors(Colors.disabled_bg_color[0], Colors.disabled_text_color[0])
            self.invalid_color.load_new_colors(Colors.invalid_bg_color[0], Colors.invalid_text_color[0])
            self.highlight_color.load_new_colors(Colors.highlight_color_enabled[0], Colors.highlight_color_disabled[0])
            self.adjacent_color.load_new_colors(Colors.adjacent_color_enabled[0], Colors.adjacent_color_disabled[0])
            self.number_highlight_color.load_new_colors(Colors.number_highlight_color_enabled[0], Colors.number_highlight_color_disabled[0])
        else:
            self.enabled_color.load_new_colors(Colors.enabled_bg_color[1], Colors.enabled_text_color[1])
            self.disabled_color.load_new_colors(Colors.disabled_bg_color[1], Colors.disabled_text_color[1])
            self.invalid_color.load_new_colors(Colors.invalid_bg_color[1], Colors.invalid_text_color[1])
            self.highlight_color.load_new_colors(Colors.highlight_color_enabled[1], Colors.highlight_color_disabled[1])
            self.adjacent_color.load_new_colors(Colors.adjacent_color_enabled[1], Colors.adjacent_color_disabled[1])
            self.number_highlight_color.load_new_colors(Colors.number_highlight_color_enabled[1], Colors.number_highlight_color_disabled[1])
            
        self.parent.controller.update_colors()