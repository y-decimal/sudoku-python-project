import tkinter as tk
import customtkinter as ctk

from view.customframes.SudokugridFrame import SudokuFrame
from view.customframes.ButtonFrame import ButtonFrame
from view.customframes.CheckboxFrame import CheckboxFrame
from view.customframes.SettingsWindow import SettingsWindow
from DebugLog import Debug


DISABLED_COLORS = ( ("#d0d0cd", "#2A2A2A"),    # (Background LightMode, DarkMode)           Background color
                     ("#545454","#86ff7b") )    # (Text LightMode, DarkMode)                 Text color
    
ENABLED_COLORS = (  ("#FFFFFF","#343638"),     # (Background LightMode, DarkMode)           Background color
                    ("#000000","#DDDDDD") )    # (Text LightMode, DarkMode)                 Text color

HIGHLIGHT_COLORS = (("#ca7f7f","#5F4648"),     # (Enabled LightMode, Enabled DarkMode)      Background color
                    ("#c75252","#3F2628"))     # (Disabled LightMode, Disabled DarkMode)    Background color

ADJACENT_COLORS = ( ("#baeac1","#445F48"),     # (Enabled LightMode, Enabled DarkMode)      Background color
                    ("#75a87d","#243F28"))     # (Disabled LightMode, Disabled DarkMode)    Background color

CELL_COLORS = ADJACENT_COLORS

INVALID_COLORS = (   ("red","red"),            # (Enabled LightMode, Enabled DarkMode)     Text color
                    ("#b29626","#403823"))     # (Disabled LightMode, Disabled DarkMode)   Background color

NUMBER_HIGHLIGHT_COLOR = (  ("#bfbf00", "#FFFF00"),  # (Enabled LightMode, Enabled DarkMode)
                                ("#bfbf00", "#FFFF00") ) # (Disabled LightMode, Disabled DarkMode)

