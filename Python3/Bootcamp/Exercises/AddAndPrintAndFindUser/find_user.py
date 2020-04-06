from csv import DictReader

def find_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        
        for (index, user) in enumerate(csv_reader):
            if user['First Name'] == first_name and user['Last Name'] == last_name:
                print(index)
        print(f"{first_name} {last_name} not found.")
        
find_user('Buzz', 'Lightyear')