import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)



def log_decorator(func):
    """
    Decorator for logging arguments and results
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs} -> Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)




def exception_handler(func):
    """
    Decorator for exception handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            return None
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

divide(10, 2)
divide(10, 0)