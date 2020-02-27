def generate_evens():
    return [evenNumber if (evenNumber % 2 == 0) for evenNumber in range(0, 50)]
    
print(generate_evens())