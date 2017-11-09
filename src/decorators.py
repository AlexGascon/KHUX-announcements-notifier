def logger(original_function):
    import time

    def wrapper_function(*args, **kwargs):
        print("Entering {}.\n Ran with arguments {} \nand keyword arguments {}").format(original_function.__name__,
                                                                                        args, kwargs)
        start_time = time.now

        result = original_function(*args, **kwargs)

        print("Exiting {}. Execution time: {}".format(original_function.__name__, time.now - start_time))

        return result