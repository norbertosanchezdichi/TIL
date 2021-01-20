def divide(num1, num2):
    try:
        result = num1 / num2
    except TypeError:
        return"Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    else:
        return result
        
#print(divide(4, 2))
#print(divide([], "1"))
#print(divide(1, 0))