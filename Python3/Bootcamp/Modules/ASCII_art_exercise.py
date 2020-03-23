import pyfiglet
from termcolor import colored

valid_colors = (red, green, yellow, blue, magenta, cyan, white)

msg = input("What would you like to print? ")
color = input("What color? ")

if color not in valid_colors:
    color = "blue"

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color = color)
print(colored_ascii)