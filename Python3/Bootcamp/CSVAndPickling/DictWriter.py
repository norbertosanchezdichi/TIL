from csv import DictWriter
with open("fighters_using_DictWriter.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, filednames = headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"
    })