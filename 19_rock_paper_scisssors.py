#!/usr/bin/env python3

import random

print('=====================================\n Rock Paper Scissors Lizard Spock\n=======================================')


player = int(input('You choose: \n(1) “is for Rock ✊” \n(2) “is for Paper ✋”	\n(3) “is for Scissors ✌️” \n(4) “is for Lizard 🦎” \n(5) “is for Spock 🖖”\n'))



computer = random.randint(1,5)

#if computer == 1 or player == 1:
#	print('✊')
#elif computer == 2 or player == 2:
#	print('✋')
	
print('You choose: '+str(player))
print('CPU choose: '+str(computer))

# 1 is for “Rock”.
# 2 is for “Paper”.
# 3 is for “Scissors”.
# 4 is for “Lizard”.
# 5 is for “Spock”.

if computer == player:
	print('Its a tie')
elif computer == 3 and player == 2:
	print('Scissors cut Paper, computer wins!')
elif computer == 2 and player == 3:
	print('Scissors cut Paper, player wins!')
elif computer == 2 and player == 1:
	print('Paper covers Rock, computer wins!')	
elif computer == 1 and player == 2:
	print('Paper covers Rock, player wins!')
elif computer == 1 and player == 4:
	print('Rock crushes Lizard, computer wins!')
elif computer == 4 and player == 1:
	print('Rock crushes Lizard, player wins!')
elif computer == 4 and player == 5:
	print('Lizard poisons Spock, computer wins!')
elif computer == 5 and player == 4:
	print('Lizard poisons Spock, player wins!')
elif computer == 5 and player == 3:
	print('Spock smashes Scissors, computer wins!')
elif computer == 3 and player == 5:
	print('Spock smashes Scissors, player wins!')
elif computer == 3 and player == 4:
	print('Scissors beat Lizard, computer wins!')
elif computer == 4 and player == 3:
	print('Scissors beat Lizard, player wins!')
elif computer == 4 and player == 2:
	print('Lizard eats Paper, computer wins!')
elif computer == 2 and player == 4:
	print('Lizard eats Paper, player wins!')
elif computer == 2 and player == 5:
	print('Paper disproves Spock, computer wins!')
elif computer == 5 and player == 2:
	print('Paper disproves Spock, player wins!')
elif computer == 5 and player == 1:
	print('Spock vaporizes Rock, computer wins!')
elif computer == 1 and player == 5:
	print('Spock vaporizes Rock, player wins!')
elif computer == 1 and player == 3:
	print('Rock breaks Scissors, computer wins!')
elif computer == 3 and player == 1:
	print('Rock breaks Scissors, player wins!')