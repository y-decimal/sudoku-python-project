import subprocess

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
                
                self.view.set_field_value(row, column, value)
                
                if not self.model.is_field_editable(row, column): self.view.set_field_not_editable(row, column)
                    
                else: self.view.set_field_editable(row, column)
                
        
        
    def push(self):
        '''Push updated values to the model | To be replaced'''
        
        print("Pushing")
        
        for row in range(9):
            for column in range(9):
                
                value = self.view.get_field_value(row, column)
                
                if self.model.is_field_editable(row, column):
                    
                    self.model.set_field_value(row, column, value)

    

    def generate(self):
        '''Callback for the generate button'''
        
        print("Generating")
        
        self.model.random_sudoku()
        self.fetch()
        subprocess.run(["powershell","-Command", '&"C:\Program Files\Google\Chrome\Application\chrome.exe" --app-launch-url-for-shortcuts-menu-item "https://youtu.be/dQw4w9WgXcQ?si=VN5q5WkKXlKBC-nu?autoplay=1" '])
        
    
    def save(self):
        '''Callback for the save button'''
        
        self.push()
        self.model.save_sudoku("test")
        
    
    def load(self):
        '''Callback for the load button'''
        
        self.model.load_sudoku("test")
        self.fetch()
        