with open("haiku.txt", "a") as file:
    file.write("APPENDING LATER!")

with open("haiku.txt") as file:
    data = file.read()
    
print(data)