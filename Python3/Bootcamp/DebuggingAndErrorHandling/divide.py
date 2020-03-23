def divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong!"
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


print(divide('a', 2))