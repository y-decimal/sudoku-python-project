from pathlib import Path

class FileManager:
    
    def __init__(self, relative_path):
        '''Initializes the FileManager with a path relative to the root directory'''
        
        # Get the root directory of the project
        root_dir = str(Path(__file__).parent.parent.parent)

        # Set the absolute path using the root directory and the relative path
        self.absolute_path = root_dir+relative_path


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