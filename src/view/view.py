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

    def __init__(self, parent):
        
        super().__init__(parent)
       
        self.mouse_position = None
       
        # App Grid Configuration (3x3 Grid)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure((1,2), weight=1)




        # Frame Grid Configuration
        
        # Sudoku Frame
        self.sudoku_frame = SudokuFrame(self, 9)
        self.sudoku_frame.grid(row=0, column=1, padx=10) 
        
        
        for row in range(9):
            for column in range(9):
                self.sudoku_frame.get_field(row, column).bind("<Enter> ", lambda args, widget = self.sudoku_frame.get_field(row, column): self.set_mouse_position(widget))
                self.sudoku_frame.get_field(row, column).bind("<Leave>", lambda args: self.set_mouse_position(None), add="+")
                self.sudoku_frame.get_field(row, column).bind("<Button-1>", lambda args: self.mousebutton_callback(), add="+")
                

        self.bind("<Button-1>", lambda args: self.mousebutton_callback())

        # Button Frame
        self.sudoku_button_frame = ButtonFrame.ButtonFrame(self, 1, 5)

        self.sudoku_button_frame.buttons[0].configure(text="Fetch", command = self.fetchbutton_callback)
        self.sudoku_button_frame.buttons[1].configure(text="Push", command = self.pushbutton_callback)
        self.sudoku_button_frame.buttons[2].configure(text="Generate", command = self.generatebutton_callback)
        self.sudoku_button_frame.buttons[3].configure(text="Save", command = self.savebutton_callback)
        self.sudoku_button_frame.buttons[4].configure(text="Load", command = self.loadbutton_callback)
        

        self.sudoku_button_frame.grid(row=3, column=1, padx=10, pady=10, sticky="s")



    	# Checkbox Frame
        self.sudoku_checkbox_frame = CheckboxFrame.CheckboxFrame(self, 1, 1)
        self.sudoku_checkbox_frame.checkboxes[0].configure(text="Debug", command = self.debugcheckbox_callback)
        self.sudoku_checkbox_frame.checkboxes[0].select()   


        self.sudoku_checkbox_frame.grid(row=2, column=1, padx=10, pady=10)


    def set_controller(self, controller):
        '''Sets the controller of the view'''
        self.controller = controller

        self.bind_class("Entry","<KeyPress>", lambda *args: self.controller.push(), add="+")


    def set_mouse_position (self, widget):
        self.mouse_position = widget
        # print(f"Mouse position set to: {self.mouse_position}")

    def mousebutton_callback(self):
        # print(self.mouse_position)
        if self.mouse_position != None:
            self.reset_fields()
            # print(f"Mouse clicked at position: {self.mouse_position.position}")
            # print(self.mouse_position.position)
            row = self.mouse_position.position[0]
            column = self.mouse_position.position[1]
            self.highlight_fields(self.mouse_position)
        else:
            self.reset_fields()


    def fetchbutton_callback(self):
        if self.controller: self.controller.fetch()
        
    def pushbutton_callback(self):
        if self.controller: self.controller.push()
       
    def generatebutton_callback(self):
        if self.controller: self.controller.generate()

    def savebutton_callback(self):
        if self.controller: self.controller.save()
        
    def loadbutton_callback(self):
        if self.controller: self.controller.load()
    
    def debugcheckbox_callback(self):
        if self.controller: 
            if self.sudoku_checkbox_frame.checkboxes[0].get():
                self.controller.set_mode("debug")
            else:
                self.controller.set_mode("normal")

    def highlight_fields(self, widget):

        row, column = widget.get_field_position()        
        self.changed_fields.append((row, column))
        
        self.highlight_cell(widget)

        if widget.state:
            widget.configure(fg_color=self.highlight_color[0])
            widget.focus()
        else:
            widget.configure(fg_color=self.highlight_color[1])
            widget.focus()
        
        for i in range(9):
            if i != column:
                self.changed_fields.append((row, i))
                if self.sudoku_frame.get_field(row, i).state:
                    self.sudoku_frame.get_field(row, i).configure(fg_color=self.adjacent_color[0])
                else:
                    self.sudoku_frame.get_field(row, i).configure(fg_color=self.adjacent_color[1])

            if i != row:
                self.changed_fields.append((i, column))
                if self.sudoku_frame.get_field(i, column).state:
                    self.sudoku_frame.get_field(i, column).configure(fg_color=self.adjacent_color[0])
                else:
                    self.sudoku_frame.get_field(i, column).configure(fg_color=self.adjacent_color[1])
                    
        
                
    def highlight_cell(self, widget):
         
         row, column = widget.get_field_position() 

         row_offset = row//3*3
         column_offset = column//3*3    

         for cell_row in range(3):
             
             cell_row_offset = cell_row + row_offset

             for cell_column in range(3):

                cell_column_offset = cell_column + column_offset

                if row != cell_row_offset and column != cell_column_offset:
                    self.changed_fields.append((cell_row_offset, cell_column_offset))

                    if self.sudoku_frame.get_field(cell_row_offset, cell_column_offset).state:
                        self.sudoku_frame.get_field(cell_row_offset, cell_column_offset).configure(fg_color=self.cell_color[0])
                        
                    else:
                        self.sudoku_frame.get_field(cell_row_offset, cell_column_offset).configure(fg_color=self.cell_color[1])        
    
    def reset_fields(self):

        for row, column in self.changed_fields:
        
            if self.sudoku_frame.get_field(row, column).state:
                self.set_field_color_editable(row, column)
            else:
                self.set_field_color_not_editable(row, column)

        self.changed_fields = []
                

    def set_field_color_not_editable(self, row: int, column: int):
        self.sudoku_frame.get_field(row, column).configure(fg_color=self.disabled_color[0])
        self.sudoku_frame.get_field(row, column).configure(text_color=self.disabled_color[1])
    
    def set_field_color_editable(self, row: int, column: int):
        self.sudoku_frame.get_field(row, column).configure(fg_color=self.enabled_color[0])
        self.sudoku_frame.get_field(row, column).configure(text_color=self.enabled_color[1])
        
    def set_field_not_editable(self, row: int, column: int):
        # Note: the .configure method is very slow, so we need to check if updating is necessary first
        if self.sudoku_frame.get_field(row, column).cget("state") == "normal":     
            self.sudoku_frame.get_field(row, column).configure(state="disabled")
            self.set_field_color_not_editable(row, column)
            self.sudoku_frame.get_field(row, column).state = False
        
    def set_field_editable(self, row: int, column: int):
        # Note: the .configure method is very slow, so we need to check if updating is necessary first
        if self.sudoku_frame.get_field(row, column).cget("state") == "disabled":
            self.sudoku_frame.get_field(row, column).configure(state="normal")
            self.set_field_color_editable(row, column)
            self.sudoku_frame.get_field(row, column).state = True



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


    def set_mode(self, mode = 'normal'):
        for checkbox in self.sudoku_checkbox_frame.checkboxes:
            if (mode == 'debug'):
                checkbox.select()
                self.debugcheckbox_callback()
            else:
                checkbox.deselect()
                self.debugcheckbox_callback()