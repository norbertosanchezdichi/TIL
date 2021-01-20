def find_and_replace(file_name, search, replace):
    with open(file_name, "r+") as file:
        text = file.read()
        replaced_text = text.replace(search, replace)
        file.seek(0)
        file.write(replaced_text)
        file.truncate()
    
find_and_replace("story.txt", "Alice", "Norberto")
find_and_replace("story.txt", "she", "he")
find_and_replace("story.txt", "She", "He")
find_and_replace("story.txt", "her", "his")
find_and_replace("story.txt", "Her", "His")
find_and_replace("story.txt", "herself", "himself")