from model.ISudokuInterface import ISudokuInterface

class Model(ISudokuInterface):
    '''Model for Sudoku fields'''

    def __init__(self, givenfield: list):
        self.block_index = [0,3,6,27,30,33, 54, 57, 60]
        self.fields = {}
        for field in givenfield:
            if isinstance(field, int) and 0 <= field <= 9:
                self.fields.append(field)#transferring the initial field values as a list, empty fields contain the value 0
            elif field == "" or field == None:
                self.fields.append(0)
            else:
                raise ValueError(f"Invalid Value at position {givenfield.index(field)}")
        self.starterfield = []
        for field in self.fields:
            self.starterfield.append(field != 0) #mirroring the information, whether the field was given from the start. True if Starterfield, false if empty (0) at start

    def rc_to_index(self,row: int, column: int):
        return (row-1)* 9 + column - 1



    def get_field_value(self, row: int, column: int) -> int:
        '''Returns the value of the field at the given row and column'''
        return self.fields[self.rc_to_index(row, column)]




    def set_field_value(self, row: int, column: int, value: int) -> bool:
        '''Returns true if value was set, returns false if value could not be set (e.g. because it is a field that is not editable)'''
        if self.entry_status(row, column, value) == 2:
            return False
        elif self.entry_status(row, column, value) == 0:
            self.fields[self.rc_to_index(row,column)] = 0
            return True
        elif self.entry_status(row, column, value) == 1:
            self.fields[self.rc_to_index(row,column)] = value
            return True

            

    def entry_status(self, row: int, column: int, value: int) -> bool:
        '''Returns 0 if value is empty (0), 1 if value is number, 2 if value is invalid'''
        if not self.is_field_editable(row,column):
            return 2
        elif value == "":
            return 0
        elif not isinstance(value, int):
            return 2
        elif value < 1 or value > 9:
            return 2
        else: 
            return 1


    def is_field_editable(self, row: int, column: int) -> bool:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field)'''
        return not self.starterfield[self.rc_to_index(row, column)]




    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''
        if self.entry_status(row, column, value) == 2:
            return False
        possible_fields = [field for field in self.fields]
        possible_fields[self.rc_to_index(row,column)] = value
        return self.invalid_rows(possible_fields) == {} and self.invalid_column(possible_fields) == {} and self.invalid_blocks(possible_fields) == {}


    def invalid_rows(self, sudoku):
        invalid= {}
        for r in range(9):
            space = []
            for c in range(9):
                if sudoku[r*9+c] not in space:
                    space.append(sudoku[r*9+c]) 
                else:
                    invalid.update({r+1:sudoku[r*9+c]})
        return invalid

    def invalid_column(self, sudoku):
        invalid= {}
        for c in range(9):
            space = []
            for r in range(9):
                if sudoku[r*9+c] not in space:
                    space.append(sudoku[r*9+c]) 
                else:
                    invalid.update({r+1:sudoku[r*9+c]})
        return invalid
    
    
    def invalid_blocks(self,sudoku):
        invalid= {}
        for b in self.block_index:
            space = []
            for r in range(3):
                for c in range(3):
                    if sudoku[b+r*9+c] not in space:
                        space.append(sudoku[b + r*9 + c])
                    else:
                        invalid.update({self.block_index.index(b)+1:sudoku[b + r*9 + c]})
        return invalid
# Hi