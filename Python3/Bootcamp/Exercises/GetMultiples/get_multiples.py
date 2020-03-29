def get_multiples(num = 1, multiples = 10):
    for multiple in range(1, multiples + 1):
        yield num * multiple
        
