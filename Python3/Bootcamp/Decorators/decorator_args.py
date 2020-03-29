def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper
    
@shout
def greet(name):
    return f"Hi, I'm {name}."
    
@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."
    
print(greet("Juan"))

print(order("burger", "jalapeño poppers"))