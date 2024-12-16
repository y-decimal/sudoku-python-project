from model.IModelInterface import IModelInterface
from model.FileManager import FileManager
from model.SudokuLogic import SudokuLogic


class Model(IModelInterface):

    sudoku_logic = None
    file_manager = None

    def __init__(self):

        self.file_manager = FileManager()
        self.sudoku_logic = SudokuLogic()




    def get_field_value(self, row: int, column: int) -> int:
        '''Returns the value of the field at the given row and column'''

        return self.sudoku_logic.get_field_value(row, column)


    def set_field_value(self, row: int, column: int, value: int) -> bool:
        '''Returns true if value was set, returns false if value could not be set (e.g. because it is a field that is not editable)'''

        return self.sudoku_logic.set_field_value(row, column, value)
    

    def is_field_editable(self, row: int, column: int) -> bool:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field)'''

        return self.sudoku_logic.is_field_editable(row, column)
    

    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''

        return self.sudoku_logic.would_value_be_valid(row, column, value)
    

    def generate_random_sudoku(self):
        '''Generates a random sudoku'''

        self.sudoku_logic.generate_random_sudoku()


    def load_sudoku(self, file_name: str) -> bool:
        '''Loads a sudoku from a file using the given filename. Returns true if the sudoku was loaded successfully, returns false if the sudoku could not be loaded'''

        sudoku = self.file_manager.load_sudoku(file_name) 

        for row in range(9):
            for column in range(9):
                    
                    self.sudoku_logic.set_field_editable(row, column, True)
                    self.sudoku_logic.set_field_value(row, column, sudoku[row][column][0])
                    self.sudoku_logic.set_field_editable(row, column, sudoku[row][column][1])

    

    def save_sudoku(self, file_name: str) -> bool:
        '''Saves a sudoku to a file using the given filename. Returns true if the sudoku was saved successfully, returns false if the sudoku could not be saved'''

        sudoku = [[(self.sudoku_logic.get_field_value(row, column), self.sudoku_logic.is_field_editable(row, column)) for column in range(9)] for row in range(9)]

        return self.file_manager.save_sudoku(sudoku, file_name)
    

    def set_mode(self, mode = 'normal'):
        '''Sets the debug mode'''

        self.file_manager.set_file_mode(mode)

    


    def would_value_be_valid(self, row: int, col: int, value: int) -> bool:
        '''Checks if the value at the given row and column is unique in its row, column, and grid'''

        if value == 0:
            return True

        current_grid = (row // 3) * 3 + col // 3
        value = self.sudoku_logic.get_field_value(row, col)

        for i in range(9):
            if col != i and value == self.sudoku_logic.get_field_value(row, i):
                return False
            if row != i and value == self.sudoku_logic.get_field_value(i, col):
                return False
            if ((row % 3) * 3 + col % 3) != i and value == self.value_at_grid_pos(current_grid, i):
                return False

        return True
    

    def value_at_grid_pos(self, grid, i):
        
        row = grid // 3 * 3 + i // 3
        col = grid % 3 * 3 + i % 3
        return self.sudoku_logic.get_field_value(row, col)
        
