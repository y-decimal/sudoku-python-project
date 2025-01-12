from pathlib import Path
import os
import shutil


class FileManager:
    '''Dummy File Manager to use for testing or reference'''
    
    sudoku_testfiles_path = "/assets/TestFiles/"
    sudoku_files_path = "/assets/SudokuFiles/"
    absolute_path = None
    root_dir = None
    read_only_files = ["sudoku_easy", "sudoku_medium", "sudoku_hard", "sudoku_easy_possible_solution"]
    mode = "normal"
    
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
        
        if file_name == "" or file_name == None or not self.is_writeable(file_name):
            return False
        
        path = self.absolute_path + file_name  + ".txt"
        
        if not os.path.exists(self.absolute_path):
            os.makedirs(self.absolute_path)
            
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
        
        path = self.absolute_path + file_name + ".txt"
        
        try:
            
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
            
        except Exception as e:
            print(e)
            return None    

    
    def set_file_path(self, path):
        '''Sets the path to the file'''
        
        self.absolute_path = self.root_dir + path
        if not os.path.exists(self.absolute_path):
            os.makedirs(self.absolute_path)

        return True
    

    def set_file_mode(self, mode):
        '''Sets the mode to the file'''
        self.mode = mode
        if mode == 'debug':
            self.absolute_path = self.root_dir + self.sudoku_testfiles_path
        elif mode == 'normal':
            self.absolute_path = self.root_dir + self.sudoku_files_path
             
        if not os.path.exists(self.absolute_path):
            os.makedirs(self.absolute_path)
            
        if mode == 'debug':
            self.copy_default_files()
            
        return True
    
    
    def get_files(self):
        '''Returns the list of files in the current directory'''
        files = os.listdir(self.absolute_path)
        for index in range(len(files)):
            files[index] = files[index].split(".")[0]
        return files
    
    def is_writeable(self, file_name):
        '''Returns true if the file is writeable'''
    
        if file_name in self.read_only_files and self.mode != 'debug':
            return False
        
        path = self.absolute_path + file_name + ".txt"
        
        if os.path.exists(path):
            return os.access(path, os.W_OK)

        return True

    def copy_default_files(self):
        '''Copies default sudoku files to the current directory if they exist'''
        source_dir = self.root_dir + self.sudoku_files_path
        target_dir = self.root_dir + self.sudoku_testfiles_path

        for file_name in self.read_only_files:
            source_path = os.path.join(source_dir, file_name + ".txt")
            target_path = os.path.join(target_dir, file_name + ".txt")
            if os.path.exists(source_path) and not os.path.exists(target_path):
                shutil.copy(source_path, target_path)
                
