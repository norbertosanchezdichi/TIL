class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")
        
class Dog(Animal):
    def speak(self):
        return "woof"
        
class Cat(Animal):
    def speak(self):
        return "meow"
        
class Fish(Animal):
    pass
    
d = Dog()
print(d.speak())
f = Fish()
print(f.speak())

sample_list = [1, 2, 3]
sample_tuple = (1, 2, 3)
sample_string = "awesome"

len(sample_list)
len(sample_tuple)
len(sample_string)