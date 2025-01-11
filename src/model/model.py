
from model.FileManager import FileManager
from model.SudokuLogic import SudokuLogic


class Model:

    sudoku_logic = None
    file_manager = None
    difficulty = None

    def __init__(self):

        self.file_manager = FileManager()
        self.sudoku_logic = SudokuLogic()
        self.difficulty = 0.5




    def get_field_value(self, row: int, column: int) -> int:
        '''Returns the value of the field at the given row and column'''

        return self.sudoku_logic.get_field_value(row, column)


    def set_field_value(self, row: int, column: int, value: int) -> bool:
        '''Returns true if value was set, returns false if value could not be set (e.g. because it is a field that is not editable)'''

        return self.sudoku_logic.set_field_value(row, column, value)
    

    def get_field_state(self, row: int, column: int) -> str:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field)'''
        return self.sudoku_logic.is_field_editable(row, column)
        
    def get_invalid_fields(self) -> list:
        '''Returns a list of tuples with the row and column of the invalid fields'''

        return [(row, column) for row in range(9) for column in range(9) if self.sudoku_logic.would_value_be_valid(row, column, self.sudoku_logic.get_field_value(row, column)) == False]
        # return self.sudoku_logic.get_invalid_fields()
        
    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''

        return self.sudoku_logic.would_value_be_valid(row, column, value)
    
    
    def set_field_state(self, row: int, column: int, state: bool):
        '''Sets the state of the field at the given row and column. True means the field is editable, False means the field is not editable'''

        self.sudoku_logic.set_field_state(row, column, state)
    

    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''

        return self.sudoku_logic.would_value_be_valid(row, column, value)
    

    def generate_random_sudoku(self):
        '''Generates a random sudoku with the current difficulty'''
        
        self.sudoku_logic.generate_random_sudoku(self.difficulty)
        
        
    def clear_sudoku(self):
        '''Clears the sudoku'''

        self.sudoku_logic.clear()


    def load_sudoku(self, file_name: str) -> bool:
        '''Loads a sudoku from a file using the given filename. Returns true if the sudoku was loaded successfully, returns false if the sudoku could not be loaded'''

        sudoku = self.file_manager.load_sudoku(file_name) 

        if sudoku == None:
            return False
    
        for row in range(9):
            for column in range(9):
                    
                    self.sudoku_logic.set_field_state(row, column, True)
                    self.sudoku_logic.set_field_value(row, column, sudoku[row][column][0])
                    self.sudoku_logic.set_field_state(row, column, sudoku[row][column][1])

        return True
    

    def save_sudoku(self, file_name: str) -> bool:
        '''Saves a sudoku to a file using the given filename. Returns true if the sudoku was saved successfully, returns false if the sudoku could not be saved'''

        sudoku = [[(self.sudoku_logic.get_field_value(row, column), self.sudoku_logic.is_field_editable(row, column)) for column in range(9)] for row in range(9)]

        return self.file_manager.save_sudoku(sudoku, file_name)
    

    def set_mode(self, mode = 'normal'):
        '''Sets the debug mode'''

        self.file_manager.set_file_mode(mode)


    def get_files(self):
        return self.file_manager.get_files()
    
    def is_file_writeable(self, file_name):
        return self.file_manager.is_writeable(file_name)