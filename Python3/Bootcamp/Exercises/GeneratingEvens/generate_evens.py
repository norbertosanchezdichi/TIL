def generate_evens():
    return [evenNumber for evenNumber in range(1, 53) if (evenNumber % 2) == 0]
    
print(generate_evens())