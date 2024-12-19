import tkinter as tk
import customtkinter as ctk

from view.customframes.SudokugridFrame import SudokuFrame
from view.customframes import ButtonFrame, CheckboxFrame


class View(ctk.CTkFrame):

    disabled_colors = ("#2F2F32", "#86ff7b")  # (Background color, Text color)
    enabled_colors = ("#343638", "#DDDDDD")  # (Background color, Text color)
    highlight_colors = ("#5F4648", "#3F2628")  # (Enabled color, disabled color)
    adjacent_colors = ("#445F48", "#243F28")  # (Enabled color, disabled color)
    cell_color = adjacent_colors  # (Enabled color, disabled color)
    invalid_color = ("#403823", "red")  # (Disabled background color, Enabled Text color)
    
    controller = None
    highlighted_fields = []
    invalid_fields = []
    edit_mode = False

    def __init__(self, parent):
        super().__init__(parent)

        self.widget_at_mouse = None

        # App Grid Configuration (3x3 Grid)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure((1, 2), weight=1)

        # Frame Grid Configuration

        # Sudoku Frame
        self.sudoku_frame = SudokuFrame(self, 9)
        self.sudoku_frame.grid(row=0, column=1, padx=10, pady=10)

        for row in range(9):
            for column in range(9):
                self.sudoku_frame.get_field(row, column).bind("<Enter> ", lambda args, widget=self.sudoku_frame.get_field(row, column): self.set_mouse_position(widget))
                self.sudoku_frame.get_field(row, column).bind("<Leave>", lambda args: self.set_mouse_position(None), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-1>", lambda args: self.mousebutton_callback(), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-3>", lambda args: self.toggle_field_editable(), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-2>", lambda args: self.toggle_field_invalid(), add="+")
                self.sudoku_frame.get_field(row, column).entry_variable.trace_add("write", lambda *args, widget=self.sudoku_frame.get_field(row, column): self.entry_callback(widget))

        self.bind("<Button-1>", lambda args: self.mousebutton_callback())

        self.tool_frame = ctk.CTkFrame(self)

        # Button Frame
        self.sudoku_button_frame = ButtonFrame.ButtonFrame(self.tool_frame, 1, 3)
        self.sudoku_button_frame.buttons[0].configure(text="Generate", command=self.generatebutton_callback)
        self.sudoku_button_frame.buttons[1].configure(text="Save", command=self.savebutton_callback)
        self.sudoku_button_frame.buttons[2].configure(text="Load", command=self.loadbutton_callback)
        self.sudoku_button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # File name entry
        self.file_entry = ctk.CTkEntry(self.tool_frame, width=200, placeholder_text="Enter filename", font=("Arial", 18))
        self.file_entry.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Checkbox Frame
        self.sudoku_checkbox_frame = CheckboxFrame.CheckboxFrame(self.tool_frame, 1, 2)
        self.sudoku_checkbox_frame.checkboxes[0].configure(text="Save Locally", command=lambda *args, widget=self.sudoku_checkbox_frame.checkboxes[0]: self.debugcheckbox_callback(widget))
        self.sudoku_checkbox_frame.checkboxes[0].select()
        self.sudoku_checkbox_frame.checkboxes[1].configure(text="Edit Mode", command=self.set_edit_mode)
        self.sudoku_checkbox_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.tool_frame.grid_columnconfigure((0, 1), weight=1)
        self.tool_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    def set_controller(self, controller):
        '''Sets the controller of the view'''
        self.controller = controller
        # self.bind_class("Entry", "<Button-1>", lambda *args: self.controller.push(), add="+")

    def set_mouse_position(self, widget):
        self.widget_at_mouse = widget

    def set_edit_mode(self):
        self.edit_mode = self.sudoku_checkbox_frame.checkboxes[1].get()

    def mousebutton_callback(self):
        if self.widget_at_mouse is not None:
            self.reset_highlighted_fields()
            self.highlight_fields(self.widget_at_mouse)
        else:
            self.reset_highlighted_fields()

    def entry_callback(self, widget):
        entry_value = widget.entry_variable.get()
        if len(entry_value) > 1:
            widget.entry_variable.set(widget.entry_variable.get()[1:])
            entry_value = widget.entry_variable.get()
        if not entry_value.isdigit() or entry_value == "0":
            widget.entry_variable.set("")
            entry_value = ''
            self.controller.push_value(widget.get_position()[0], widget.get_position()[1], 0)
            self.set_field_valid(widget.get_position()[0], widget.get_position()[1])
        else:
            entry_value = int(entry_value)
            self.controller.push_value(widget.get_position()[0], widget.get_position()[1], entry_value)
        for row in range(9):
            for column in range(9):
                if (row, column) in self.invalid_fields:
                    self.set_field_invalid(row, column)
                else:
                    self.set_field_valid(row, column)
        #     self.validate_field(widget)
        # if self.invalid_fields:
        #     temp_invalid_fields = self.invalid_fields.copy()
        #     for row, column in temp_invalid_fields:
        #         self.validate_field(self.sudoku_frame.get_field(row, column))

    def fetchbutton_callback(self):
        if self.controller:
            self.controller.fetch()

    def pushbutton_callback(self):
        if self.controller:
            self.controller.push()

    def generatebutton_callback(self):
        if self.controller:
            self.controller.generate()

    def savebutton_callback(self):
        if self.controller:
            file_name = self.file_entry.get()
            if file_name != "":
                self.controller.save(file_name)
            else:
                self.controller.save("test")

    def loadbutton_callback(self):
        if self.controller:
            file_name = self.file_entry.get()
            self.reset_highlighted_fields()
            if file_name != "":
                self.controller.load(file_name)
            else:
                self.controller.load("test")

    def debugcheckbox_callback(self, widget):
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
                    widget.configure(fg_color=self.invalid_color[0])
                else:
                    widget.configure(fg_color=self.adjacent_colors[1])
            if i != row:
                widget = self.sudoku_frame.get_field(i, column)
                self.highlighted_fields.append((i, column))
                if widget.get_state():
                    widget.configure(fg_color=self.adjacent_colors[0])
                elif widget.get_invalid_state():
                    widget.configure(fg_color=self.invalid_color[0])
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
                        self.set_field_color(cell_row_offset, cell_column_offset, self.invalid_color[0])
                    else:
                        self.set_field_color(cell_row_offset, cell_column_offset, self.cell_color[1])

    def reset_highlighted_fields(self):
        for row, column in self.highlighted_fields:
            widget = self.sudoku_frame.get_field(row, column)
            if widget.get_state():
                self.set_field_color(row, column, self.enabled_colors[0])
                if widget.get_invalid_state():
                    self.set_field_text_color(row, column, self.invalid_color[1])
                else:
                    self.set_field_text_color(row, column, self.enabled_colors[1])
            else:
                self.set_field_text_color(row, column, self.disabled_colors[1])
                if widget.get_invalid_state():
                    self.set_field_color(row, column, self.invalid_color[0])
                else:
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
            widget.configure(text_color=self.invalid_color[1])
        else:
            widget.configure(fg_color=self.invalid_color[0])
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
        

    # def validate_field(self, widget):
    #     if widget.get_value() == "":
    #         return
    #     row, column = widget.get_position()
    #     value = int(widget.get_value())
    #     current_cell = row // 3 * 3 + column // 3
    #     cell_index = row % 3 * 3 + column % 3
    #     valid = True
    #     for i in range(9):
    #         grid_row = i // 3 + (current_cell // 3) * 3
    #         grid_column = i % 3 + (current_cell % 3) * 3
    #         if i != column and self.get_field_value(row, i) == value:
    #             self.set_field_invalid(row, i)
    #             valid = False
    #         if i != row and self.get_field_value(i, column) == value:
    #             self.set_field_invalid(i, column)
    #             valid = False
    #         if cell_index != i and self.get_field_value(grid_row, grid_column) == value:
    #             self.set_field_invalid(grid_row, grid_column)
    #             valid = False
                
    #     if valid: 
    #         self.set_field_valid(row, column)
    #     else:
    #         self.set_field_invalid(row, column)

     
            

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
        return self.sudoku_frame.get_field(row, column).get_state()

    def set_mode(self, mode='normal'):
        for checkbox in self.sudoku_checkbox_frame.checkboxes:
            if mode == 'debug':
                checkbox.select()
                self.debugcheckbox_callback(checkbox)
            else:
                checkbox.deselect()
                self.debugcheckbox_callback(checkbox)