for number in range(1, 21):

	if number == 4 or number == 13:
		state = 'UNLUCKY'
	elif number % 2 == 0:
		state = 'EVEN'
	else:
		state = 'ODD'

print(f'{number} is {state}!')