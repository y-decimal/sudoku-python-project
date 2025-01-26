class Colors:
    
    disabled_colors = ( ("#d0d0cd", "#2A2A2A"),     # (Background LightMode, DarkMode)           Background color
                        ("#545454","#86ff7b") )     # (Text LightMode, DarkMode)                 Text color
    
    enabled_colors = (  ("#FFFFFF","#343638"),      # (Background LightMode, DarkMode)           Background color
                        ("#000000","#DDDDDD") )     # (Text LightMode, DarkMode)                 Text color

    highlight_colors = (("#ca7f7f","#5F4648"),      # (Enabled LightMode, Enabled DarkMode)      Background color
                        ("#c75252","#3F2628"))      # (Disabled LightMode, Disabled DarkMode)    Background color

    adjacent_colors = ( ("#baeac1","#445F48"),      # (Enabled LightMode, Enabled DarkMode)      Background color
                        ("#75a87d","#243F28"))      # (Disabled LightMode, Disabled DarkMode)    Background color

    cell_colors = adjacent_colors

    inavlid_colors = (  ("red","red"),              # (Enabled LightMode, Enabled DarkMode)     Text color
                        ("#b29626","#403823"))      # (Disabled LightMode, Disabled DarkMode)   Background color

    number_highlight_colors = ( ("#bfbf00", "#FFFF00"),     # (Enabled LightMode, Enabled DarkMode)
                                ("#bfbf00", "#FFFF00") )    # (Disabled LightMode, Disabled DarkMode)
    
class Settings:
    
    mode = "normal"
    appearance = "system"
    scale = 1.0
    
    
    def get_settings():
        var = {
            "mode": Settings.mode,
            "appearance": Settings.appearance,
            "scale": Settings.scale
        }
        return var
    
    def get_default_settings():
        var = {
            "mode": "normal",
            "appearance": "System",
            "scale": 1.0
        }
        return var
    
    def set_settings(settings):
        Settings.mode = settings["mode"]
        Settings.appearance = settings["appearance"]
        Settings.scale = settings["scale"]
        
    def set_mode(mode):
        if mode == "reset":
            Settings.mode = "normal"
        else:
            Settings.mode = mode
    
    def set_appearance(appearance):
        if appearance == "reset":
            Settings.appearance = "System"
        else:
            Settings.appearance = appearance
    
    def set_scale(scale):
        if scale == "reset":
            Settings.scale = 1.0
        else:
            Settings.scale = scale
        