from random import choice

player_wins = 0
computer_wins = 0

while player_wins < 2 or computer_wins < 2:
	
	print(f'Player Score: {player_wins} Computer Score: {computer_wins}')
	
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
		player_wins += 1
	elif player1 == 'paper' and player2 == 'rock':
		print('Player 1 WINS!')
		player_wins += 1
	elif player1 == 'scissors' and player2 == 'paper':
		print('Player 1 WINS!')
		player_wins += 1
	else:
		print('Computer WINS!')
		computer_wins += 1

if player_wins > computer_wins:
	print('CONGRATULATIONS!')
else:
	print('Better luck next time!')
print(f'FINAL SCORE: Player Score: {player_wins} Computer Score: {computer_wins}')
