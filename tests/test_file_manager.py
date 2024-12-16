import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model.FileManager import FileManager


def test_initialization():
    '''Tests the FileManager initialization'''
    
    # Test FileManager initialization
    file_manager = FileManager()
    assert file_manager is not None
   
def test_mode():
    '''Tests the FileManager set_mode method'''

    file_manager = FileManager()

    # Test set_mode with debug mode
    file_manager.set_file_mode("debug")
    assert file_manager.absolute_path == file_manager.root_dir + file_manager.sudoku_testfiles_path
    
    # Test set_mode with normal mode
    file_manager.set_file_mode("normal")
    assert file_manager.absolute_path == file_manager.root_dir + file_manager.sudoku_files_path
    
    
def test_save():
    '''Tests the save method of the FileManager'''
    
    file_manager = FileManager()
    file_manager.set_file_mode("debug")
    
    sudoku = [[(0, True) for _ in range(9)] for _ in range(9)]
    
    # Save empty sudoku, should return true
    assert file_manager.save_sudoku(sudoku, "testCase") is True
    
    # Save sudoku with invalid file path, should return false
    assert file_manager.save_sudoku(sudoku, "") is False
    

def test_load():
    '''Tests the load method of the FileManager'''

    file_manager = FileManager()   
    file_manager.set_file_mode("debug")
    
    sudoku = [[(0, True) for _ in range(9)] for _ in range(9)]

    # Save empty sudoku
    file_manager.save_sudoku(sudoku, "testCase")
    
    # Load file with invalid file path
    assert file_manager.load_sudoku("wrongPath") is None

    # Load file with valid file path
    assert file_manager.load_sudoku("testCase") == sudoku
    
    # Save file with defined values   
    sudoku[0][0] = (1, False)
    sudoku[1][1] = (2, False)
    sudoku[2][2] = (3, False)
    sudoku[3][3] = (4, False)
    sudoku[4][4] = (5, False)
    sudoku[5][5] = (6, False)
    sudoku[6][6] = (7, False)
    sudoku[7][7] = (8, False)
    sudoku[8][8] = (9, False)
    
    file_manager.save_sudoku(sudoku, "testCase")
    
    # Load file with defined values
    assert file_manager.load_sudoku("testCase") == sudoku
    
