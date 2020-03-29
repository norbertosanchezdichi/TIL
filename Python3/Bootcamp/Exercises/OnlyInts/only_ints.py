from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for value in args:
            if type(value) is not int or len(kwargs) != 0:
                return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return wrapper
    
@only_ints 
def add(x, y):
    return x + y
    
print(add(1, 2)) # 3
print(add("1", "2")) # "Please only invoke with integers."