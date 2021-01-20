def max_magnitude(listOfNums):
    return abs(max(listOfNums, key = lambda n: abs(n)))
    
print(max_magnitude([300, 20, -900]))