from csv import DictReader

def print_users():
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        next(csv_reader)
        users = list(csv_reader)
        
        for u in users:
            print(f"{u['First Name']} {u['Last Name']}")
            
print_users()