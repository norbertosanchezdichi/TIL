from copy import copy
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age
        
    def __add__(self, other):
        if ininstance(other, Human):
            return Human(first = 'Newborn', last = self.last, age = 0)
        return "You can't add that!"
        
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "You can't multiply!"
        
j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
print(j)
print(len(j))

print(j + k)
triplets = j * 3
triplets[1].first = 'Jessica'
print(triplets)

triplets = (k + j) * 3