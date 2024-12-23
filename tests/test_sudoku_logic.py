import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model.SudokuLogic import SudokuLogic

@pytest.fixture
def sudoku():
    return SudokuLogic()

def test_clear(sudoku):
    """Test that the clear method resets the fields and starterfield."""
    sudoku.clear()
    assert sudoku.fields == [0] * 81
    assert sudoku.starterfield == [False] * 81

def test_new_sudoku(sudoku):
    """Test that new_sudoku method sets the fields and starterfield correctly."""
    new_sudoku = [1] * 81
    sudoku.new_sudoku(new_sudoku)
    assert sudoku.fields == new_sudoku
    assert sudoku.starterfield == [True] * 81

def test_get_field_value(sudoku):
    """Test that get_field_value returns the correct value."""
    sudoku.fields = [1] * 81
    assert sudoku.get_field_value(0, 0) == 1

def test_set_field_value(sudoku):
    """Test that set_field_value sets the value if the field is editable."""
    sudoku.fields = [0] * 81
    sudoku.starterfield = [False] * 81
    assert sudoku.set_field_value(0, 0, 5)
    assert sudoku.fields[0] == 5

def test_set_field_value_not_editable(sudoku):
    """Test that set_field_value does not set the value if the field is not editable."""
    sudoku.fields = [0] * 81
    sudoku.starterfield = [True] * 81
    assert not sudoku.set_field_value(0, 0, 5)
    assert sudoku.fields[0] == 0

def test_is_field_editable(sudoku):
    """Test that is_field_editable returns the correct boolean value."""
    sudoku.starterfield = [False] * 81
    assert sudoku.is_field_editable(0, 0)
    sudoku.starterfield = [True] * 81
    assert not sudoku.is_field_editable(0, 0)

def test_would_value_be_valid(sudoku):
    """Test that would_value_be_valid returns the correct boolean value."""
    sudoku.fields = [0] * 81
    assert sudoku.would_value_be_valid(0, 0, 5)
    sudoku.fields[1] = 5
    assert not sudoku.would_value_be_valid(0, 0, 5)

def test_generate_random_sudoku(sudoku):
    """Test that generate_random_sudoku generates a valid Sudoku puzzle."""
    sudoku.generate_random_sudoku()
    assert len(sudoku.fields) == 81
    assert len(sudoku.starterfield) == 81

def test_set_field_state(sudoku):
    """Test that set_field_state sets the state of a field correctly."""
    sudoku.set_field_state(0, 0, True)
    assert not sudoku.starterfield[0]
    sudoku.set_field_state(0, 0, False)
    assert sudoku.starterfield[0]

