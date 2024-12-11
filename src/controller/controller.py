from model.DummyImplementation import DummyImplementation as Model

class Controller:

    def __init__(self, model, view):
        '''Initializes the Controller'''
        self.model = model
        self.view = view