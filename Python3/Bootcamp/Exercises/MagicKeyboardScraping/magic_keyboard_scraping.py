import requests
from bs4 import BeautifulSoup
from csv import reader

#response = requests.get("https://www.apple.com/shop/product/MXQT2LL/A/magic-keyboard-for-ipad-pro-11-inch-2nd-generation-us-english")

with open("scratchpad.html") as file:
    data = reader(file)
    soup = BeautifulSoup(str(data), "html.parser")

li = soup.find(class_ = "as-purchaseinfo-availabilityinfo row")
div1 = li.find(class_ = "as-pdp-deliverydates column large-6 small-6 isdudeavailable as-purchaseinfo-dudeinfo as-icondetails as-icondetails-topicon")
div2 = div1.find(class_ = "shipdeliverydates as-pdp-shipdeliverydates")

#with open("juicy_details.txt", "w") as file:
#    file.write()