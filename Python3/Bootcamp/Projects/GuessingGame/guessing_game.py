import random

random_number = random.randint(1, 10)

continue = 'y'
guess = input('Guess a number from 1 through 10: ')

while continue = 'y':

	while guess != random_number:
	
		guess = input('Guess a number from 1 through 10: ')
		
	continue = input('You guessed right!  Want to continue (y/n)?').lower()