def remove_negatives(listOfNums):
    return list(filter(lambda n: n >= 0, listOfNums))

print(remove_negatives([-1, 3, 4, -99]))