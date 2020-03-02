# Straigtforward solution

def speak(animal = "dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"
        
print(speak())

# Compact solution

def speak(animal = "dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    
    noise = noises.get(animal)
    
    if noise:
        return noise
    return "?"
    
print(speak())

# Ultra-Compact solution

def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    
    return noises.get(animal, '?')

print(speak())