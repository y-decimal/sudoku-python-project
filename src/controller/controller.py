class Controller:

    def __init__(self, model, view):
        '''Initializes the Controller'''
        self.model = model
        self.view = view
        
        for row in range(9):
            for column in range(9):
                
                value = self.model.get_field_value(row, column)
                if value != 0:
                    self.view.set_field_value(row, column, value)
                    self.view.set_field_not_editable(row, column)
        
    
    
    def fetch_button_clicked(self):
        '''Callback for the fetch button'''
        
        print("Fetch Button Clicked")
        
        self.model.load_sudoku("test_sudoku")
        
        for row in range(9):           
            for column in range(9):
                
                value = self.model.get_field_value(row, column)
                
                if value != 0: print(f"Field at row {row} and column {column} has value {value}")
                self.view.set_field_value(row, column, value)
                
        
        
    def submit_button_clicked(self):
        '''Callback for the submit button'''
        
        print("Submit Button Clicked")
        
        for row in range(9):
            for column in range(9):
                
                value = self.view.get_field_value(row, column)
                
                if self.model.is_field_editable(row, column):
                    
                    if value != 0: print(f"Setting field at row {row} and column {column} to value {value}")
                    self.model.set_field_value(row, column, value)


        self.model.save_sudoku("test_sudoku")
        
