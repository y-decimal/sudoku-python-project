class Colors:
    disabled_bg_color = ("#d0d0cd", "#2A2A2A")
    disabled_text_color = ("#545454", "#86ff7b")
    enabled_bg_color = ("#FFFFFF", "#343638")
    enabled_text_color = ("#000000", "#DDDDDD")
    highlight_color_enabled = ("#ca7f7f", "#5F4648")
    highlight_color_disabled = ("#c75252", "#3F2628")
    adjacent_color_enabled = ("#baeac1", "#445F48")
    adjacent_color_disabled = ("#75a87d", "#243F28")
    invalid_text_color = ("#FF0000", "#FF0000")
    invalid_bg_color = ("#b29626", "#403823")
    number_highlight_color_enabled = ("#bfbf00", "#FFFF00")
    number_highlight_color_disabled = ("#bfbf00", "#FFFF00")
    
    @staticmethod
    def get_colors():
        return {
            "disabled_bg_color": Colors.disabled_bg_color,
            "disabled_text_color": Colors.disabled_text_color,
            "enabled_bg_color": Colors.enabled_bg_color,
            "enabled_text_color": Colors.enabled_text_color,
            "highlight_color_enabled": Colors.highlight_color_enabled,
            "highlight_color_disabled": Colors.highlight_color_disabled,
            "adjacent_color_enabled": Colors.adjacent_color_enabled,
            "adjacent_color_disabled": Colors.adjacent_color_disabled,
            "invalid_text_color": Colors.invalid_text_color,
            "invalid_bg_color": Colors.invalid_bg_color,
            "number_highlight_color_enabled": Colors.number_highlight_color_enabled,
            "number_highlight_color_disabled": Colors.number_highlight_color_disabled
        }
    
    @staticmethod
    def set_colors(colors: dict):
        Colors.disabled_bg_color = colors["disabled_bg_color"]
        Colors.disabled_text_color = colors["disabled_text_color"]
        Colors.enabled_bg_color = colors["enabled_bg_color"]
        Colors.enabled_text_color = colors["enabled_text_color"]
        Colors.highlight_color_enabled = colors["highlight_color_enabled"]
        Colors.highlight_color_disabled = colors["highlight_color_disabled"]
        Colors.adjacent_color_enabled = colors["adjacent_color_enabled"]
        Colors.adjacent_color_disabled = colors["adjacent_color_disabled"]
        Colors.invalid_text_color = colors["invalid_text_color"]
        Colors.invalid_bg_color = colors["invalid_bg_color"]
        Colors.number_highlight_color_enabled = colors["number_highlight_color_enabled"]
        Colors.number_highlight_color_disabled = colors["number_highlight_color_disabled"]
    
    @staticmethod
    def reset_colors():
        Colors.reset_disabled_bg_color()
        Colors.reset_disabled_text_color()
        Colors.reset_enabled_bg_color()
        Colors.reset_enabled_text_color()
        Colors.reset_highlight_color_enabled()
        Colors.reset_highlight_color_disabled()
        Colors.reset_adjacent_color_enabled()
        Colors.reset_adjacent_color_disabled()
        Colors.reset_invalid_text_color()
        Colors.reset_invalid_bg_color()
        Colors.reset_number_highlight_color_enabled()
        Colors.reset_number_highlight_color_disabled()
    
    
    @staticmethod
    def reset_disabled_bg_color():
        Colors.disabled_bg_color = ("#d0d0cd", "#2A2A2A")
    
    @staticmethod
    def reset_disabled_text_color():
        Colors.disabled_text_color = ("#545454", "#86ff7b")
    
    @staticmethod
    def reset_enabled_bg_color():
        Colors.enabled_bg_color = ("#FFFFFF", "#343638")
    
    @staticmethod
    def reset_enabled_text_color():
        Colors.enabled_text_color = ("#000000", "#DDDDDD")
    
    @staticmethod
    def reset_highlight_color_enabled():
        Colors.highlight_color_enabled = ("#ca7f7f", "#5F4648")
    
    @staticmethod
    def reset_highlight_color_disabled():
        Colors.highlight_color_disabled = ("#c75252", "#3F2628")
    
    @staticmethod
    def reset_adjacent_color_enabled():
        Colors.adjacent_color_enabled = ("#baeac1", "#445F48")
    
    @staticmethod
    def reset_adjacent_color_disabled():
        Colors.adjacent_color_disabled = ("#75a87d", "#243F28")
    
    @staticmethod
    def reset_invalid_text_color():
        Colors.invalid_text_color = ("#FF0000", "#FFFF00")
    
    @staticmethod
    def reset_invalid_bg_color():
        Colors.invalid_bg_color = ("#b29626", "#403823")
    
    @staticmethod
    def reset_number_highlight_color_enabled():
        Colors.number_highlight_color_enabled = ("#bfbf00", "#FFFF00")
    
    @staticmethod
    def reset_number_highlight_color_disabled():
        Colors.number_highlight_color_disabled = ("#bfbf00", "#FFFF00")


class Settings:
    mode = "normal"
    appearance = "System"
    scale = 1.0
    
    @staticmethod
    def get_settings():
        return {
            "mode": Settings.mode,
            "appearance": Settings.appearance,
            "scale": Settings.scale
        }
    
    @staticmethod
    def get_default_settings():
        return {
            "mode": "normal",
            "appearance": "System",
            "scale": 1.0
        }
    
    @staticmethod
    def set_settings(settings):
        Settings.mode = settings["mode"]
        Settings.appearance = settings["appearance"]
        Settings.scale = settings["scale"]
        
    @staticmethod
    def reset_mode():
        Settings.mode = "normal"
    
    @staticmethod
    def reset_appearance():
        Settings.appearance = "System"
    
    @staticmethod
    def reset_scale():
        Settings.scale = 1.0
