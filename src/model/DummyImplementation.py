from model.ISudokuInterface import ISudokuInterface
import random

class DummyImplementation(ISudokuInterface):
    '''Dummy implementation of the ISudokuInterface to use for testing'''

    game_field = []

    def __init__(self):
        '''Initializes the DummyImplementation'''

        # Initialize the game field with 0s for the value and True for the editable flag
        self.game_field = [[(0, True) for _ in range(9)] for _ in range(9)] 

        # Set some fields to random values
        for row in range (9):
            for column in range(9):
                if (random.randint(1,9) < 3):
                    self.game_field[row][column] = (random.randint(1,9), False)
        
    

    def get_field_value(self, row: int, column: int) -> int:
        '''Returns the value of the field at the given row and column'''

        # Return -1 if the row or column is out of bounds
        if (row < 0 or row > 8 or column < 0 or column > 8):
            print(f"Row {row} or column {column} out of bounds")
            return -1
        
        # Return the value of the field by accessing the first element of the tuple
        return self.game_field[row][column][0]
    


    def set_field_value(self, row: int, column: int, value: int) -> bool:
        '''Returns true if value was set, returns false if value could not be set (e.g. because it is a field that is not editable)'''

        # Abort if the row or column is out of bounds
        if (row < 0 or row > 8 or column < 0 or column > 8):
            print(f"Row {row} or column {column} out of bounds")
            return False
        
        # Abort if the field is not editable
        if (not self.game_field[row][column][1]):
            print(f"Field at row {row} and column {column} is not editable")
            return False
        
        # Set the value of the field by overwriting the first element of the tuple
        self.game_field[row][column][0] = value
        return True
    

    def is_field_editable(self, row: int, column: int) -> bool:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field)'''

        # Abort if the row or column is out of bounds
        if (row < 0 or row > 8 or column < 0 or column > 8):
            print(f"Row {row} or column {column} out of bounds")
            return False
        
        # Return the editable flag by accessing the second element of the tuple
        return self.game_field[row][column][1]
    


    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''

        # Abort if the row or column is out of bounds
        if (row < 0 or row > 8 or column < 0 or column > 8):
            print(f"Row {row} or column {column} out of bounds")
            return False

        # Actual check not Implemented
        return True