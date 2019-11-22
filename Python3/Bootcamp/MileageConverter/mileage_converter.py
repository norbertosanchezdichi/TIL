print("How many kilometers did you run today?)
kilometers = input()

miles = float(kilometers) / 1.60934
miles = round(miles, 2)
print(f"That is equal to {miles} miles.")