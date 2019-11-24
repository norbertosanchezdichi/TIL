from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|           
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /

if x > 0:
    
    if y > 0:
    
        print("both positive")

    else: 
        
        print("x is positive and y is negative")
        
elif x < 0:

    if y > 0:
        
        print("y is positive and x is negative")

    elif y < 0:

        print("both negative")