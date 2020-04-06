import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

c = Cat("Charles", "Toby")

with open("cat.json", "w") as file:
    frozen = jsonpickle.encode(c)
    file.write(frozen)
    
with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(c)
    print(unfrozen)