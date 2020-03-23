def triple_and_filter(listOfNums):
    return [num * 3 for num in list(filter(lambda x: not x % 4, listOfNums))]
    
print(triple_and_filter([1, 2, 3, 4]))