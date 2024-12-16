from pathlib import Path
import os


class FileManager:
    '''Dummy File Manager to use for testing or reference'''
    
    sudoku_testfiles_path = "/assets/TestFiles/"
    sudoku_files_path = "/assets/SudokuFiles/"
    root_dir = None
    
    def __init__(self):
        '''Initializes the FileManager with a path relative to the root directory'''
        
        # Get the root directory of the project
        self.root_dir = str(Path(__file__).parent.parent.parent)

        # Set the absolute path using the root directory and the relative path
        self.set_file_mode('normal')


    def save(self, content, file_name):
        '''Saves content to the file without formatting'''
        
        path = self.absolute_path + file_name
        with open(path, 'w') as file:
            file.write(content)
            
    
    def load(self, file_name):
        '''Loads content from the file without formatting'''
        
        path = self.absolute_path + file_name
        with open(path, 'r') as file:
            return file.read()
        
        
    def save_sudoku(self, sudoku: list, file_name):
        '''Saves a sudoku to the file in format "(Value, Writeable) /n"'''
        
        path = self.absolute_path + file_name
        
        if not os.path.exists(path):
            os.makedirs(newpath)
            
        try:
            with open(path, 'w') as file:
                
                for row in range(9):
                    for column in range(9):
                        file.write(str(sudoku[row][column]))
                        file.write("\n")
            return True
        
        except Exception as e: 
            print(e)
            return False        


    def load_sudoku(self, file_name):
        '''Loads a sudoku from the file in format "(Value, Writeable) /n", returns a 9x9 list of tuples'''
        
        path = self.absolute_path + file_name
        with open(path, 'r') as file:
            
            sudoku = [[(0, True) for _ in range(9)] for _ in range(9)]
            
            for row in range(9):
                
                for column in range(9):
                    
                    line = file.readline()
                    value = int(line[1])
                    writeable_flag = None
                    
                    if line[4] == 'T':
                        writeable_flag = True
                    elif line[4] == 'F':
                        writeable_flag = False
                                           
                    sudoku[row][column] = (value, writeable_flag)
            
            return sudoku
        

    
    def set_file_path(self, path):
        '''Sets the path to the file'''
        
        self.absolute_path = self.root_dir + path

        return True
    

    def set_file_mode(self, mode):
        '''Sets the mode to the file'''
        
        if mode == 'debug':
            self.absolute_path = self.root_dir + self.sudoku_testfiles_path
        elif mode == 'normal':
            self.absolute_path = self.root_dir + self.sudoku_files_path

        return True