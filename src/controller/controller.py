from DebugLog import Debug

class Controller:

    def __init__(self, model, view):
        '''Initializes the Controller'''
        self.model = model
        self.view = view

    def fetch(self):
        '''Fetch updated values from the model'''
        Debug.log_level2("Fetching")
        self.view.sudoku_view.supress_entry_callback = True
        for row in range(9):
            for column in range(9):
                value = self.model.get_field_value(row, column)
                state = self.model.get_field_state(row, column)
                self.view.sudoku_view.set_field_value(row, column, value)
                self.view.sudoku_view.set_field_state(row, column, state)
                self.view.sudoku_view.set_field_valid(row, column)
        invalid_fields = self.model.get_invalid_fields()
        for row, column in invalid_fields:
            self.view.sudoku_view.set_field_invalid(row, column)
        self.view.sudoku_view.supress_entry_callback = False

    def push(self):
        '''Push updated values to the model | To be replaced'''
        for row in range(9):
            for column in range(9):
                value = self.view.sudoku_view.get_field_value(row, column)
                state = self.view.sudoku_view.get_field_state(row, column)
                self.model.set_field_value(row, column, value)
                self.model.set_field_state(row, column, state)
        self.fetch()

    def fetch_value(self, row, column):
        '''Fetch updated value from the model'''
        return self.model.get_field_value(row, column)

    def push_value(self, row, column, value):
        '''Push updated value to the model'''
        self.model.set_field_value(row, column, value)
        self.view.sudoku_view.invalid_fields = self.model.get_invalid_fields()

    def generate(self):
        '''Callback for the generate button'''
        Debug.log_level2("Generating")
        self.model.generate_random_sudoku()
        self.view.sudoku_view.reset_highlighted_fields()
        self.fetch()
    
    def clear(self):
        '''Callback for the clear button'''
        
        Debug.log_level2("Clearing")
        
        self.model.clear_sudoku()
        self.view.sudoku_view.reset_highlighted_fields()
        self.fetch()

    def reset(self):
        '''Callback for the reset button'''
        Debug.log_level2("Resetting")
        self.model.reset_sudoku()
        self.view.sudoku_view.reset_highlighted_fields()
        self.fetch()
    
    def save(self, file_name):
        '''Callback for the save button'''
        self.push()
        self.model.save_sudoku(file_name)

    def load(self, file_name):
        '''Callback for the load button'''
        self.model.load_sudoku(file_name)
        self.fetch()
        
    def set_file_mode(self, mode='normal'):
        '''Callback for the file mode button'''
        self.model.set_file_mode(mode)
        self.view.sudoku_view.set_file_mode(mode)

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
        self.model.difficulty = difficulty
        
    def load_settings(self):
        '''Callback for the load_settings function'''
        return self.model.load_settings()

    def save_settings(self, settings):
        '''Callback for the save_settings function'''
        self.model.save_settings(settings)
        
    def set_mode(self, mode='normal'):
        '''Callback for the mode button'''
        self.model.set_mode(mode)
        self.view.sudoku_view.set_mode(mode)    
        
    def set_appearance(self, appearance):
        '''Callback for the set_appearance function'''
        self.view.sudoku_view.set_appearance(appearance)
        
    def set_scale(self, scale):
        '''Callback for the set_scale function'''
        self.view.sudoku_view.set_scale(scale)
        
    def update_colors(self):
        '''Callback for the update_colors function'''
        self.view.sudoku_view.update_colors()

    def set_field_state(self, row, column, state):
        '''Sets the state of a field'''
        self.model.set_field_state(row, column, state)

