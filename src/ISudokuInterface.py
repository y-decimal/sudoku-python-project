from abc import ABC, abstractmethod


class ISudokuInterface(ABC):
    '''Interface for Sudoku fields'''


    @abstractmethod
    def __init__(self):
        pass



    @abstractmethod
    def get_field_value(self, row: int, column: int) -> int:
        '''Returns the value of the field at the given row and column'''
        return -1



    @abstractmethod
    def set_field_value(self, row: int, column: int, value: int) -> bool:
        '''Returns true if value was set, returns false if value could not be set (e.g. because it is a field that is not editable)'''
        return False



    @abstractmethod
    def is_field_editable(self, row: int, column: int) -> bool:
        '''Returns true if field is editable, returns false if field is not editable (e.g because it is a given field)'''
        return False



    @abstractmethod
    def would_value_be_valid(self, row: int, column: int, value) -> bool:
        '''Returns true if value would be valid in the field, returns false if value would not be valid (e.g. because it is already in the row, column or block)'''
        return False

# Hi