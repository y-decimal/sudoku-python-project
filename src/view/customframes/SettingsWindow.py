import customtkinter as ctk
from view.customframes.SwitchFrame import SwitchFrame

class SettingsWindow(ctk.CTkToplevel):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        
        self.title("Settings")
        self.geometry("400x300")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.hide)

        
        self.parent = parent
        
        self.settings_frame_title = ctk.CTkLabel(self, text="Settings", font=("Arial", 34), justify="right", text_color="lightblue")
        
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
        
        self.settings_frame_title.pack(padx=10, pady=10, fill="x", anchor="ne")
        self.debug_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.appearance_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.scale_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        
        self.load_settings()
   
    def set_mode(self, *args):
        mode = self.debug_frame.switch.get()
        if mode:
            self.parent.set_mode("debug")
        else: 
            self.parent.set_mode("normal")

    def set_scale(self, *args):
        scale = self.scale_frame.scale.get()
        self.parent.set_scale(scale)
        self.scale_frame.scale_value.configure(text=f"{round(scale*100)}%")

    def set_appearance(self, *args):
        self.parent.set_appearance(self.appearance_frame.setting.get())
        print(self.appearance_frame.setting.get())
    
    def load_settings(self):
        settings = self.parent.controller.get_settings()
        if settings["mode"] == "debug":
            self.debug_frame.switch.select()
        else:
            self.debug_frame.switch.deselect()
        self.set_mode()
        
        self.appearance_frame.setting.set(settings["appearance"])
        self.set_appearance()
        
        self.scale_frame.scale.set(settings["scale"])
        self.set_scale()
    
    def hide(self):
        self.withdraw()
        self.parent.controller.save_settings()
        
    def show(self):
        self.load_settings()
        self.deiconify()