from pathlib import Path

class FileManager:
    
    def __init__(self, relative_path):
        
        root_dir = str(Path(__file__).parent.parent.parent)

        self.absolute_path = root_dir+relative_path


    def save(self, content):
        with open(self.absolute_path, 'w') as file:
            file.write(content)
            
    
    def load(self):
        with open(self.absolute_path, 'r') as file:
            return file.read()
        
        
    def save_sudoku(self, sudoku: list):
        
        with open(self.absolute_path, 'w') as file:
            
            for row in range(9):
                for column in range(9):
                    file.write(str(sudoku[row][column]))
                    file.write("\n")

    def load_sudoku(self):
        
        with open(self.absolute_path, 'r') as file:
            
            sudoku = [[(0, True) for _ in range(9)] for _ in range(9)]
            
            for row in range(9):
                
                for column in range(9):
                    
                    line = file.readline()
                    value = int(line[1])
                    
                    if line[4] == 'T':
                        writeable_flag = True
                    elif line[4] == 'F':
                        writeable_flag = False
                                           
                    sudoku[row][column] = (value, writeable_flag)
            
            return sudoku