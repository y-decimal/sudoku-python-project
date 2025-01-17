class Debug:
    '''Debugging class to control the log level of the application'''
    
    LOG_LEVEL = {"disabled": 0, "minimal": 1, "normal": 2, "verbose": 3,"high": 4, "debug": 5}
    '''Dictionary containing the log levels. Keys are "disabled", "minimal", "normal", "verbose", "high" and "debug"'''
    
    current_log_level = LOG_LEVEL["disabled"]
    
    def log_level1(message):
        '''Logs message if current log level is minimal or higher'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["minimal"]:
            print(message)
    
    def log_level2(message):
        '''Logs message if current log level is normal or higher'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["normal"]:
            print(message)
    
    def log_level3(message):
        '''Logs message if current log level is verbose or higher'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["verbose"]:
            print(message)
            
    def log_level4(message):
        '''Logs message if current log level is high or higher'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["high"]:
            print(message)
            
    def log_level5(message):
        '''Logs message if current log level is debug'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["debug"]:
            print(message)