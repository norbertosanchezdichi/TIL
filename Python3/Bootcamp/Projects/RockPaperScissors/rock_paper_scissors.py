print('Rock...')
print('Paper...')
print('Scissors...')

player1 = input('Player 1, make your move: ')
print('.................' * 10)
player2 = input('Player 2, make your move: ')

if player1 == player2:
	print('Its a TIE!')
elif player1 == 'rock' and player2 == 'scissors':
	print('Player 1 WINS!')
elif player1 == 'paper' and player2 == 'rock':
	print('Player 1 WINS!')
elif player1 == 'scissors' and player2 == 'paper':
	print('Player 1 WINS!')
else:
	print('Player 2 WINS!')
