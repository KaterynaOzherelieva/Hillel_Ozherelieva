print("____TASK 1____")
def log_decorator(func):
    """
    Decorator for logging arguments and results
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs} -> Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)




print("____TASK 2____")
def exception_handler(func):
    """
    Decorator for exception handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

divide(10, 2)
divide(10, 0)