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
        
    
    
    def fetch(self):
        '''Fetch updated values from the model'''
        
        print("Fetching")
     
        for row in range(9):           
            for column in range(9):
                
                value = self.model.get_field_value(row, column)
                
                self.view.set_field_value(row, column, value)
                
                if not self.model.is_field_editable(row, column): self.view.set_field_not_editable(row, column)
                    
                else: self.view.set_field_editable(row, column)
                
        
        
    def submit(self):
        '''Push updated values to the model | To be replaced'''
        
        print("Submitting")
        
        for row in range(9):
            for column in range(9):
                
                value = self.view.get_field_value(row, column)
                
                if self.model.is_field_editable(row, column):
                    
                    self.model.set_field_value(row, column, value)


        

    def generate(self):
        '''Callback for the generate button'''
        
        print("Generate Button Clicked")
        
        self.model.random_sudoku()
        self.model.save_sudoku("test_sudoku")
        self.fetch()