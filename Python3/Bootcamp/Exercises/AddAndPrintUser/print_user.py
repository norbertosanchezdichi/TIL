from csv import DictReader

def print_users():
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        next(csv_reader)
        
        for user in csv_reader:
            print(f"{user['First Name']} {user['Last Name']}")
            
print_users()