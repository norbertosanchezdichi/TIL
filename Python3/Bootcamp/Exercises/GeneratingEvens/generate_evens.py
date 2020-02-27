def generate_evens():
    return [evenNumber for evenNumber in range(1, 51) if (evenNumber % 2) == 0]
    
print(generate_evens())