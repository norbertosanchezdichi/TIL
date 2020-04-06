from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")