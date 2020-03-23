import pyfiglet
from termcolor import colored

msg = input("What would you like to print?")
color = input("What color?")

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art< color = "green"
print(colored_ascii)