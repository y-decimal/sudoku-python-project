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
                self.view.set_field_valid(row, column)
        invalid_fields = self.model.get_invalid_fields()
        for row, column in invalid_fields:
            self.view.set_field_invalid(row, column)

    def push(self):
        '''Push updated values to the model | To be replaced'''
        for row in range(9):
            for column in range(9):
                value = self.view.get_field_value(row, column)
                state = self.view.get_field_state(row, column)
                self.model.set_field_value(row, column, value)
                self.model.set_field_state(row, column, state)
        self.fetch()

    def fetch_value(self, row, column):
        '''Fetch updated value from the model'''
        return self.model.get_field_value(row, column)

    def push_value(self, row, column, value):
        '''Push updated value to the model'''
        self.model.set_field_value(row, column, value)
        self.view.invalid_fields = self.model.get_invalid_fields()

    def generate(self):
        '''Callback for the generate button'''
        print("Generating")
        self.model.generate_random_sudoku()
        self.view.reset_highlighted_fields()
        self.fetch()
    
    def clear(self):
        '''Callback for the clear button'''
        
        print("Clearing")
        
        self.model.clear_sudoku()
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

    def set_mode(self, mode='normal'):
        '''Callback for the mode button'''
        self.model.set_mode(mode)
        self.view.dropdown_callback()

    def get_files(self):
        '''Callback for the get files method'''
        
        return self.model.get_files()
    
    def is_file_writeable(self, file_name):
        '''Checks if the file is writeable'''
        
        return self.model.is_file_writeable(file_name)

    def get_invalid_fields(self):
        '''Callback for the get_invalid_fields function'''
        return self.model.get_invalid_fields()
    
    def set_difficulty(self, difficulty):
        '''Callback for the set_difficulty function'''
        self.model.set_difficulty(difficulty)