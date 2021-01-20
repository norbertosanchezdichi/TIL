from random import choice

print('Rock...')
print('Paper...')
print('Scissors...')

player1 = input('Player 1, make your move: ').lower()

player2 = choice(['rock', 'paper', 'scissors'])

print(f'Computer plays {player2}')

if player1 == player2:
	print('Its a TIE!')
elif player1 == 'rock' and player2 == 'scissors':
	print('Player 1 WINS!')
elif player1 == 'paper' and player2 == 'rock':
	print('Player 1 WINS!')
elif player1 == 'scissors' and player2 == 'paper':
	print('Player 1 WINS!')
else:
	print('Computer WINS!')
