class Controller:

    def __init__(self, model, view):
        '''Initializes the Controller'''
        self.model = model
        self.view = view

        self.fetch()
        
    
    
    def fetch(self):
        '''Fetch updated values from the model'''
        
        print("Fetching")
     
        for row in range(9):           
            for column in range(9):
                
                value = self.model.get_field_value(row, column)
                state = self.model.get_field_state(row, column)

                
                self.view.set_field_value(row, column, value)
                self.view.set_field_state(row, column, state)

                
                
        
        
    def push(self):
        '''Push updated values to the model | To be replaced'''
        
        #self.model.clear()
        for row in range(9):
            for column in range(9):     
                
                value = self.view.get_field_value(row, column)
                state = self.view.get_field_state(row, column)

                
                self.model.set_field_value(row, column, value)
                self.model.set_field_state(row, column, state)
                


    

    def generate(self):
        '''Callback for the generate button'''
        
        print("Generating")
        
        self.model.generate_random_sudoku()
        self.view.reset_highlighted_fields()
        self.fetch()

        
    
    def save(self, file_name):
        '''Callback for the save button'''
        
        self.push()
        self.model.save_sudoku(file_name)
        
    

    def load(self, file_name):
        '''Callback for the load button'''
        
        self.model.load_sudoku(file_name)
        self.fetch()
        

    def set_mode(self, mode = 'normal'):
        '''Callback for the mode button'''
        
        self.model.set_mode(mode)