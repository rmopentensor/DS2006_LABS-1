import random

print('🎲 Welcome to Battle of Dices! 🎲')

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
player1_roll = random.randint(1,20)
player2_roll = random.randint(1,20)

# Round 1
input('\nPress ENTER to roll the dice...')

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input('\nPress ENTER to continue...')

# So far so good right? But how to check who got the highest roll?
player1_wins = 0
player2_wins = 0
