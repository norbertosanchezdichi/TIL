class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
        
    #@property
    #def name(self):
    #    return self.name
        
    #@property
    #def hp(self):
    #    return self.hp
        
    #@property
    #def level(self):
    #    return self.level
        
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
    
    #def speak(self):
        #return f"I heard there were monsters running around last night!"
        
villager = Character("Bob", 100, 12)
#print(villager.name)
#print(villager.hp)
#print(villager.level)
#print(villager.speak())