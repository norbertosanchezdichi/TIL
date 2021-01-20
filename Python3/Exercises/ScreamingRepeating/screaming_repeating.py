number_of_times = input('How many times do I have to tell you? ')
number_of_times = int(number_of_times)

for time in range(number_of_times):
	
	print(f'time {time + 1}: CLEAN UP YOUR ROOM!')
	
	if (time + 1) > 3:
	
		print('DO YOU EVEN LISTEN ANYMORE?')
		
		break