for number in range(1, 21):

	if number == 4 or number == 13:
		print(f'{number} is UNLUCKY!')
	elif number % 2 == 0:
		print(f'{number} is EVEN')
	else:
		print(f'{number} is ODD')