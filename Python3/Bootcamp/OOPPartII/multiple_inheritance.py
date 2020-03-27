class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT")
        self.name = name
        
    def swim(self):
        return f"{self.name} is swimming"
        
    def greet(self):
        return f"I am {self.name} of the sea!"
        
class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INIT")
        self.name = name
        
    def walk(self):
        return f"{self.name} is walking"
        
    def greet(self):
        return f"I am {self.name} of the land!"
        
class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("PENGUIN INIT")
        Ambulatory.__init__(name = name) # using super() would make code be ambiguous  
        Aquatic.__init__(self, name = name)
        

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_hook = Penguin("Captain Hook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print(f"captain_hook is instance of Penguin: {isinstance(captain_hook, Penguin)}")
print(f"captain_hook is instance of Aquatic: {isinstance(captain_hook, Aquatic)}")
print(f"captain_hook is instance of Ambulatory: {isinstance(captain_hook, Ambulatory)}")