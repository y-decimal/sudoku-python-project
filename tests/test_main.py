import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model.model import Model



def test_FileManager():
    # This tests the file manager
    model = Model()
    assert model not None
   
    model.generate_sudoku()
    
    # Save empty model, should return true
    assert model.save_sudoku("testCase") is True

    # Load model with invalid file path
    assert model.load_sudoku("wrongPath") is False

    