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