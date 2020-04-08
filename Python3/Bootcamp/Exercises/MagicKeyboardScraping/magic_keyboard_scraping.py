import requests
from bs4 import BeautifulSoup
from fileds import reader

#response = requests.get("https://www.apple.com/shop/product/MXQT2LL/A/magic-keyboard-for-ipad-pro-11-inch-2nd-generation-us-english")

file = open("scratchpad.html")
soup = BeautifulSoup(file, "html.parser")
availability = soup.findAll(class_="as-purchaseinfo-dudeinfo-deliverymsg")

with open("juicy_details.txt", "w") as file:
    file.write("Currently unavailable" not in availability)