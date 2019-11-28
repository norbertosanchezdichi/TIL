donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

print(f'{donations.items() =}')

total_donations = 0.0

print('Using for-loop')
for donation_value in donations.values():
    total_donations += donation_value
    
print(f'{total_donations =}')

print('Using sum(..) with for-loop')
print(f'{sum(donation for donation in donations.values()) =}')

print('Using sum(..) without for-loop')
print(f'{sum(donations.values()) =}')