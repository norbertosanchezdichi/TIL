class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        self.__msg = "I like turtles!" # name mangling
    def doorman(self, guess):
        if guess == self._secret:
            pass
        
p = Person()

print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)
print(p._Person__lol)