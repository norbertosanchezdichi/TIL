def display_names(first, second):
    print(f"{first} says hello to {second}")
    
names = {"first": "Norberto", "second": "Lorenzo"}
display_names(**names)