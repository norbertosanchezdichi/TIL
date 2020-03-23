import pyfiglet

msg = input("What would you like to print?")
color = input("What color?")

ascii_art = pyfiglet.figlet_format(msg)
print(ascii_art)