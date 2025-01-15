import customtkinter as ctk
from view.customframes.SwitchFrame import SwitchFrame

class SettingsWindow(ctk.CTkToplevel):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        
        self.title("Settings")
        self.geometry("400x300")
        self.resizable(False, False)
        self.focus_set()
        
        self.parent = parent
        
        self.settings_frame_title = ctk.CTkLabel(self, text="Settings", font=("Arial", 34), justify="right", text_color="lightblue")
        
        self.settings_switch_frame = SwitchFrame(self, rows=3, columns=1)
        
        i = 0
        setting = [("Debug Mode", "debug"), ("Light Mode", "mode"), ("To be added", "")]
        for switch in self.settings_switch_frame.switches:
            switch.configure(text=setting[i][0], font=("Arial", 18), command = lambda *args, setting = setting[i][1], widget = switch: self.switch(setting, widget))
            i += 1
        self.settings_switch_frame.switches[0].select()
        
        self.scale_frame = ctk.CTkFrame(self)
        
        self.scale_frame.label = ctk.CTkLabel(self.scale_frame, text=f"Scale", font=("Arial", 18), justify="right")
        self.scale_frame.scale = ctk.CTkSlider(self.scale_frame, from_=0.5, to=2.0, number_of_steps=15, orientation="horizontal", command=self.set_scale)
        self.scale_frame.scale_value = ctk.CTkLabel(self.scale_frame, text="100%", font=("Arial", 18), justify="right")
        self.scale_frame.scale.set(1.0)
        
        self.scale_frame.grid_rowconfigure(0, weight=1)
        # self.scale_frame.grid_columnconfigure(0, weight=1)
        # self.scale_frame.grid_columnconfigure(1, weight=10)
        # self.scale_frame.grid_columnconfigure(2, weight=1)
        
        self.scale_frame.label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.scale_frame.scale_value.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        self.scale_frame.scale.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        

        self.settings_frame_title.pack(padx=10, pady=10, fill="x", anchor="ne")
        self.settings_switch_frame.pack(padx=10, pady=10, fill="both", anchor="e")
        self.scale_frame.pack(padx=10, pady=10, fill="both", anchor="e")
   
    def switch(self, setting, widget):
        self.parent.switch_setting(setting, widget.get())

    def set_scale(self, *args):
        scale = self.scale_frame.scale.get()
        self.parent.set_scale(scale)
        self.scale_frame.scale_value.configure(text=f"{round(scale*100)}%")
