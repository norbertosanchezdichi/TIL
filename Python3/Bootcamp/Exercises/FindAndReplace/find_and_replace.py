def find_and_replace(file_name, search, replace):
    with open(file_name, "r+") as file:
        text = file.read()
        replaced_text = text.replace(search, replace)
        file.seek(0)
        file.write(replaced_text)
        file.truncate()
    
find_and_replace("story.txt", "Alice", "Norberto")