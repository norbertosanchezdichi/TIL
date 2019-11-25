for number in range(1,11):

	print('\U0001f600' * number)

number = 0
while number < 11:

	print('\U0001f600' * number)
	number += 1

for number in range(1,11):
	
	count = 1
	smileys = ""
	
	while count < number:
	
		smileys += '\U0001f600'
		count += 1
	
	print(smileys)
