def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if type(color) is not str:
        raise TypeError("color must be instance of str")
    if colornot in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")
    
colorize("hello", "red")
colorize(4, "red")