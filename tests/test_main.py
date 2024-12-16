import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.model import Model



def test_FileManager():
    # This tests the file manager
    model = Model()
    
    # Save empty model, should return true
    assert model.save_sudoku("testCase")

    # Load model with invalid file path
    assert not model.load_sudoku("wrongPath")

    