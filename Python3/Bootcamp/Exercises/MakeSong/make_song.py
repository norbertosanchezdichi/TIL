def make_song(verses = 99, beverage = "soda"):
    for num in range(verses, -1, -1):
        if verses == 0:
            yield f"No more {beverage}!"
        elif verses == 1:
            yield f"Only {verses} bottle of {beverage} left!"
        else:    
            yield f"{verses} bottles of {beverage} on the wall."

song = make_song(4, "michelada")
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))