from csv import DictReader, DictWriter

def add_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        users = list(csv_reader)
        headers = users[0]
    
        with open("users.csv", "w") as file:
            csv_writer = DictWriter(file, fieldnames = headers)
            
            csv_writer.writeheader()
            
            for user in users:
                csv_writer.writerow({
                    "First Name": user["First Name"],
                    "Last Name": user["Last Name"]
                    })
            
            csv_writer.writerow({
                "First Name": first_name,
                "Last Name": last_name
                })

add_user("Dwayne", "Johnson")