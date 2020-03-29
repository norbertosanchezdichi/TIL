from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper
    
@speed_test
def sum_nums_gen(number):
    return sum(x for x in range(number))
    
def sum_nums_list(number):
    return sum([x for x in range(number)])
    
print(sum_nums_gen(50000000))
print(sum_nums_list(50000000))