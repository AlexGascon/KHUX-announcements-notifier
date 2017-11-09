def logger(original_function):
    """Decorator that will log execution information of the method.
    Currently, it logs its name, arguments with which it has been run and execution time"""
    
    import datetime

    def wrapper_function(*args, **kwargs):

        function_name = original_function.__name__

        start_time = datetime.datetime.now()
        print("Entering {}.\nRan with arguments {} \nand keyword arguments {}".format(function_name, args, kwargs))

        execution_result = original_function(*args, **kwargs)

        execution_time = datetime.datetime.now() - start_time
        print("Exiting {}. Execution time: {}".format(function_name, execution_time))

        return execution_result

    return wrapper_function()