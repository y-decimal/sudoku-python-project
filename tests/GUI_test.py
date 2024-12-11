from src.App import App

def null_test():

    # Initialize the App
    app = App()
    
    # Check if the App is not None
    assert app is not None
    
    # Check if the MVC components are not None
    assert app.controller is not None
    assert app.view is not None
    assert app.model is not None
    
    # Check if the controller has a model and a view
    assert app.controller.model is not None
    assert app.controller.view is not None
    
    # Check if the view has a controller
    assert app.view.controller is not None
    
    