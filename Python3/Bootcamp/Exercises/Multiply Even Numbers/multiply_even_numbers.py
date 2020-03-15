def multiply_even_numbers(list):

    result = 1
    for number in list:
        if number % 2 == 0:
            result *= number
    
    return result
    
print(multiply_even_numbers([2, 4, 5]))    