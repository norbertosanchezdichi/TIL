def list_manipulation(listOfStuff, command, location, value):
    if command == "remove":
        if location == "end":
            return listOfStuff.pop()
        elif location == "beginning":
            return listOfStuff.pop(0)
    elif command == "add":
        if location == "beginning":
            listOfStuff.insert(0, value)
            return listOfStuff
        elif location == "end":
            listOfStuff.append(value)
            return listOfStuff

print(list_manipulation([1, 2, 3], "remove", "end", 9))
print(list_manipulation([1, 2, 3], "remove", "beginning", 9))
print(list_manipulation([1, 2, 3], "add", "end", 9))
print(list_manipulation([1, 2, 3], "add", "beginning", 9))