from abc import ABC, abstractmethod

class IModelInterface(ABC):


    @abstractmethod
    def load_sudoku(self, file_name: str) -> bool:
        '''Loads a sudoku from a file using the given filename. Returns true if the sudoku was loaded successfully, returns false if the sudoku could not be loaded'''
        pass
    
    
    
    @abstractmethod
    def save_sudoku(self, file_name: str) -> bool:
        '''Saves a sudoku to a file using the given filename. Returns true if the sudoku was saved successfully, returns false if the sudoku could not be saved'''
        pass