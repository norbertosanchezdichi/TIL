with open("haiku.txt", "a") as file:
    file.write("APPENDING LATER!")
    data = file.read()
    
print(data)