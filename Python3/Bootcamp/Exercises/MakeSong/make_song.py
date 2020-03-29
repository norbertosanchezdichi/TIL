def make_song(verses = 99, beverage = "soda"):
    for num in range(verses, -1, -1):
        if num == 0:
            yield f"No more {beverage}!"
        elif num == 1:
            yield f"Only {num} bottle of {beverage} left!"
        else:    
            yield f"{num} bottles of {beverage} on the wall."

song = make_song(4, "michelada")
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))