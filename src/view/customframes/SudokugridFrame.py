import customtkinter as ctk
from threading import Thread


class SudokuFrame(ctk.CTkFrame):

    game_field = [[0 for _ in range(9)] for _ in range(9)]
    scale = 1.0
    window_size = 200

    def __init__(self, master, game_gridsize):
        
        super().__init__(master)
        
        self.game_gridsize = game_gridsize
        self.gridsize = self.game_gridsize+(self.game_gridsize-1)
        
        self.configure_grid()
        self.initialize_fields()  # ideally should be dynamically scaled
        

        self.add_horizontal_separators()
        self.add_vertical_separators()


           
    def set_scale(self, scale):
        self.scale = scale
        
    def set_window_size(self, window_size):
        self.window_size = window_size

    def get_field(self, row, column):
        return self.game_field[row][column]


    def configure_grid(self):
        self.grid_columnconfigure([i for i in range(self.gridsize)], weight=1)
        self.grid_rowconfigure([i for i in range(self.gridsize)], weight=1)


    def initialize_fields(self):
    
        self.game_entry_dimension = int(self.window_size // self.game_gridsize * 0.75)

        self.sudoku_row = 0
        for row in range(self.gridsize):        
            if row % 2 == 0:
                self.sudoku_column = 0
                for column in range(self.gridsize):
                    if column % 2 == 0:
                        self.game_field[self.sudoku_row][self.sudoku_column] = SudokuEntryField(self, self.game_entry_dimension, (self.sudoku_row, self.sudoku_column))
                        self.game_field[self.sudoku_row][self.sudoku_column].grid(row=row, column=column, padx=2, pady=2)
                        self.sudoku_column += 1
                self.sudoku_row += 1

        self.update_entries()    


    def add_horizontal_separators(self):
        for row in range(self.gridsize):
            if row % 2 != 0 and (row + 1) % 3 == 0:
                ctk.CTkFrame(self, height=4, fg_color="#505070", corner_radius=2).grid(row=row, column=0, columnspan=self.gridsize, sticky="ew", pady=3)


    def add_vertical_separators(self):
        for col in range(self.gridsize):
            if col % 2 != 0 and (col + 1) % 3 == 0:
                ctk.CTkFrame(self, width=4, fg_color="#505070", corner_radius=2).grid(row=0, column=col, rowspan=self.gridsize, sticky="ns", padx=3)
               
                
    def update_entries(self):
           
        self.game_entry_dimension = int((self.window_size // self.game_gridsize) * 0.75 * self.scale)
        for row in range(9):
            for column in range(9):
                self.get_field(row, column).update_size(self.game_entry_dimension)        







class SudokuEntryField(ctk.CTkEntry):

    def __init__(self, master, entry_dimensions, position):      

        self.entry_variable = ctk.StringVar()       

        super().__init__(master, 
                         width= entry_dimensions, 
                         height = entry_dimensions, 
                         font = ("Arial", 0.75*entry_dimensions), 
                         textvariable=self.entry_variable, 
                         justify="center",
                         insertontime=0
                        )

        self.state = True
        self.invalid_state = False
        self.position = position
        


    def get_position(self):
        return self.position
    
    def get_row(self):
        return self.position[0]
    
    def get_column(self):
        return self.position[1]
    
    def get_state(self):
        return self.state

    def get_invalid_state(self):
        return self.invalid_state
        
    def get_value(self):
        return self.entry_variable.get()      
                
    def set_state(self, state: bool):
        self.state = state

    def set_invalid_state(self, invalid_state: bool):
        self.invalid_state = invalid_state

    def set_value(self, value):
        self.entry_variable.set(str(value))
        
    def update_size(self, entry_dimensions):
        self.configure(width=entry_dimensions, height=entry_dimensions)
        self.configure(font = ("Arial", 0.75*entry_dimensions))