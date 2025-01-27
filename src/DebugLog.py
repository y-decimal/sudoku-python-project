class Debug:
    '''Debugging class to control the log level of the application'''
    
    LOG_LEVEL = {"disabled": 0, "minimal": 1, "normal": 2, "verbose": 3,"high": 4, "debug": 5}
    '''Dictionary containing the log levels. Keys are "disabled", "minimal", "normal", "verbose", "high" and "debug"'''
    
    current_log_level = LOG_LEVEL["disabled"]
    
    def log_level1(message):
        ''' Logs message if current log level is minimal or higher. \n
            Should be used for critical errors only'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["minimal"] and Debug.current_log_level < Debug.LOG_LEVEL["debug"]:
            print(message)
    
    def log_level2(message):
        ''' Logs message if current log level is normal or higher. \n
            Should be used for general information that only needs to be logged occasionally'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["normal"] and Debug.current_log_level < Debug.LOG_LEVEL["debug"]:
            print(message)
    
    def log_level3(message):
        ''' Logs message if current log level is verbose or higher \n
            Should be used for information that needs to be logged frequently'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["verbose"] and Debug.current_log_level < Debug.LOG_LEVEL["debug"]:
            print(message)
            
    def log_level4(message):
        '''Logs message if current log level is high or higher \n
            Should be used for information that needs to be logged very frequently'''
        if Debug.current_log_level >= Debug.LOG_LEVEL["high"] and Debug.current_log_level < Debug.LOG_LEVEL["debug"]:
            print(message)
            
    def log_level_debug(message):
        ''' Logs message if current log level is debug \n
            Should be used for information that needs to be logged many times a second. Will slow down the application'''
        if Debug.current_log_level == Debug.LOG_LEVEL["debug"]:
            print(message)