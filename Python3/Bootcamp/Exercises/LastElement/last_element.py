def last_element(listOfStuff):
    if listOfStuff:
        return listOfStuff[len(listOfStuff)]
    return None

print(last_element([1,2]))
print(last_element([]))