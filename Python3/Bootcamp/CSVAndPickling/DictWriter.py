from csv import DictWriter
with open("fighters_using_DictWriter.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames = headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"
    })
    
from csv import DictReader

def cm_to_in(cm):
    return float(cm) * 0.393701

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = (list(csv_reader))
    
with open("fighters_in_inches.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames = headers)
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_in(f["Height (in cm)"])
            })