def colorize(text, color):
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    
    print(f"Printed {text} in {color}")
    
colorize("hello", "red")
colorize(4, "red")