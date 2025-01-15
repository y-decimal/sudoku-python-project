import tkinter as tk
import customtkinter as ctk

from view.customframes.SudokugridFrame import SudokuFrame
from view.customframes.ButtonFrame import ButtonFrame
from view.customframes.CheckboxFrame import CheckboxFrame
from view.customframes.SettingsWindow import SettingsWindow


class View(ctk.CTkFrame):

    disabled_colors = ( ("#d0d0cd", "#2F2F32"),    # (Background LightMode, DarkMode)
                        ("#545454","#86ff7b") )    # (Text LightMode, DarkMode)
    
    enabled_colors = (  ("#FFFFFF","#343638"),     # (Background LightMode, DarkMode)
                        ("#000000","#DDDDDD") )    # (Text LightMode, DarkMode)
    
    highlight_colors = (("#ca7f7f","#5F4648"),     # (Enabled LightMode, Enabled DarkMode)
                        ("#d32c2c","#3F2628"))     # (Disabled LightMode, Disabled DarkMode)
    
    adjacent_colors = ( ("#baeac1","#445F48"),     # (Enabled LightMode, Enabled DarkMode)
                        ("#75a87d","#243F28"))     # (Disabled LightMode, Disabled DarkMode)
    
    cell_color = adjacent_colors
    
    invalid_color = (   ("red","red"),         # (Enabled LightMode, Enabled DarkMode)
                        ("#e67e41","#403823"))     # (Disabled LightMode, Disabled DarkMode)


    controller = None
    highlighted_fields = []
    invalid_fields = []
    edit_mode = False
    controller = None

    def __init__(self, parent):
        super().__init__(parent)


        self.widget_at_mouse = None
        ButtonFrame.font = ctk.CTkFont(family="Helvectia", size=14, weight="normal")

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
        self.settings_button = ctk.CTkButton(self.sidebar_frame, text="Settings", command = lambda: SettingsWindow(self))
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
        self.debug_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        # Frame Title
        self.debug_frame_title = ctk.CTkLabel(self.debug_frame, text="Debugging Tools", font=("Arial", 16), justify="center")
        
    	# Debug Checkbox Frame
        self.sudoku_checkbox_frame = CheckboxFrame(self.debug_frame, 2, 1)
        self.sudoku_checkbox_frame.checkboxes[0].configure(text="Save Locally", command = lambda *args, widget = self.sudoku_checkbox_frame.checkboxes[0]: self.localsave_callback(widget))
        self.sudoku_checkbox_frame.checkboxes[0].select()   
        self.sudoku_checkbox_frame.checkboxes[1].configure(text="Edit Mode", command =  self.set_edit_mode)
    
        # Debug Context Frame
        self.debug_context_frame = ctk.CTkFrame(self.debug_frame)
        self.debug_context_frame.grid_columnconfigure(0, weight=1)
        # Context Frame Edit Mode
        self.debug_button = ctk.CTkButton(self.debug_context_frame, text="Toggle fields", command = self.toggle_all_fields)
        
        # Debug Frame Gridding
        self.debug_frame_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.sudoku_checkbox_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")


        # Grid weight configuration
        self.debug_frame.grid_columnconfigure(0, weight=1)
        self.debug_frame.grid_rowconfigure((0,1,2), weight=1)
        


    def set_controller(self, controller):
        '''Sets the controller of the view'''
        self.controller = controller
        
        self.dropdown_callback()
        
        
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
            self.reset_highlighted_fields()
            self.highlight_fields(self.widget_at_mouse)
        else:
            self.reset_highlighted_fields()


    def entry_callback(self, widget):
        entry_value = widget.entry_variable.get()
        if len(entry_value) > 1:
            widget.entry_variable.set(entry_value[1:])
            entry_value = entry_value[1:]

        if not entry_value.isdigit() or entry_value == "0":
            widget.entry_variable.set("")
            self.push_value(widget.get_position()[0], widget.get_position()[1], 0)
            self.set_field_valid(widget.get_position()[0], widget.get_position()[1])
        else:
            self.push_value(widget.get_position()[0], widget.get_position()[1], int(entry_value))
        

    def dropdown_callback(self, *args):
            files = self.controller.get_files()
            files.append("[ New file ]")
            files.append("[ New blank Sudoku ]")
            self.load_dropdown.configure(values=files)
            dropdown_selection = self.load_dropdown.get()
            if dropdown_selection == "[ New file ]" or dropdown_selection == "[ New blank Sudoku ]":
                self.file_button_frame.buttons[0].configure(state="normal")
                self.load_dropdown.set("")
                self.load_dropdown.configure(state="normal", text_color="#999999", dropdown_text_color="#999999")
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
        if self.controller: self.controller.generate()
        
        
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
            file_name = self.load_dropdown.get()
            self.reset_highlighted_fields()
            if file_name != "":
                self.controller.load(file_name)
            else:
                self.controller.load("temp")
            
    
    def localsave_callback(self, widget):
        
        if self.controller: 
            if widget.get():
                self.controller.set_mode("debug")
            else:
                self.controller.set_mode("normal")


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
        
    
    def highlight_fields(self, widget):
        row, column = widget.get_position()
        self.highlighted_fields.append((row, column))
        self.highlight_cell(widget)
        self.highlight_line(widget)

        if widget.get_state():
            widget.configure(fg_color=self.highlight_colors[0])
            widget.focus()
        else:
            widget.configure(fg_color=self.highlight_colors[1])
            widget.focus()


    def highlight_line(self, widget):
        row, column = widget.get_position()
        for i in range(9):
            if i != column:
                widget = self.sudoku_frame.get_field(row, i)
                self.highlighted_fields.append((row, i))
                if widget.get_state():
                    widget.configure(fg_color=self.adjacent_colors[0])
                elif widget.get_invalid_state():
                    widget.configure(fg_color=self.invalid_color[1])
                else:
                    widget.configure(fg_color=self.adjacent_colors[1])
            if i != row:
                widget = self.sudoku_frame.get_field(i, column)
                self.highlighted_fields.append((i, column))
                if widget.get_state():
                    widget.configure(fg_color=self.adjacent_colors[0])
                elif widget.get_invalid_state():
                    widget.configure(fg_color=self.invalid_color[1])
                else:
                    widget.configure(fg_color=self.adjacent_colors[1])


    def highlight_cell(self, widget):
        row, column = widget.get_position()
        row_offset = row // 3 * 3
        column_offset = column // 3 * 3
        for cell_row in range(3):
            cell_row_offset = cell_row + row_offset
            for cell_column in range(3):
                cell_column_offset = cell_column + column_offset
                widget = self.sudoku_frame.get_field(cell_row_offset, cell_column_offset)
                if row != cell_row_offset and column != cell_column_offset:
                    self.highlighted_fields.append((cell_row_offset, cell_column_offset))
                    if widget.get_state():
                        self.set_field_color(cell_row_offset, cell_column_offset, self.cell_color[0])
                    elif widget.get_invalid_state():
                        self.set_field_color(cell_row_offset, cell_column_offset, self.invalid_color[1])
                    else:
                        self.set_field_color(cell_row_offset, cell_column_offset, self.cell_color[1])


    def reset_highlighted_fields(self):
        for row, column in self.highlighted_fields:
            widget = self.sudoku_frame.get_field(row, column)
            if widget.get_state():
                self.set_field_color(row, column, self.enabled_colors[0])
                if widget.get_invalid_state():
                    self.set_field_text_color(row, column, self.invalid_color[0])
                else:
                    self.set_field_text_color(row, column, self.enabled_colors[1])
            else:
                self.set_field_text_color(row, column, self.disabled_colors[1])
                self.set_field_color(row, column, self.disabled_colors[0])
        self.highlighted_fields = []


    def set_field_not_editable(self, row: int, column: int):
        widget = self.sudoku_frame.get_field(row, column)
        if widget.get_state():
            widget.configure(state="disabled")
            self.set_field_color(row, column, self.disabled_colors[0])
            self.set_field_text_color(row, column, self.disabled_colors[1])
            widget.set_state(False)


    def set_field_editable(self, row: int, column: int):
        widget = self.sudoku_frame.get_field(row, column)
        if not widget.get_state():
            widget.configure(state="normal")
            self.set_field_color(row, column, self.enabled_colors[0])
            self.set_field_text_color(row, column, self.enabled_colors[1])
            widget.set_state(True)


    def set_field_invalid(self, row: int, column: int):
        widget = self.sudoku_frame.get_field(row, column)
        if widget.get_invalid_state():
            return
        if widget.get_state():
            widget.configure(text_color=self.invalid_color[0])
        elif widget.get_position() in self.highlighted_fields:
            widget.configure(fg_color=self.invalid_color[1])
        widget.set_invalid_state(True)


    def set_field_valid(self, row: int, column: int):
        widget = self.sudoku_frame.get_field(row, column)
        if not widget.get_invalid_state():
            return
        if widget.get_state():
            widget.configure(text_color=self.enabled_colors[1])
        elif widget.get_position() in self.highlighted_fields:
            widget.configure(fg_color=self.adjacent_colors[1])
        else:
            widget.configure(fg_color=self.disabled_colors[0])
        widget.set_invalid_state(False)


    def update_invalid_fields(self):
        for row in range(9):
            for column in range(9):
                if (row, column) in self.invalid_fields:
                    self.set_field_invalid(row, column)
                else:
                    self.set_field_valid(row, column)


    def set_field_color(self, row: int, column: int, color: str):
        self.sudoku_frame.get_field(row, column).configure(fg_color=color)


    def set_field_text_color(self, row: int, column: int, color: str):
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


    def set_mode(self, mode='normal'):
        if mode == 'debug':
            self.debug_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
            self.dropdown_callback()
        else:
            self.debug_frame.grid_forget()
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