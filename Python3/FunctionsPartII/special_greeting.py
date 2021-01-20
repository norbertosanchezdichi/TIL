def special_greeting(**kwargs):
    if "Norberto" in kwargs and kwargs["Norberto"] == "special":
        return "You get a special greeting Norberto!"
    elif "Norberto" in kwargs:
        return f"{kwargs['Norberto']} Norberto!"
    
    return "Not sure who this is..."
    
print(special_greeting(Norberto='special'))
print(special_greeting(Norberto='hello'))
print(special_greeting(Lorenzo='squawk'))