class Animal:
    def make_sound(self, sound):
        print(sound)
        
    cool = True
    
class Cat(Animal):
    pass
    
gandalf = Cat()
gandalf.make_sound("meow")
gandalf.cool = True
print(gandalf.cool)
print(Cat.cool)
print(Animal.cool)
print(isinstance(gandalf, Animal))
