import random

random_number = random.randint(1, 10)

continue_playing = 'y'
guess = input('Guess a number from 1 through 10: ')

while continue_playing == 'y':

	while int(guess) != random_number:
	
		guess = input('Guess a number from 1 through 10: ')
		
	continue_playing = input('You guessed right!  Want to continue (y/n)?').lower()