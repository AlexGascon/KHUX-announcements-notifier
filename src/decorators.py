def logger(original_function):
    """Decorator that will log execution information of the method.
    Currently, it logs its name, arguments with which it has been run and execution time"""
    
    import time

    def wrapper_function(*args, **kwargs):
        print("Entering {}.\n Ran with arguments {} \nand keyword arguments {}").format(original_function.__name__,
                                                                                        args, kwargs)
        start_time = time.now

        result = original_function(*args, **kwargs)

        print("Exiting {}. Execution time: {}".format(original_function.__name__, time.now - start_time))

        return result