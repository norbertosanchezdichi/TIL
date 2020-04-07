import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.apple.com/shop/product/MXQT2LL/A/magic-keyboard-for-ipad-pro-11-inch-2nd-generation-us-english")

print(response.text)

soup = BeautifulSoup(response.text, "html.parser")





