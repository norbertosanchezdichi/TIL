class Character:
    def __init__(self, name, hp, level):
        self._name = name
        self._hp = hp
        self._level = level
        
    @property
    def name(self):
        return self._name
        
    @property
    def hp(self):
        return self._hp
        
    @property
    def level(self):
        return self._level
        
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
    
    def speak(self):
        return f"speak"
        
villager = NPC("Bob", 100, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
print(villager.speak())