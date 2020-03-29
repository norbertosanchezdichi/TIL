from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Here are the args: {args}")
        print(f"Here are the kwargs: {kwargs}")
        return fn(*args, **kwargs)
    return wrapper

@show_args
def do_nothing(self, a, b):
    pass

do_nothing(1, 2, 3, a = "hi", b = "bye")