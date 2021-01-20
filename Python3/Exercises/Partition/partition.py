def isEven(num):
    return num % 2 == 0

def partition(list, function):
    return [[value for value in list if function(value)], [value for value in list if not function(value)]]

def partition(list, function):
    return [[list.pop(list.index(index)) for index in list if function(index)], list]

print(partition([1, 2, 3, 4], isEven))