class User:
    def __init__(self, first):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"
        
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
        
    def likes(self, thing):
        return f"{self.first} likes {thing}"
        
    def is_senior(self):
        return self.age >= 65
        
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

user1 = User("Joe", "Dawson", 25)
user2 = User("Jack", "Chap", 29)

print(user1.full_name())
print(user2.full_name())

print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user1.initials())
print(user2.initials())

print(user1.is_senior())
print(user1.birthday())
print(user1.age)