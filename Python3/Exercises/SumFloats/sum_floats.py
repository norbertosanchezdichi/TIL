def sum_floats(*arg):
    return sum(arg for arg in arg if type(arg) is float)
    
print(sum_floats(1.5, 2.4, 'awesome', 3))