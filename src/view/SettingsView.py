import customtkinter as ctk
from view.customframes.SwitchFrame import SwitchFrame

class SettingsView(ctk.CTkFrame):
    
    parent = None
    settings = None
    controller = None
    
    def __init__(self, parent):
        
        super().__init__(parent)
        
        self.parent = parent
        
        self.settings = None
        
        
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
        
        self.debug_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.appearance_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.scale_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        
   
   
    def set_controller(self, controller):
        self.controller = controller
        self.load_settings()
   
   
    def set_mode(self, *args):
        mode = self.debug_frame.switch.get()
        if mode:
            self.controller.set_mode("debug")
        else: 
            self.controller.set_mode("normal")
        self.save_settings()


    def set_scale(self, *args):
        scale = round(self.scale_frame.scale.get(), 2)
        self.controller.set_scale(scale)
        self.scale_frame.scale_value.configure(text=f"{round(scale*100)}%")
        self.save_settings()


    def set_appearance(self, *args):
        self.controller.set_appearance(self.appearance_frame.setting.get())
        self.save_settings()

    
    
    def load_settings(self):
        settings = self.controller.load_settings()
        if settings == self.settings:
            return
        if settings["mode"] == "debug":
            self.debug_frame.switch.select()
        else:
            self.debug_frame.switch.deselect()
        self.set_mode()
        
        self.appearance_frame.setting.set(settings["appearance"])
        self.set_appearance()
        
        self.scale_frame.scale.set(float(settings["scale"]))
        self.set_scale()

        self.settings = settings    
    
    def save_settings(self):
        settings = {
            "mode": "debug" if self.debug_frame.switch.get() else "normal",
            "appearance": self.appearance_frame.setting.get(),
            "scale": str(round(self.scale_frame.scale.get(), 2))
        }
        self.controller.save_settings(settings)
        
        self.settings = settings
    
    