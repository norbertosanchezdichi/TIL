 instructor1 = "Mary"
 def say_hello():
    instructor2 = "Norberto"
    return f'Hello {instructor1}'
    
print(say_hello())
print(instructor2) #NameError

total = 0
def increase_total():
    total += 1  #UnboundLocalError: local variable "total" not found.  Must use "global" keyword.  Only works if the variable is only accessed and an assignment is not attempted.
    return total
    
total = 0
def increase_total():
    global total
    total += 1
    return total
    
def outer():
    count = 0
    def inner():
        nonlocal count #nonlocal keyword allows to modify a parent function's variable and not a global variable.
        count += 1
        return count
    return inner()