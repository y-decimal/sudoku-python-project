class Colors:
    DEFAULT_DISABLED_BG_COLOR = disabled_bg_color = ("#d0d0cd", "#2A2A2A")
    DEFAULT_DISABLED_TEXT_COLOR = disabled_text_color = ("#545454", "#86ff7b")
    DEFAULT_ENABLED_BG_COLOR = enabled_bg_color = ("#FFFFFF", "#343638")
    DEFAULT_ENABLED_TEXT_COLOR = enabled_text_color = ("#000000", "#DDDDDD")
    DEFAULT_HIGHLIGHT_COLOR_ENABLED = highlight_color_enabled = ("#ca7f7f", "#5F4648")
    DEFAULT_HIGHLIGHT_COLOR_DISABLED = highlight_color_disabled = ("#c75252", "#3F2628")
    DEFAULT_ADJACENT_COLOR_ENABLED = adjacent_color_enabled = ("#baeac1", "#445F48")
    DEFAULT_ADJACENT_COLOR_DISABLED = adjacent_color_disabled = ("#75a87d", "#304734")
    DEFAULT_INVALID_TEXT_COLOR = invalid_text_color = ("#FF0000", "#FF0000")
    DEFAULT_INVALID_BG_COLOR = invalid_bg_color = ("#b29626", "#403823")
    DEFAULT_NUMBER_HIGHLIGHT_COLOR_ENABLED = number_highlight_color_enabled = ("#bfbf00", "#FFFF00")
    DEFAULT_NUMBER_HIGHLIGHT_COLOR_DISABLED = number_highlight_color_disabled = ("#bfbf00", "#FFFF00")
    
    
    
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
        
    def get_default_colors():
        return {
            "disabled_bg_color": Colors.DEFAULT_DISABLED_BG_COLOR,
            "disabled_text_color": Colors.DEFAULT_DISABLED_TEXT_COLOR,
            "enabled_bg_color": Colors.DEFAULT_ENABLED_BG_COLOR,
            "enabled_text_color": Colors.DEFAULT_ENABLED_TEXT_COLOR,
            "highlight_color_enabled": Colors.DEFAULT_HIGHLIGHT_COLOR_ENABLED,
            "highlight_color_disabled": Colors.DEFAULT_HIGHLIGHT_COLOR_DISABLED,
            "adjacent_color_enabled": Colors.DEFAULT_ADJACENT_COLOR_ENABLED,
            "adjacent_color_disabled": Colors.DEFAULT_ADJACENT_COLOR_DISABLED,
            "invalid_text_color": Colors.DEFAULT_INVALID_TEXT_COLOR,
            "invalid_bg_color": Colors.DEFAULT_INVALID_BG_COLOR,
            "number_highlight_color_enabled": Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_ENABLED,
            "number_highlight_color_disabled": Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_DISABLED
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
        Colors.disabled_bg_color = Colors.DEFAULT_DISABLED_BG_COLOR
    
    @staticmethod
    def reset_disabled_text_color():
        Colors.disabled_text_color = Colors.DEFAULT_DISABLED_TEXT_COLOR
    
    @staticmethod
    def reset_enabled_bg_color():
        Colors.enabled_bg_color = Colors.DEFAULT_ENABLED_BG_COLOR
    
    @staticmethod
    def reset_enabled_text_color():
        Colors.enabled_text_color = Colors.DEFAULT_ENABLED_TEXT_COLOR
    
    @staticmethod
    def reset_highlight_color_enabled():
        Colors.highlight_color_enabled = Colors.DEFAULT_HIGHLIGHT_COLOR_ENABLED
    
    @staticmethod
    def reset_highlight_color_disabled():
        Colors.highlight_color_disabled = Colors.DEFAULT_HIGHLIGHT_COLOR_DISABLED
    
    @staticmethod
    def reset_adjacent_color_enabled():
        Colors.adjacent_color_enabled = Colors.DEFAULT_ADJACENT_COLOR_ENABLED
    
    @staticmethod
    def reset_adjacent_color_disabled():
        Colors.adjacent_color_disabled = Colors.DEFAULT_ADJACENT_COLOR_DISABLED
    
    @staticmethod
    def reset_invalid_text_color():
        Colors.invalid_text_color = Colors.DEFAULT_INVALID_TEXT_COLOR
    
    @staticmethod
    def reset_invalid_bg_color():
        Colors.invalid_bg_color = Colors.DEFAULT_INVALID_BG_COLOR
    
    @staticmethod
    def reset_number_highlight_color_enabled():
        Colors.number_highlight_color_enabled = Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_ENABLED
    
    @staticmethod
    def reset_number_highlight_color_disabled():
        Colors.number_highlight_color_disabled = Colors.DEFAULT_NUMBER_HIGHLIGHT_COLOR_DISABLED


class Settings:
    DEFAULT_MODE = mode = "normal"
    DEFAULT_APPEARANCE = appearance = "System"
    DEFAULT_SCALE = scale = 1.0
    
    @staticmethod
    def get_settings():
        settings = {
            "mode": Settings.mode,
            "appearance": Settings.appearance,
            "scale": Settings.scale         
        }
        settings.update(Colors.get_colors())
        return settings
    
    @staticmethod
    def get_default_settings():
        settings = {
            "mode": Settings.DEFAULT_MODE,
            "appearance": Settings.DEFAULT_APPEARANCE,
            "scale": Settings.DEFAULT_SCALE
        }
        settings.update(Colors.get_default_colors())
        return settings
    
    @staticmethod
    def set_settings(settings):
        Settings.mode = settings["mode"]
        Settings.appearance = settings["appearance"]
        Settings.scale = float(settings["scale"])
        Colors.set_colors(settings)
        
        
    @staticmethod
    def reset_mode():
        Settings.mode = "normal"
    
    @staticmethod
    def reset_appearance():
        Settings.appearance = "System"
    
    @staticmethod
    def reset_scale():
        Settings.scale = 1.0