class SudokuView(ctk.CTkFrame):
    '''The main view of the Sudoku application'''

    controller = None
    previous_focus = None
    highlighted_fields = []
    invalid_fields = []
    highlighted_numbers = []
    edit_mode = False
    supress_entry_callback = False

    def __init__(self, parent):
        super().__init__(parent)


        self.widget_at_mouse = None
        ButtonFrame.font = ctk.CTkFont(family="Helvectia", size=14, weight="normal")
        
        self.setting_window = SettingsWindow(self) 
        self.setting_window.withdraw()

        # App Grid Configuration (3x3 Grid)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure((0,2), weight=1)

        
        self.bind("<Button-1>", lambda args: self.mousebutton_callback())
        
        
        # Sudoku Frame
        self.sudoku_frame = SudokuFrame(self, 9)
        self.sudoku_frame.grid(row=1, column=1, padx=10, pady=10) 
        
        for row in range(9):
            for column in range(9):
                self.sudoku_frame.get_field(row, column).bind("<Enter> ", lambda args, widget=self.sudoku_frame.get_field(row, column): self.set_mouse_position(widget))
                self.sudoku_frame.get_field(row, column).bind("<Leave>", lambda args: self.set_mouse_position(None), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-1>", lambda args: self.mousebutton_callback(), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-2>", lambda args: self.toggle_field_invalid(), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-3>", lambda args: self.toggle_field_editable(), add="+")
                self.sudoku_frame.get_field(row, column).entry_variable.trace_add("write", lambda *args, widget = self.sudoku_frame.get_field(row, column): self.entry_callback(widget))


        # Sidebar Frame 1x5 Grid
        self.sidebar_frame = ctk.CTkFrame(self)
        self.sidebar_frame.grid(row=1, column=2, padx=10, pady=10, sticky="ew")   
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        
        
        # File Load Frame Configuration
        self.file_frame = ctk.CTkFrame(self.sidebar_frame)
        self.file_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")  
        # File Button Frame
        self.file_button_frame = ButtonFrame(self.file_frame, rows = 1, columns = 2, sticky="ew")   
        self.file_button_frame.buttons[0].configure(text="Save", command = self.savebutton_callback)
        self.file_button_frame.buttons[1].configure(text="Load", command = self.loadbutton_callback)
        # File Selection Dropdown and Label
        self.load_label = ctk.CTkLabel(self.file_frame, text="Select File", font=("Arial", 16), justify="center")
        self.load_dropdown = ctk.CTkComboBox(self.file_frame, font=("Arial", 16), dropdown_font=("Arial", 14), justify="center", values=[""], command=self.dropdown_callback, state="readonly")
        # File Gridding
        self.load_label.grid(row=0, column=0, padx=25, pady=10, sticky="ew")
        self.load_dropdown.grid(row=1, column=0, padx=25, pady=25, sticky="ew")
        self.file_button_frame.grid(row=2, column=0, padx=25, pady=10, sticky="nsew")
        # File Grid weight configuration
        self.file_frame.grid_columnconfigure(0, weight=1)
        
        # Sudoku Generation Frame
        self.generate_frame = ctk.CTkFrame(self.sidebar_frame)
        self.generate_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        # Generate Title
        self.generate_frame_title = ctk.CTkLabel(self.generate_frame, text="Sudoku Generation", font=("Arial", 16), justify="center")
        # Generate Button Frame
        self.generate_button_frame = ButtonFrame(self.generate_frame, rows = 1, columns = 2, sticky="ew")
        self.generate_button_frame.buttons[0].configure(text="Generate", command = self.generatebutton_callback)
        self.generate_button_frame.buttons[1].configure(text="Reset", command = self.resetbutton_callback)
        
        # Generate Slider
        self.generate_slider_frame = ctk.CTkFrame(self.generate_frame)
        self.generate_slider_label = ctk.CTkLabel(self.generate_slider_frame, text="Difficulty = Medium", font=("Arial", 16), justify="center")
        self.generate_slider = ctk.CTkSlider(self.generate_slider_frame, from_=0.3, to=0.7, orientation="horizontal", number_of_steps=8, command=self.generateslider_callback)  
        self.generate_slider_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.generate_slider.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.generate_slider_frame.grid_columnconfigure(0, weight=1)      
        # Generate Gridding
        self.generate_frame_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.generate_button_frame.grid(row=1, column=0, padx=25, pady=10, sticky="nsew")
        self.generate_slider_frame.grid(row=2, column=0, padx=25, pady=10, sticky="nsew")
        # Generate Grid weight configuration
        self.generate_frame.grid_columnconfigure(0, weight=1)
        
        
        # Settings Button
        self.settings_button = ctk.CTkButton(self.sidebar_frame, text="Settings", command = lambda *args: self.setting_window.show())
        self.settings_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
           
        # Edit Mode Frame
        self.edit_mode_frame = ctk.CTkFrame(self.sidebar_frame)
        # Edit Mode Title
        self.edit_mode_frame_title = ctk.CTkLabel(self.edit_mode_frame, text="Sudoku Editor", font=("Arial", 16), justify="center")
        # Edit Mode Toggle Button
        self.edit_mode_toggle_fields = ctk.CTkButton(self.edit_mode_frame, text="Toggle fields", command = self.toggle_all_fields) 
        # Edit Mode Confirm Button
        self.edit_mode_confirm_button = ctk.CTkButton(self.edit_mode_frame, text="Confirm", command = lambda *args: self.set_edit_mode(0))
        # Edit Mode Gridding
        self.edit_mode_frame_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        self.edit_mode_toggle_fields.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.edit_mode_confirm_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        # Edit Mode Grid weight configuration
        self.edit_mode_frame.grid_columnconfigure((0,1), weight=1)
           
           
        # Debug Frame Configuration
        self.debug_frame = ctk.CTkFrame(self)
        
        # Frame Title
        self.debug_frame_title = ctk.CTkLabel(self.debug_frame, text="Debugging Tools", font=("Arial", 16), justify="center")
        
    	# Debug Checkbox Frame
        self.sudoku_checkbox_frame = CheckboxFrame(self.debug_frame, 2, 1)
        self.sudoku_checkbox_frame.checkboxes[0].configure(text="Save Locally", command = lambda *args, widget = self.sudoku_checkbox_frame.checkboxes[0]: self.localsave_callback(widget))
        self.sudoku_checkbox_frame.checkboxes[0].select()   
        self.sudoku_checkbox_frame.checkboxes[1].configure(text="Edit Mode", command =  self.set_edit_mode)
    
        # Debug Log Frame
        self.debug_log_frame = ctk.CTkFrame(self.debug_frame)
        self.debug_log_frame.grid_columnconfigure(0, weight=1)
        self.debug_log_frame.title = ctk.CTkLabel(self.debug_log_frame, text="Log Level", font=("Arial", 16), justify="center")
        values = (list(Debug.LOG_LEVEL.keys()))
        self.debug_log_frame.toggle = ctk.CTkOptionMenu(self.debug_log_frame, values=values, command = lambda *args: self.log_level_callback())
        self.debug_log_frame.toggle.set(values[1])
        self.log_level_callback()
        self.debug_log_frame.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.debug_log_frame.toggle.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        
        # Debug Frame Gridding
        self.debug_frame_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.sudoku_checkbox_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.debug_log_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")


        # Grid weight configuration
        self.debug_frame.grid_columnconfigure(0, weight=1)
        self.debug_frame.grid_rowconfigure((0,1,2), weight=1)
        


    def set_controller(self, controller):
        '''Sets the controller of the view'''
        self.controller = controller
        
        self.controller.set_file_mode("debug")
        
        self.refresh_settings()
        
        
    def set_mouse_position(self, widget):
        self.widget_at_mouse = widget

    def set_edit_mode(self, mode = None):
        if mode is not None:
            self.edit_mode = mode
        else:
            self.edit_mode = self.sudoku_checkbox_frame.checkboxes[1].get()
        if self.edit_mode == 1:
            self.generate_frame.grid_forget()
            self.edit_mode_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
            self.sudoku_checkbox_frame.checkboxes[1].select()
        else:
            self.edit_mode_frame.grid_forget()
            self.generate_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
            self.sudoku_checkbox_frame.checkboxes[1].deselect()
            self.savebutton_callback()
        

    def mousebutton_callback(self):
        if self.widget_at_mouse is not None:
            self.highlight_fields(self.widget_at_mouse)
            self.highlight_numbers(self.widget_at_mouse)
        else:
            self.reset_highlighted_fields()


    def entry_callback(self, widget):
        if self.supress_entry_callback:
            return
        entry_value = widget.entry_variable.get()
        if len(entry_value) > 1:
            widget.entry_variable.set(entry_value[1:])
            entry_value = entry_value[1:]

        if not entry_value.isdigit() or entry_value == "0":
            widget.entry_variable.set("")
            self.push_value(widget.get_position()[0], widget.get_position()[1], 0)
            self.set_field_valid(widget.get_position()[0], widget.get_position()[1])
            self.reset_highlighted_numbers()
        else:
            self.push_value(widget.get_position()[0], widget.get_position()[1], int(entry_value))
            self.highlight_numbers(widget)
        

    def dropdown_callback(self, *args):
            files = self.controller.get_files()
            files.append("[ New file ]")
            files.append("[ New blank Sudoku ]")
            self.load_dropdown.configure(values=files)
            dropdown_selection = self.load_dropdown.get()
            if dropdown_selection == "[ New file ]" or dropdown_selection == "[ New blank Sudoku ]":
                self.file_button_frame.buttons[0].configure(state="normal")
                self.load_dropdown.set("")
                self.load_dropdown.configure(state="normal", text_color=("#999999","#999999"), dropdown_text_color=("#999999","#999999"))
                self.load_dropdown.focus()
            else:
                self.load_dropdown.configure(state="readonly", text_color=("#111111","#99FF99"), dropdown_text_color=("#111111","#99FF99"))
            
            if not self.controller.is_file_writeable(dropdown_selection):
                self.file_button_frame.buttons[0].configure(state="disabled")
            else:
                self.file_button_frame.buttons[0].configure(state="normal")
            
            if dropdown_selection == "[ New blank Sudoku ]":
                self.controller.clear()
                self.set_edit_mode(1)


    def fetchbutton_callback(self):
        if self.controller:
            self.controller.fetch()


    def pushbutton_callback(self):
        if self.controller:
            self.controller.push()


    def generatebutton_callback(self):
        if self.controller: 
            self.controller.generate()
        
        
    def generateslider_callback(self, value):
        if self.controller: self.controller.set_difficulty(value)
        if value < 0.4:
            self.generate_slider_label.configure(text="Difficulty = Easy")
        elif value < 0.6:
            self.generate_slider_label.configure(text="Difficulty = Medium")
        else:
            self.generate_slider_label.configure(text="Difficulty = Hard")
            
        
    def resetbutton_callback(self):
        if self.controller: self.controller.reset()

    def savebutton_callback(self):
        if self.controller: 
            file_name = self.load_dropdown.get()
            if file_name != "":
                self.controller.save(file_name)
            else:
                self.controller.save("temp")
                
            self.dropdown_callback()
        
        
    def loadbutton_callback(self):
        if self.controller:
            self.supress_entry_callback = True
            file_name = self.load_dropdown.get()
            self.reset_highlighted_fields()
            if file_name != "":
                self.controller.load(file_name)
            else:
                self.controller.load("temp")
            self.reset_highlighted_numbers()
            self.supress_entry_callback = False
            
    
    def localsave_callback(self, widget):
        
        if self.controller: 
            if widget.get():
                self.controller.set_file_mode("debug")
            else:
                self.controller.set_file_mode("normal")


    def log_level_callback(self):
            Debug.current_log_level = Debug.LOG_LEVEL[self.debug_log_frame.toggle.get()]


    def toggle_field_editable(self):
        widget = self.widget_at_mouse
        if widget is not None and self.edit_mode == 1:
            row, column = widget.get_position()
            if widget.get_state():
                self.set_field_not_editable(row, column)
            else:
                self.set_field_editable(row, column)
               
            self.reset_highlighted_fields()


    def toggle_field_invalid(self):
        widget = self.widget_at_mouse
        if widget is not None and self.edit_mode == 1:
            row, column = widget.get_position()
            if widget.get_invalid_state():
                self.set_field_valid(row, column)
            else:
                self.set_field_invalid(row, column)
            self.reset_highlighted_fields()

            
    def set_all_fields_readonly(self):
        
        for row in range(9):
            for column in range(9):
                if self.get_field_value(row, column) != 0:
                    self.set_field_not_editable(row, column)
                else:
                    self.set_field_editable(row, column)
        
        self.reset_highlighted_fields()
        
        
    def set_all_fields_editable(self):
        
        for row in range(9):
            for column in range(9):
                self.set_field_editable(row, column)
        
        self.reset_highlighted_fields()
      
           
    def toggle_all_fields(self):
        
        editable_fields = 0
        readonly_fields = 0
        
        for row in range(9):
            for column in range(9):
                if self.get_field_state(row, column) and self.get_field_value(row, column) != 0:
                    editable_fields += 1
                elif self.get_field_value(row, column) != 0:
                    readonly_fields += 1
                    
        if editable_fields > readonly_fields:
            self.set_all_fields_readonly()
        else:
            self.set_all_fields_editable()
        
        self.reset_highlighted_fields() 
        
        
    def highlight_numbers(self, widget):
        
        self.reset_highlighted_numbers()
        
        if widget is None:
            return
        
        widget_position = widget.get_position()

        for row in range(9):
            for column in range(9):
                             
                if (row, column) in self.invalid_fields or (row, column) == widget_position:
                    break
                    
                if self.get_field_value(row, column) == self.get_field_value(widget_position[0], widget_position[1]) and self.get_field_value(row, column) != 0:
                    if self.get_field_state(row, column):
                        self.set_field_text_color(row, column, NUMBER_HIGHLIGHT_COLOR[0])
                    else:
                        self.set_field_text_color(row, column, NUMBER_HIGHLIGHT_COLOR[1])
                    self.highlighted_numbers.append((row, column))


    def reset_highlighted_numbers(self):
        for row, column in self.highlighted_numbers:
            if self.get_field_state(row, column): 
                self.set_field_text_color(row, column, ENABLED_COLORS[1])
            else:
                self.set_field_text_color(row, column, DISABLED_COLORS[1])
        self.highlighted_numbers = []
    
    
    def highlight_fields(self, widget):
        self.current_highlighted_fields = []
        self.highlight_cell(widget)
        self.highlight_line(widget)
        
        Debug.log_level3(f"Current highlighted fields ({len(self.current_highlighted_fields)}): {self.current_highlighted_fields}")
        Debug.log_level3(f"Actual highlighted fields ({len(self.highlighted_fields)}): {self.highlighted_fields}\n")
        # There are 4 fields (corners of the center cell) that occur twice in the list of highlighted fields
        # This appears to be because the coordinates of those fields are different when read front to back or 
        # back to front but reference the same field
        
        self.reset_previous_highlighted_fields()
        self.focus_field(widget) 
        


    def focus_field(self, widget):
        
        if self.previous_focus is not None:

            previous_widget = self.sudoku_frame.get_field(self.previous_focus[0], self.previous_focus[1])
            
            if self.previous_focus not in self.current_highlighted_fields:
                if previous_widget.get_state():
                    self.set_field_color(self.previous_focus[0], self.previous_focus[1], ENABLED_COLORS[0])
                else:
                    self.set_field_color(self.previous_focus[0], self.previous_focus[1], DISABLED_COLORS[0])
            else:
                if previous_widget.get_state():
                    self.set_field_color(self.previous_focus[0], self.previous_focus[1], ADJACENT_COLORS[0])    
                else:
                    self.set_field_color(self.previous_focus[0], self.previous_focus[1], ADJACENT_COLORS[1])
        
        
        self.previous_focus = widget.get_position()
        self.set_field_color(widget.get_position()[0], widget.get_position()[1], HIGHLIGHT_COLORS[0])

        widget.focus()
        Debug.log_level2(f"Focused field: {widget.get_position()}")
        


    def set_field_highlighted(self, row: int, column: int):
        if (row, column) in self.highlighted_fields:
            return
        self.highlighted_fields.append((row, column))
        widget = self.sudoku_frame.get_field(row, column)
        if widget.get_state():
            widget.configure(fg_color=ADJACENT_COLORS[0])
        elif widget.get_invalid_state():
            widget.configure(fg_color=INVALID_COLORS[1])
        else:
            widget.configure(fg_color=ADJACENT_COLORS[1])
        Debug.log_level3(f"Field {row}, {column} was highlighted")
            
            
    def set_field_not_highlighted(self, row: int, column: int):
        if (row, column) not in self.highlighted_fields:
            return
        self.highlighted_fields.remove((row, column))
        widget = self.sudoku_frame.get_field(row, column)
        if widget.get_state():
            widget.configure(fg_color=ENABLED_COLORS[0])
        else:
            widget.configure(fg_color=DISABLED_COLORS[0])
        Debug.log_level3(f"Field {row}, {column} was reset")


    def highlight_line(self, widget):
        row, column = widget.get_position()
        for i in range(9):
            if i != column and (row, i):
                self.set_field_highlighted(row, i)
                self.current_highlighted_fields.append((row, i))
            if i != row and (i, column):
                self.set_field_highlighted(i, column)
                self.current_highlighted_fields.append((i, column))


    def highlight_cell(self, widget):
        row, column = widget.get_position()
        row_offset = row // 3 * 3
        column_offset = column // 3 * 3
        for cell_row in range(3):
            cell_row_offset = cell_row + row_offset
            for cell_column in range(3):
                cell_column_offset = cell_column + column_offset
                if (cell_row_offset, cell_column_offset) != (row, column):
                    self.set_field_highlighted(cell_row_offset, cell_column_offset)
                    self.current_highlighted_fields.append((cell_row_offset, cell_column_offset))
  


    def reset_previous_highlighted_fields(self):
        highlighted_fields = self.highlighted_fields.copy()
        for (row, column) in highlighted_fields: 
            if (row, column) not in self.current_highlighted_fields:
                self.set_field_not_highlighted(row, column)

    def reset_highlighted_fields(self):
        Debug.log_level3(f"Resetting fields: {self.highlighted_fields}")
        fields = self.highlighted_fields.copy()
        for (row, column) in fields:
            Debug.log_level3(f"Resetting field: {row}, {column}")
            self.set_field_not_highlighted(row, column)
            Debug.log_level3(f"Current fields: {self.highlighted_fields}")
        self.highlighted_fields.clear()
        if self.previous_focus is not None:
            self.highlighted_fields.append(self.previous_focus)
            self.set_field_not_highlighted(self.previous_focus[0], self.previous_focus[1])
            self.highlighted_fields.clear()
            self.previous_focus = None


    def set_field_not_editable(self, row: int, column: int):
        widget = self.sudoku_frame.get_field(row, column)
        if widget.get_state():
            widget.configure(state="disabled")
            self.set_field_color(row, column, DISABLED_COLORS[0])
            self.set_field_text_color(row, column, DISABLED_COLORS[1])
            widget.set_state(False)


    def set_field_editable(self, row: int, column: int):
        widget = self.sudoku_frame.get_field(row, column)
        if not widget.get_state():
            widget.configure(state="normal")
            self.set_field_color(row, column, ENABLED_COLORS[0])
            self.set_field_text_color(row, column, ENABLED_COLORS[1])
            widget.set_state(True)


    def set_field_invalid(self, row: int, column: int):
        widget = self.sudoku_frame.get_field(row, column)
        if widget.get_invalid_state():
            return
        if widget.get_state():
            widget.configure(text_color=INVALID_COLORS[0])
        elif widget.get_position() in self.highlighted_fields:
            widget.configure(fg_color=INVALID_COLORS[1])
        widget.set_invalid_state(True)


    def set_field_valid(self, row: int, column: int):
        widget = self.sudoku_frame.get_field(row, column)
        if not widget.get_invalid_state():
            return
        if widget.get_state():
            widget.configure(text_color=ENABLED_COLORS[1])
        elif widget.get_position() in self.highlighted_fields:
            widget.configure(fg_color=ADJACENT_COLORS[1])
        else:
            widget.configure(fg_color=DISABLED_COLORS[0])
        widget.set_invalid_state(False)


    def update_invalid_fields(self):
        for row in range(9):
            for column in range(9):
                if (row, column) in self.invalid_fields:
                    self.set_field_invalid(row, column)
                else:
                    self.set_field_valid(row, column)


    def set_field_color(self, row: int, column: int, color: tuple):
        self.sudoku_frame.get_field(row, column).configure(fg_color=color)


    def set_field_text_color(self, row: int, column: int, color: tuple):
        self.sudoku_frame.get_field(row, column).configure(text_color=color)


    def set_field_value(self, row: int, column: int, value: int):
        if value > 0 and value < 10:
            self.sudoku_frame.get_field(row, column).set_value(value)
        elif value == 0:
            self.sudoku_frame.get_field(row, column).set_value("")


    def get_field_value(self, row: int, column: int) -> int:
        value = self.sudoku_frame.get_field(row, column).get_value()
        if value == "":
            return 0
        else:
            return int(value)


    def set_field_state(self, row: int, column: int, state: str):
        if state:
            self.set_field_editable(row, column)
        else:
            self.set_field_not_editable(row, column)


    def get_field_state(self, row: int, column: int) -> bool:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field'''
        return self.sudoku_frame.get_field(row, column).get_state()

    def get_field(self, row: int, column: int):
        return self.sudoku_frame.get_field(row, column)


    def set_mode(self, mode='normal'):
        if mode == 'debug':
            self.debug_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        else:
            self.debug_frame.grid_forget()
            
            
    def set_file_mode(self, mode='normal'):
        if mode == 'debug':
            self.sudoku_checkbox_frame.checkboxes[0].select()
        else:
            self.sudoku_checkbox_frame.checkboxes[0].deselect()
        self.dropdown_callback()


    def push_value(self, row, column, value):
        if self.controller:
            self.controller.push_value(row, column, value)
            self.update_invalid_fields()
            
            
    def update_field_size(self, window_size = None):
        if window_size is not None:
            self.sudoku_frame.set_window_size(window_size)
        else:
            window_size = self.sudoku_frame.window_size
        grid_info = self.sudoku_frame.grid_info()
        row = grid_info.get("row")
        column = grid_info.get("column")
        sticky = grid_info.get("sticky")
        load_frame = ctk.CTkFrame(self, width=window_size*0.75, height=window_size*0.75)
        self.sudoku_frame.grid_forget()
        load_frame.grid(row=row, column=column, sticky=sticky)
        self.sudoku_frame.configure(width=window_size*0.75, height=window_size*0.75)
        self.sudoku_frame.update_entries()
        load_frame.grid_forget()
        self.sudoku_frame.grid(row=row, column=column, sticky=sticky)
            
            
    def switch_setting(self, setting, value):
        if not self.controller:
            return
        if setting == "debug":
            if value == 1:
                self.controller.set_mode("debug")
            else:
                self.controller.set_mode("normal")
                            
            
    def set_scale(self, scale):
        self.sudoku_frame.set_scale(scale)
        self.update_field_size()
        
        
    def set_appearance(self, mode):
        ctk.set_appearance_mode(mode)
        
        
    def refresh_settings(self):
        self.setting_window.load_settings()
            

