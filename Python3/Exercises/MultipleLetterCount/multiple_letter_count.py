def multiple_letter_count(string):
    return {key: string.count(key) for key in string}
    
print(multiple_letter_count('Norberto'))