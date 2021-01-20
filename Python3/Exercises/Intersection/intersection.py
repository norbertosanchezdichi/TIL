def intersection(list1, list2):
    return list(set(list1) & set(list2))
    
print(intersection(['a','b','z'], ['x','y','z']))