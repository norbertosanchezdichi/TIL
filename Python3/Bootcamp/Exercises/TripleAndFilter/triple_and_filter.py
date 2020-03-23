#Using list comprehension
def triple_and_filter(listOfNums):
    return [num * 3 for num in list(filter(lambda x: not x % 4, listOfNums))]
    
#Using map function   
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))
    
print(triple_and_filter([1, 2, 3, 4]))