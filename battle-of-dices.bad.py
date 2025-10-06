import random

print('🎲 Welcome to Battle of Dices! 🎲')

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
player1_roll = random.randint(1,6)
player2_roll = random.randint(1,6)

# Round 1
input('\nPress ENTER to roll the dice...')

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input('\nPress ENTER to continue...')

# So far so good right? But how to check who got the highest roll?
player1_wins = 0
player2_wins = 0



# Round 2
input("\nPress ENTER to roll the dice...")


player1_roll = random.randint(1, 100)
print("Player 1 rolled: " + str(player1_roll))

player2_roll = random.randint(1, 100)
print("Player 2 rolled: " + str(player2_roll))

input("\nPress ENTER to continue...")


if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!\n")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("Player 2 wins this round!\n")
else:
    print("It's a tie!\n")

# Round 3
input("\nPress ENTER to roll the dice...")


player1_roll = random.randint(1, 100)
print("Player 1 rolled: " + str(player1_roll))

player2_roll = random.randint(1, 100)
print("Player 2 rolled: " + str(player2_roll))

input("\nPress ENTER to continue...")


if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!\n")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("Player 2 wins this round!\n")
else:
    print("It's a tie!\n")

# Round 4
input("\nPress ENTER to roll the dice...")


player1_roll = random.randint(1, 100)
print("Player 1 rolled: " + str(player1_roll))

player2_roll = random.randint(1, 100)
print("Player 2 rolled: " + str(player2_roll))

input("\nPress ENTER to continue...")


if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!\n")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("Player 2 wins this round!\n")
else:
    print("It's a tie!\n")

# Round 5
input("\nPress ENTER to roll the dice...")


player1_roll = random.randint(1, 100)
print("Player 1 rolled: " + str(player1_roll))

player2_roll = random.randint(1, 100)
print("Player 2 rolled: " + str(player2_roll))

input("\nPress ENTER to continue...")


if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!\n")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("Player 2 wins this round!\n")
else:
    print("It's a tie!\n")
