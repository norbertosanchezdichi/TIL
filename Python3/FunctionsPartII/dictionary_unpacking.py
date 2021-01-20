def display_names(first, second):
    print(f"{first} says hello to {second}")
    
names = {"first": "Norberto", "second": "Lorenzo"}
display_names(**names)

def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print(kwargs)
    
data = dict(a=1, b=2, c=3, d=55, name="the Tiger")

add_and_multiply_numbers(**data, cat="blue")