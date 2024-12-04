from abc import ABC, abstractmethod


class ISudokuInterface(ABC):
    '''Interface for Sudoku fields'''


    @abstractmethod
    def __init__(self, givenfield: list):
        self.block_index = [0,3,6,27,30,33, 54, 57, 60] #indices for upper left fields for each box, necessary for block_check
        self.fields = []
        for field in givenfield:
            if isinstance(field, int) and 0 <= field <= 9:
                self.fields.append(field)#transferring the initial field values as a list, empty fields contain the value 0
            elif field == "" or field == None:
                self.fields.append(0) # for connectivity purposes, depending on the format of the values given by the interface
            else:
                raise ValueError(f"Invalid Value at position {givenfield.index(field)}")
        self.starterfield = []
        for field in self.fields:
            self.starterfield.append(field != 0) #mirroring the information, whether the field was given from the start. True if given Starterfield, false if empty (0) at start

    def rc_to_index(self,row: int, column: int):
        return (row-1)* 9 + column - 1

    @abstractmethod
    def get_field_value(self, row: int, column: int) -> int:
        '''Returns the value of the field at the given row and column'''
        return self.fields[self.rc_to_index(row, column)]

    @abstractmethod
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
        elif value == "" or value == None or value == 0:# allows flexible handling of entries of different types. May be removed if stricter defined in UI
            return 0
        elif not isinstance(value, int):
            return 2
        elif value < 1 or value > 9:
            return 2
        else: 
            return 1

    @abstractmethod
    def is_field_editable(self, row: int, column: int) -> bool:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field)'''
        return not self.starterfield[self.rc_to_index(row, column)]



    @abstractmethod
    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''
        if self.entry_status(row, column, value) == 2:
            return False
        possible_fields = [field for field in self.fields]
        possible_fields[self.rc_to_index(row,column)] = value
        return self.invalid_rows(possible_fields) == {} and self.invalid_columns(possible_fields) == {} and self.invalid_blocks(possible_fields) == {}


    def invalid_rows(self, sudoku: list) -> dict: # returns a dict with double numbers for each row
        invalid= {}
        for r in range(9):
            space = []
            for c in range(9):
                if sudoku[r*9+c] not in space:
                    space.append(sudoku[r*9+c]) 
                else:
                    invalid.update({r+1:sudoku[r*9+c]})
        return invalid

    def invalid_columns(self, sudoku) -> dict: # returns a dict with double numbers for each column
        invalid= {}
        for c in range(9):
            space = []
            for r in range(9):
                if sudoku[r*9+c] not in space:
                    space.append(sudoku[r*9+c]) 
                else:
                    invalid.update({r+1:sudoku[r*9+c]})
        return invalid
    
    def invalid_blocks(self,sudoku) -> dict: # returns a dict with double numbers for each block
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