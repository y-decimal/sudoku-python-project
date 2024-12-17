import tkinter as tk
import customtkinter as ctk

from view.customframes.SudokugridFrame import SudokuFrame
from view.customframes import ButtonFrame, CheckboxFrame



class View(ctk.CTkFrame):


    

    disabled_color = ("#2F2F32", "#86ff7b") # (Background color, Text color)
    enabled_color = ("#343638", "#DDDDDD")  # (Background color, Text color)
    highlight_color = ("#5F4648", "#3F2628") # (Enabled color, disabled color)
    adjacent_color = ("#445F48", "#243F28") # (Enabled color, disabled color)
    cell_color = adjacent_color # (Enabled color, disabled color)
    
    changed_fields = []
    edit_mode = False

    def __init__(self, parent):
        
        super().__init__(parent)
       
        self.widget_at_mouse = None
       
        # App Grid Configuration (3x3 Grid)
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure((1,2), weight=1)




        # Frame Grid Configuration
        
        # Sudoku Frame
        self.sudoku_frame = SudokuFrame(self, 9)
        self.sudoku_frame.grid(row=0, column=1, padx=10, pady=10) 
        
        
        for row in range(9):
            for column in range(9):
                self.sudoku_frame.get_field(row, column).bind("<Enter> ", lambda args, widget = self.sudoku_frame.get_field(row, column): self.set_mouse_position(widget))
                self.sudoku_frame.get_field(row, column).bind("<Leave>", lambda args: self.set_mouse_position(None), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-1>", lambda args: self.mousebutton_callback(), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-3>", lambda args: self.toggle_field(), add="+")
                

        self.bind("<Button-1>", lambda args: self.mousebutton_callback())



        self.tool_frame = ctk.CTkFrame(self)
        
        # Button Frame
        self.sudoku_button_frame = ButtonFrame.ButtonFrame(self.tool_frame, 1, 3)

        self.sudoku_button_frame.buttons[0].configure(text="Generate", command = self.generatebutton_callback)
        self.sudoku_button_frame.buttons[1].configure(text="Save", command = self.savebutton_callback)
        self.sudoku_button_frame.buttons[2].configure(text="Load", command = self.loadbutton_callback)
        
        self.sudoku_button_frame.grid(row=1, column=0, columnspan = 2, padx=10, pady=10, sticky="nsew")
         
        # File name entry        
        self.file_entry = ctk.CTkEntry(self.tool_frame, width=200, placeholder_text="Enter filename", font=("Arial", 18))
        self.file_entry.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    	# Checkbox Frame
        self.sudoku_checkbox_frame = CheckboxFrame.CheckboxFrame(self.tool_frame, 1, 2)
        self.sudoku_checkbox_frame.checkboxes[0].configure(text="Save Locally", command = self.debugcheckbox_callback)
        self.sudoku_checkbox_frame.checkboxes[0].select()   
        self.sudoku_checkbox_frame.checkboxes[1].configure(text="Edit Mode", command =  self.set_edit_mode)
        
        self.sudoku_checkbox_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        
        self.tool_frame.grid_columnconfigure((0,1), weight=1)
        # self.tool_frame.grid_rowconfigure((1,2), weight=0)
        # self.tool_frame.grid_rowconfigure((0,3), weight=2)

        self.tool_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ew")



    def set_controller(self, controller):
        '''Sets the controller of the view'''
        self.controller = controller

        self.bind_class("Entry","<Button-1>", lambda *args: self.controller.push(), add="+")


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


    def fetchbutton_callback(self):
        if self.controller: self.controller.fetch()
        
    def pushbutton_callback(self):
        if self.controller: self.controller.push()
       
    def generatebutton_callback(self):
        if self.controller: self.controller.generate()

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
            self.reset_fields()
            if file_name != "":
                self.controller.load(file_name)
            else:
                self.controller.load("test")
            
    
    def debugcheckbox_callback(self):
        if self.controller: 
            if self.sudoku_checkbox_frame.checkboxes[0].get():
                self.controller.set_mode("debug")
            else:
                self.controller.set_mode("normal")


    def toggle_field(self):
        
        if self.widget_at_mouse != None and self.edit_mode == 1:
            
            
            
            row, column = self.widget_at_mouse.get_position()
            
            # print(f"Toggling field at row: {row}, column: {column}")
            
            if self.widget_at_mouse.get_state():
                self.set_field_not_editable(row, column)
                # print(f"Field at row: {row}, column: {column} is now not editable")
            else:
                self.set_field_editable(row, column)
                # print(f"Field at row: {row}, column: {column} is now editable")
                
            self.reset_fields()
            #self.highlight_fields(self.widget_at_mouse)


    def highlight_fields(self, widget):

        row, column = widget.get_position()        
        self.changed_fields.append((row, column))
        
        self.highlight_cell(widget)

        if widget.get_state():
            widget.configure(fg_color=self.highlight_color[0])
            widget.focus()
        else:
            widget.configure(fg_color=self.highlight_color[1])
            widget.focus()
        
        for i in range(9):
            if i != column:
                self.changed_fields.append((row, i))
                if self.sudoku_frame.get_field(row, i).get_state():
                    self.sudoku_frame.get_field(row, i).configure(fg_color=self.adjacent_color[0])
                else:
                    self.sudoku_frame.get_field(row, i).configure(fg_color=self.adjacent_color[1])

            if i != row:
                self.changed_fields.append((i, column))
                if self.sudoku_frame.get_field(i, column).get_state():
                    self.sudoku_frame.get_field(i, column).configure(fg_color=self.adjacent_color[0])
                else:
                    self.sudoku_frame.get_field(i, column).configure(fg_color=self.adjacent_color[1])
                    
        
                
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
                        self.sudoku_frame.get_field(cell_row_offset, cell_column_offset).configure(fg_color=self.cell_color[0])
                        
                    else:
                        self.sudoku_frame.get_field(cell_row_offset, cell_column_offset).configure(fg_color=self.cell_color[1])        
    
    def reset_fields(self):

        for row, column in self.changed_fields:
        
            if self.sudoku_frame.get_field(row, column).get_state():
                self.set_field_color_editable(row, column)
            else:
                self.set_field_color_not_editable(row, column)

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


    def set_field_color_not_editable(self, row: int, column: int):
        self.sudoku_frame.get_field(row, column).configure(fg_color=self.disabled_color[0])
        self.sudoku_frame.get_field(row, column).configure(text_color=self.disabled_color[1])
    
    def set_field_color_editable(self, row: int, column: int):
        self.sudoku_frame.get_field(row, column).configure(fg_color=self.enabled_color[0])
        self.sudoku_frame.get_field(row, column).configure(text_color=self.enabled_color[1])
        


    def set_field_value(self, row: int, column: int, value: int):
        
        if (value > 0 and value < 10):
            self.sudoku_frame.get_field(row, column).entry_variable.set(str(value))
            
        elif (value == 0):
            self.sudoku_frame.get_field(row, column).entry_variable.set("")


    def get_field_value(self, row: int, column: int) -> int:
        
        value = self.sudoku_frame.get_field(row, column).entry_variable.get()
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
        return self.sudoku_frame.get_field(row, column).get_state()


    def set_mode(self, mode = 'normal'):
        for checkbox in self.sudoku_checkbox_frame.checkboxes:
            if (mode == 'debug'):
                checkbox.select()
                self.debugcheckbox_callback()
            else:
                checkbox.deselect()
                self.debugcheckbox_callback()