age = input('How old are you?')

if age:
	age = int(age)
	
	if age >= 21:
		print('You can enter and can drink!')
	elif age >= 18:
		print('You can enter but you need a wristband!')
	else:
		print('You can\'t come in, little one! :[')
else:
	print('Enter an age!')