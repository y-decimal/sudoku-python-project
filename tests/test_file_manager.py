import sys
import os
import shutil
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model.FileManager import FileManager

@pytest.fixture
def file_manager():
    return FileManager()

def prepare_test_files(file_manager):
    if os.path.exists(file_manager.root_dir + file_manager.sudoku_testfiles_path + "testCase.txt"):
        os.remove(file_manager.root_dir + file_manager.sudoku_testfiles_path + "testCase.txt")
    if os.path.exists(file_manager.root_dir + "/new/path"):
        os.rmdir(file_manager.root_dir + "/new/path")
        os.rmdir(file_manager.root_dir + "/new")
        

@pytest.fixture(autouse=True)
def run_before_and_after_tests(file_manager):
    # Before each test
    prepare_test_files(file_manager)
    yield
    # After each test
    prepare_test_files(file_manager)

def test_initialization(file_manager):
    '''Tests the FileManager initialization'''
    assert file_manager is not None

def test_mode(file_manager):
    '''Tests the FileManager set_mode method'''
    # Test set_mode with debug mode
    file_manager.set_file_mode("debug")
    assert file_manager.absolute_path == file_manager.root_dir + file_manager.sudoku_testfiles_path
    
    # Test set_mode with normal mode
    file_manager.set_file_mode("normal")
    assert file_manager.absolute_path == file_manager.root_dir + file_manager.sudoku_files_path

def test_save(file_manager):
    '''Tests the save method of the FileManager'''
    file_manager.set_file_mode("debug")
    
    sudoku = [[(0, True) for _ in range(9)] for _ in range(9)]
    
    # Save empty sudoku, should return true
    assert file_manager.save_sudoku(sudoku, "testCase") is True
    
    # Save sudoku with invalid file path, should return false
    assert file_manager.save_sudoku(sudoku, "") is False

def test_load(file_manager):
    '''Tests the load method of the FileManager'''
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

def test_save_load(file_manager):
    '''Tests the save and load methods of the FileManager'''
    file_manager.set_file_mode("debug")
    
    content = "Test content"
    file_name = "testCase.txt"
    
    # Save content
    file_manager.save(content, file_name)
    
    # Load content
    loaded_content = file_manager.load(file_name)
    assert loaded_content == content

def test_set_file_path(file_manager):
    '''Tests the set_file_path method of the FileManager'''
    path = "/new/path/"
    assert file_manager.set_file_path(path)
    assert file_manager.absolute_path == file_manager.root_dir + path

def test_save_to_non_existent_directory(file_manager):
    '''Tests saving to a non-existent directory'''
    non_existent_path = "/non_existent_path/"
    
    # Ensure the directory does not exist before the test
    if os.path.exists(file_manager.root_dir + non_existent_path):
        if os.path.exists(file_manager.root_dir + non_existent_path + "testCase.txt"):
            os.remove(file_manager.root_dir + non_existent_path + "testCase.txt")
        os.rmdir(file_manager.root_dir + non_existent_path)
    
    file_manager.set_file_path(non_existent_path)
    
    sudoku = [[(0, True) for _ in range(9)] for _ in range(9)]
    
    # Save sudoku to non-existent directory, should return true and create the directory
    assert file_manager.save_sudoku(sudoku, "testCase") is True
    assert os.path.exists(file_manager.absolute_path)
    
    # Clean up by removing the created directory
    os.remove(file_manager.root_dir + non_existent_path + "testCase.txt")
    os.rmdir(file_manager.root_dir + non_existent_path)

def test_save_sudoku_exception(file_manager):
    '''Tests if save_sudoku returns false when catching an exception'''
    file_manager.set_file_mode("debug")
    
    sudoku = [[(0, True) for _ in range(8)] for _ in range(8)]
    
    # Save sudoku, should return false due to the sudoku being out of bounds
    assert not file_manager.save_sudoku(sudoku, "testCase")

