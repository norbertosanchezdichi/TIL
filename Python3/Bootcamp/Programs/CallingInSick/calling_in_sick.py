from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

calling_in_sick = False

if (actually_sick and (sick_days != 0)) or (kinda_sick and hate_your_job and (sick_days != 0)):
    
    calling_in_sick = True
    
print(f'Calling in sick is {calling_in_sick}')