from functools import wraps

def except_detect_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(str(e))
    return inner