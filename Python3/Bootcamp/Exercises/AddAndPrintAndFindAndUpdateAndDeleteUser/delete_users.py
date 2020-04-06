from csv import reader, writer

def delete_users(first_name, last_name):
    with open("users.csv") as file:
        users = list(reader(file))
        count = 0
        
        with open("users.csv", "w") as file:
            csv_writer = writer(file)
            for u in users:
                if u[0] == first_name and u[1] == last_name:
                    count += 1
                    continue
                else:
                    csv_writer.writerow(u)
                    
    return f"Users updated: {count}"
                    
print(delete_users("Norberto", "Sanchez-Dichi"))