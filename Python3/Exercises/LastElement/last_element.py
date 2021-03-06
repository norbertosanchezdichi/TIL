# Compact solution
def last_element(listOfStuff):
    if listOfStuff:
        return listOfStuff[len(listOfStuff) - 1]
    return None

print(last_element([1,2]))
print(last_element([]))

# Ultra-compact solution
def last_element(listOfStuff):
    if listOfStuff:
        return listOfStuff[-1]
    return None
    
print(last_element([1,2]))
print(last_element([]))    