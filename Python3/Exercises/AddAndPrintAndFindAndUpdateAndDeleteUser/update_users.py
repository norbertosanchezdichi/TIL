from csv import reader, writer

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as file:
        users = list(reader(file))
        count = 0
        
        with open("users.csv", "w") as file:
            csv_writer = writer(file)
            for u in users:
                if u[0] == old_first and u[1] == old_last:
                    csv_writer.writerow([new_first, new_last])
                    count += 1
                else:
                    csv_writer.writerow(u)
                    
    return f"Users updated: {count}"
                    
print(update_users("Norberto", "Sanchez-Dichi", "Barack", "Obama"))