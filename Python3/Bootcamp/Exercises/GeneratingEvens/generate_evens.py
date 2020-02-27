def generate_evens():
    return [evenNumber for evenNumber in range(0, 50) if (evenNumber % 2) == 0]
    
print(generate_evens())