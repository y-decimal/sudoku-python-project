from model.ISudokuInterface import ISudokuInterface

def test():

    # This is a placeholder test
    assert (ISudokuInterface.get_field_value(1,1) == 0)
    assert (ISudokuInterface.is_field_editable(1,1) == False)
