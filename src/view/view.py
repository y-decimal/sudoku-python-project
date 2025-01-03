import tkinter as tk
import customtkinter as ctk

from view.customframes.SudokugridFrame import SudokuFrame
from view.customframes import ButtonFrame, CheckboxFrame



class View(ctk.CTkFrame):


    

    disabled_colors = ("#2F2F32", "#86ff7b") # (Background color, Text color)
    enabled_colors = ("#343638", "#DDDDDD")  # (Background color, Text color)
    highlight_colors = ("#5F4648", "#3F2628") # (Enabled color, disabled color)
    adjacent_colors = ("#445F48", "#243F28") # (Enabled color, disabled color)
    cell_color = adjacent_colors # (Enabled color, disabled color)
    changed_fields = []
    edit_mode = False
    controller = None

    def __init__(self, parent):
        
        super().__init__(parent)
       
        self.widget_at_mouse = None
       
        # App Grid Configuration (3x3 Grid)
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure((0,2), weight=1)
        
        
        self.bind("<Button-1>", lambda args: self.mousebutton_callback())
        
        
        # Sudoku Frame
        self.sudoku_frame = SudokuFrame(self, 9)
        self.sudoku_frame.grid(row=1, column=1, padx=10, pady=10) 
        
        for row in range(9):
            for column in range(9):
                self.sudoku_frame.get_field(row, column).bind("<Enter> ", lambda args, widget = self.sudoku_frame.get_field(row, column): self.set_mouse_position(widget))
                self.sudoku_frame.get_field(row, column).bind("<Leave>", lambda args: self.set_mouse_position(None), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-1>", lambda args: self.mousebutton_callback(), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-3>", lambda args: self.toggle_field(), add="+")
                self.sudoku_frame.get_field(row, column).entry_variable.trace_add("write", lambda *args, widget = self.sudoku_frame.get_field(row, column): self.entry_callback(widget))


        # Sidebar Frame 1x5 Grid
        self.sidebar_frame = ctk.CTkFrame(self)
        self.sidebar_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")   
        # self.sidebar_frame.grid_rowconfigure((0,4), weight=1)
        # self.sidebar_frame.grid_rowconfigure((1,2,3), weight=5)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        
            
            

        # File Load Frame Configuration
        self.file_frame = ctk.CTkFrame(self.sidebar_frame)
        self.file_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        # File Button Frame
        self.file_button_frame = ButtonFrame.ButtonFrame(self.file_frame, rows = 1, columns = 2, sticky="ew")    
        self.file_button_frame.buttons[0].configure(text="Save", command = self.savebutton_callback)
        self.file_button_frame.buttons[1].configure(text="Load", command = self.loadbutton_callback)
           
        # File Selection Dropdown and Label
        self.load_label = ctk.CTkLabel(self.file_frame, text="Select File", font=("Arial", 16), justify="center")
        self.load_dropdown = ctk.CTkComboBox(self.file_frame, font=("Arial", 16), dropdown_font=("Arial", 14), justify="center", values=[""], command=self.dropdown_callback, state="readonly")
        
        # Gridding
        self.load_label.grid(row=0, column=0, padx=25, pady=10, sticky="ew")
        self.load_dropdown.grid(row=1, column=0, padx=25, pady=25, sticky="ew")
        self.file_button_frame.grid(row=2, column=0, padx=25, pady=10, sticky="nsew")
        
        # Grid weight configuration
        self.file_frame.grid_columnconfigure(0, weight=1)
        
        
        
        # Sudoku Generation Frame
        self.generate_frame = ctk.CTkFrame(self.sidebar_frame)
        self.generate_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        # Generate Title
        self.generate_frame_title = ctk.CTkLabel(self.generate_frame, text="Sudoku Generation", font=("Arial", 16), justify="center")
        
        # Generate Button Frame
        self.generate_button_frame = ButtonFrame.ButtonFrame(self.generate_frame, rows = 1, columns = 2, sticky="ew")
        self.generate_button_frame.buttons[0].configure(text="Generate", command = self.generatebutton_callback)
        self.generate_button_frame.buttons[1].configure(text="Clear", command = self.clearbutton_callback)  
        
        # Gridding
        self.generate_frame_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.generate_button_frame.grid(row=1, column=0, padx=25, pady=10, sticky="nsew")

        # Grid weight configuration
        self.generate_frame.grid_columnconfigure(0, weight=1)
           


        # Debug Frame Configuration
        self.debug_frame = ctk.CTkFrame(self)
        self.debug_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        # Frame Title
        self.debug_frame_title = ctk.CTkLabel(self.debug_frame, text="Debugging Tools", font=("Arial", 16), justify="center")
        
    	# Debug Checkbox Frame
        self.sudoku_checkbox_frame = CheckboxFrame.CheckboxFrame(self.debug_frame, 2, 1)
        self.sudoku_checkbox_frame.checkboxes[0].configure(text="Save Locally", command = lambda *args, widget = self.sudoku_checkbox_frame.checkboxes[0]: self.debugcheckbox_callback(widget))
        self.sudoku_checkbox_frame.checkboxes[0].select()   
        self.sudoku_checkbox_frame.checkboxes[1].configure(text="Edit Mode", command =  self.set_edit_mode)
    
        # Gridding
        self.debug_frame_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.sudoku_checkbox_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        # Grid weight configuration
        self.debug_frame.grid_columnconfigure(0, weight=1)
        self.debug_frame.grid_rowconfigure((0,1), weight=1)
        






    def set_controller(self, controller):
        '''Sets the controller of the view'''
        self.controller = controller

        self.bind_class("Entry","<Button-1>", lambda *args: self.controller.push(), add="+")


        def on_keypress():
            for row in range(9):
                for column in range(9):
                    self.invalid_field(row, column)
        
        self.bind_class("Entry", "<Button-1>", lambda args: on_keypress(), add="+")
        
        self.dropdown_callback()
        
        
    

    def set_mouse_position (self, widget):
        self.widget_at_mouse = widget
        # print(f"Mouse position set to: {self.mouse_position}")

    def set_edit_mode(self):
        self.edit_mode = self.sudoku_checkbox_frame.checkboxes[1].get()
        # print(f"Edit mode set to: {self.edit_mode}")

    def mousebutton_callback(self):
        # print(self.mouse_position)
        if self.widget_at_mouse != None:
            self.reset_fields()
            self.highlight_fields(self.widget_at_mouse)
        else:
            self.reset_fields()


    def entry_callback(self, widget):

        entry_value = widget.entry_variable.get()  

        if len(entry_value) > 1:
            widget.entry_variable.set(widget.entry_variable.get()[1:])
            entry_value = widget.entry_variable.get()

                    
        if (not entry_value.isdigit() or entry_value == "0"):
            widget.entry_variable.set("")
            entry_value = ''
     

        # self.invalid_field(widget.position[0], widget.position[1])
        

        

    def dropdown_callback(self, *args):
            files = self.controller.get_files()
            files.append("[ new file ]")
            self.load_dropdown.configure(values=files)
            if self.load_dropdown.get() == "[ new file ]":
                self.file_button_frame.buttons[1].configure(state="normal")
                self.load_dropdown.set("")
                self.load_dropdown.configure(state="normal", text_color="#999999", dropdown_text_color="#999999")
                self.load_dropdown.focus()
            else:
                self.load_dropdown.configure(state="readonly", text_color="#99FF99", dropdown_text_color="#99FF99")
            
            if not self.controller.is_file_writeable(self.load_dropdown.get()):
                self.file_button_frame.buttons[1].configure(state="disabled")
            else:
                self.file_button_frame.buttons[1].configure(state="normal")


    def fetchbutton_callback(self):
        if self.controller: self.controller.fetch()
        
    def pushbutton_callback(self):
        if self.controller: self.controller.push()
       
    def generatebutton_callback(self):
        if self.controller: self.controller.generate()
        
    def clearbutton_callback(self):
        if self.controller: self.controller.clear()

    def savebutton_callback(self):
        if self.controller: 
            file_name = self.load_dropdown.get()
            
            
            if file_name != "":
                self.controller.save(file_name)
            else:
                self.controller.save("test")
                
            self.dropdown_callback()
        
    def loadbutton_callback(self):

        if self.controller: 
            file_name = self.load_dropdown.get()
            self.reset_fields()
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


    def toggle_field(self):
        
        if self.widget_at_mouse != None and self.edit_mode == 1:
                       
            row, column = self.widget_at_mouse.get_position()
                       
            if self.widget_at_mouse.get_state():
                self.set_field_not_editable(row, column)

            else:
                self.set_field_editable(row, column)
               
            self.reset_fields()

            
    def toggle_all_fields(self):
        
        for row in range(9):
            for column in range(9):
                if self.get_field_value(row, column) != 0:
                    self.set_field_not_editable(row, column)
                else:
                    self.set_field_editable(row, column)
        
        self.reset_fields()
      


    def highlight_fields(self, widget):

        row, column = widget.get_position()        
        self.changed_fields.append((row, column))
        
        self.highlight_cell(widget)

        if widget.get_state():
            widget.configure(fg_color=self.highlight_colors[0])
            widget.focus()
        else:
            widget.configure(fg_color=self.highlight_colors[1])
            widget.focus()
        
        for i in range(9):
            if i != column:
                self.changed_fields.append((row, i))
                if self.sudoku_frame.get_field(row, i).get_state():
                    self.sudoku_frame.get_field(row, i).configure(fg_color=self.adjacent_colors[0])
                else:
                    self.sudoku_frame.get_field(row, i).configure(fg_color=self.adjacent_colors[1])

            if i != row:
                self.changed_fields.append((i, column))
                if self.sudoku_frame.get_field(i, column).get_state():
                    self.sudoku_frame.get_field(i, column).configure(fg_color=self.adjacent_colors[0])
                else:
                    self.sudoku_frame.get_field(i, column).configure(fg_color=self.adjacent_colors[1])
                    
        
                
    def highlight_cell(self, widget):
         
         row, column = widget.get_position() 

         row_offset = row//3*3
         column_offset = column//3*3    

         for cell_row in range(3):
             
             cell_row_offset = cell_row + row_offset

             for cell_column in range(3):

                cell_column_offset = cell_column + column_offset

                if row != cell_row_offset and column != cell_column_offset:
                    self.changed_fields.append((cell_row_offset, cell_column_offset))

                    if self.sudoku_frame.get_field(cell_row_offset, cell_column_offset).get_state():
                        self.set_field_color(cell_row_offset, cell_column_offset, self.cell_color[0])
                        
                    else:
                        self.set_field_color(cell_row_offset, cell_column_offset, self.cell_color[1])      
    
    
    
    def reset_fields(self, mode = 'changed'):

        if mode == 'all':
            self.changed_fields = [(row, column) for row in range(9) for column in range(9)]
            
        for row, column in self.changed_fields:
                
            if self.sudoku_frame.get_field(row, column).get_state():
                    self.set_field_color(row, column, self.enabled_colors[0])
                    self.set_field_text_color(row, column, self.enabled_colors[1])
            else:
                self.set_field_color(row, column, self.disabled_colors[0])
                self.set_field_text_color(row, column, self.disabled_colors[1])

        self.changed_fields = []
                

    def set_field_not_editable(self, row: int, column: int):
        # Note: the .configure method is very slow, so we need to check if updating is necessary first
        #if self.sudoku_frame.get_field(row, column).cget("state") == "normal":     
            self.sudoku_frame.get_field(row, column).configure(state="disabled")
            self.set_field_color_not_editable(row, column)
            self.sudoku_frame.get_field(row, column).set_state(False)
        
    def set_field_editable(self, row: int, column: int):
        # Note: the .configure method is very slow, so we need to check if updating is necessary first
        #if self.sudoku_frame.get_field(row, column).cget("state") == "disabled":
            self.sudoku_frame.get_field(row, column).configure(state="normal")
            self.set_field_color_editable(row, column)
            self.sudoku_frame.get_field(row, column).set_state(True)


    def invalid_field(self, row: int, column: int):
        
        widget = self.sudoku_frame.get_field(row, column)
        entry_value = widget.get_value()
        
        if entry_value == '':
            widget.configure(text_color=self.enabled_colors[1])
            return
        else:
            entry_value = int(entry_value)
        
        would_value_be_valid = self.controller.model.would_value_be_valid(row, column, entry_value)
        
        if widget.get_state():       
            if not would_value_be_valid:
                widget.configure(text_color="red")
                self.changed_fields.append((row, column))
            else: 
                widget.configure(text_color=self.enabled_colors[1])
        
        else:
            if not would_value_be_valid:
                widget.configure(fg_color="#403823")
                self.changed_fields.append((row, column))
            else: 
                widget.configure(text_color=self.disabled_colors[1])


    def set_field_color(self, row: int, column: int, color: str):      
        self.sudoku_frame.get_field(row, column).configure(fg_color=color)

    def set_field_text_color(self, row: int, column: int, color: str):
        self.sudoku_frame.get_field(row, column).configure(text_color=color)
    

        
    def set_field_not_editable(self, row: int, column: int):
        # Note: the .configure method is very slow, so we need to check if updating is necessary first
        if self.sudoku_frame.get_field(row, column).cget("state") == "normal":     
            self.sudoku_frame.get_field(row, column).configure(state="disabled")
            
            self.set_field_color(row, column, self.disabled_colors[0])
            self.set_field_text_color(row, column, self.disabled_colors[1])
            
            self.sudoku_frame.get_field(row, column).set_state(False)
        
    def set_field_editable(self, row: int, column: int):
        # Note: the .configure method is very slow, so we need to check if updating is necessary first
        if self.sudoku_frame.get_field(row, column).cget("state") == "disabled":
            self.sudoku_frame.get_field(row, column).configure(state="normal")
            
            self.set_field_color(row, column, self.enabled_colors[0])
            self.set_field_text_color(row, column, self.enabled_colors[1])
            
            self.sudoku_frame.get_field(row, column).set_state(True)



    def set_field_value(self, row: int, column: int, value: int):
        
        if (value > 0 and value < 10):
            self.sudoku_frame.get_field(row, column).set_value(value)
            
        elif (value == 0):
            self.sudoku_frame.get_field(row, column).set_value("")


    def get_field_value(self, row: int, column: int) -> int:
        
        value = self.sudoku_frame.get_field(row, column).get_value()
        if value == "":
            return 0
        else:
            return int(value)


    def set_field_state(self, row: int, column: int, state: bool):
        if state:
            self.set_field_editable(row, column)
        else:
            self.set_field_not_editable(row, column)
            
            
    def get_field_state(self, row: int, column: int) -> bool:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field'''
        return self.sudoku_frame.get_field(row, column).get_state()


    def set_mode(self, mode = 'normal'):
        for checkbox in self.sudoku_checkbox_frame.checkboxes:
            if (mode == 'debug'):
                checkbox.select()
                self.debugcheckbox_callback(checkbox)
            else:
                checkbox.deselect()
                self.debugcheckbox_callback(checkbox)