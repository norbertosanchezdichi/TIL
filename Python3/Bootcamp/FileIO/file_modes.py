with open("haiku.txt", "a") as file:
    file.write("APPENDING LATER!")

with open("haiku.txt") as file:
    data = file.read()
    
print(data)

with open("haiku.txt", "r+") as file:
    file.write("\nADDED USING r+")
    file.seek(20)
    file.write(":)")
    data = file.read()
    
print(data)