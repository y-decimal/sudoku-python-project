from model.ISudokuInterface import ISudokuInterface
import random

class SudokuLogic(ISudokuInterface):
    '''Model for Sudoku fields'''
    
    def __init__(self, givenfield: list = [0 for _ in range (81)]):
        self.block_index = [0,3,6,27,30,33, 54, 57, 60]
        self.fields = []
        for field in givenfield:
            self.fields.append(field)#transferring the initial field values as a list, empty fields contain the value 0
        self.starterfield = []
        for field in self.fields:
            self.starterfield.append(field != 0) #mirroring the information, whether the field was given from the start. True if Starterfield, false if empty (0) at start

    def rc_to_index(self,row: int, column: int):
        return (row)* 9 + column

    def clear(self, clearstarter = False):
        self.fields = [0 for _ in range (81)]
        if clearstarter:
            self.starterfield = [False for _ in range (81)]

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

    def set_field_editable(self, row: int, column: int, editable: bool):
        '''Sets the field to editable or not editable'''
        
        self.starterfield[self.rc_to_index(row, column)] = not editable

    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''
        
        if not self.is_field_editable:
            return False
        possible_fields = [field for field in self.fields]
        possible_fields[self.rc_to_index(row,column)] = value
        check = self.invalid_rows(possible_fields) == {} and self.invalid_column(possible_fields) == {} and self.invalid_blocks(possible_fields) == {}
        print(f'{self.rc_to_index(row,column)}:{check}:{value}')
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


    def generate_random_sudoku(self):
        '''Sets random values for some fields in the game field'''   
        self.clear(True)
        for row in range (9):
            for column in range(9):
                
                self.fields[self.rc_to_index(row, column)] = 0
                self.starterfield[self.rc_to_index(row, column)] = False
                
                if (random.randint(1,9) < 3):
                    
                    self.fields[self.rc_to_index(row, column)] = random.randint(1,9)
                    self.starterfield[self.rc_to_index(row, column)] = True



# Test 2, test2