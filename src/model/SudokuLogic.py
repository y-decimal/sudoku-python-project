from model.ISudokuInterface import ISudokuInterface
import random

class SudokuLogic(ISudokuInterface):
    '''Model for Sudoku fields'''
    block_index = [0,3,6,27,30,33, 54, 57, 60]
    block = {
    0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2,
    9: 0, 10: 0, 11: 0, 12: 1, 13: 1, 14: 1, 15: 2, 16: 2, 17: 2,
    18: 0, 19: 0, 20: 0, 21: 1, 22: 1, 23: 1, 24: 2, 25: 2, 26: 2,
    27: 3, 28: 3, 29: 3, 30: 4, 31: 4, 32: 4, 33: 5, 34: 5, 35: 5,
    36: 3, 37: 3, 38: 3, 39: 4, 40: 4, 41: 4, 42: 5, 43: 5, 44: 5,
    45: 3, 46: 3, 47: 3, 48: 4, 49: 4, 50: 4, 51: 5, 52: 5, 53: 5,
    54: 6, 55: 6, 56: 6, 57: 7, 58: 7, 59: 7, 60: 8, 61: 8, 62: 8,
    63: 6, 64: 6, 65: 6, 66: 7, 67: 7, 68: 7, 69: 8, 70: 8, 71: 8,
    72: 6, 73: 6, 74: 6, 75: 7, 76: 7, 77: 7, 78: 8, 79: 8, 80: 8
}
    
    
    def __init__(self):
        self.clear()


    def rc_to_index(self,row: int, column: int):
        return (row)* 9 + column

    def clear(self):
        self.fields = [0 for _ in range (81)]
        self.starterfield = [False for _ in range (81)]

    def new_sudoku(self, newSudoku: list):
        self.fields = [field for field in newSudoku]
        self.starterfield = [field != 0 for field in self.fields]
            

    def get_field_value(self, row: int, column: int) -> int:
        '''Returns the value of the field at the given row and column'''
        return self.fields[self.rc_to_index(row, column)]

    def set_field_value(self, row: int, column: int, value: int) -> bool:
        '''Returns true if value was set, returns false if value could not be set (e.g. because it is a field that is not editable)'''
        if not self.is_field_editable(row,column):
            return False
        
        else:
            self.fields[self.rc_to_index(row,column)] = value
            return True

    def is_field_editable(self, row: int, column: int) -> bool:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field)'''
        
        check1 = not self.starterfield[self.rc_to_index(row, column)]
        #print("Check1")
        #print(check1)
        return check1

    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''
        
        if not self.is_field_editable:
            return False
        possible_fields = [field for field in self.fields]
        possible_fields[self.rc_to_index(row,column)] = value
        check = self.invalid_rows2(possible_fields, row, column, value) == {} and self.invalid_column2(possible_fields, row, column, value) == {} and self.invalid_blocks2(possible_fields, row, column, value) == {}
        # if not check:
        #     print(f'{self.rc_to_index(row,column)}:{check}:{value}:{row, column}')
        return check


    def invalid_rows(self, sudoku):
        invalid= {}
        for r in range(9):
            space = []
            for c in range(9):
                if sudoku[r*9+c] not in space and sudoku[r*9+c] !=0:
                    space.append(sudoku[r*9+c]) 
                elif sudoku[r*9+c] != 0:
                    invalid.update({r+1:sudoku[r*9+c]})
        return invalid

    def invalid_column(self, sudoku):
        invalid= {}
        for c in range(9):
            space = []
            for r in range(9):
                if sudoku[r*9+c] not in space and sudoku[r*9+c] !=0:
                    space.append(sudoku[r*9+c]) 
                elif sudoku[r*9+c] != 0:
                    invalid.update({r+1:sudoku[r*9+c]})
        return invalid
    
    
    def invalid_blocks(self,sudoku):
        invalid= {}
        for b in self.block_index:
            space = []
            for r in range(3):
                for c in range(3):
                    if sudoku[b+r*9+c] not in space and sudoku[b+r*9+c] !=0:
                        space.append(sudoku[b + r*9 + c])
                    elif sudoku[b + r*9 + c] != 0:
                        invalid.update({self.block_index.index(b)+1:sudoku[b + r*9 + c]})
        return invalid


    
    def invalid_blocks2(self,sudoku,row,column,value):
        invalid= {}
        b = self.block_index[self.block[self.rc_to_index(row,column)]]
        for r in range(3):
            for c in range(3):
                if sudoku[b+r*9+c] ==  value and sudoku[b+r*9+c] !=0 and b+r*9+c != self.rc_to_index(row, column):
                    invalid.update({b + r*9 + c:sudoku[b + r*9 + c]})
        return invalid
    

    def invalid_rows2(self, sudoku, row, column, value):
        invalid= {}
        for c in range(9):
            if sudoku[row*9+c] ==  value and sudoku[row*9+c] !=0 and c != column:
                invalid.update({self.rc_to_index(row,c):sudoku[row*9+c]})
        return invalid

    def invalid_column2(self, sudoku,row, column, value):
        invalid= {}
        for r in range(9):
            if sudoku[r*9+column] ==  value and sudoku[r*9+column] !=0 and r != row:
                invalid.update({self.rc_to_index(r,column):sudoku[r*9+column]})
        return invalid





    def generate_random_sudoku(self, difficulty = 0.5):
        '''Sets random values for some fields in the game field'''   
        self.clear()
        for row in range (9):
            for column in range(9):
                
                self.fields[self.rc_to_index(row, column)] = 0
                self.starterfield[self.rc_to_index(row, column)] = False
                
                if (random.random() > difficulty):
                    
                    self.fields[self.rc_to_index(row, column)] = random.randint(1,9)
                    self.starterfield[self.rc_to_index(row, column)] = True


    def set_field_state(self, row: int, column: int, state: bool):
        '''Sets the state of a field. True means the field can be edited, False means the field is a given field'''
        self.starterfield[self.rc_to_index(row, column)] = not state
    