# Round 1

import random

input("\nPress ENTER to roll the dice...")

player1_Round1_roll = random.randint(1,6)
player2_Round1_roll = random.randint(1,6)

print(f"Player 1 rolled: {player1_Round1_roll}")
print(f"Player 2 rolled: {player2_Round1_roll}")

if player1_Round1_roll > player2_Round1_roll:
    print("Player 1 wins Round 1!")
elif player2_Round1_roll > player1_Round1_roll:
    print("Player 2 wins Round 1!")
else:
    print("Round 1 is a tie!")

    # Round 2

input("\nPress ENTER to roll the dice...")

player1_Round2_roll = random.randint(1,6)
player2_Round2_roll = random.randint(1,6)

print(f"Player 1 rolled: {player1_Round2_roll}")
print(f"Player 2 rolled: {player2_Round2_roll}")

if player1_Round2_roll > player2_Round2_roll:
    print("Player 1 wins Round 2!")
elif player2_Round2_roll > player1_Round2_roll:
    print("Player 2 wins Round 2!")
else:
    print("Round 2 is a tie!")

   #  Round 3
input("\nPress ENTER to roll the dice...")
player1_Round3_roll = random.randint(1,6)
player2_Round3_roll = random.randint(1,6)

print(f"\nPlayer 1 rolled: {player1_Round3_roll}")
print(f"Player 2 rolled: {player2_Round3_roll}")

if player1_Round3_roll > player2_Round3_roll:
        print("Player 1 wins Round 3!")
elif player2_Round3_roll > player1_Round3_roll:
        print("Player 2 wins Round 3!")
else:
        print("Round 3 is a tie!")

# Round 4
input("\nPress ENTER to roll the dice...") 
player1_Round4_roll = random.randint(1,6)
player2_Round4_roll = random.randint(1,6)

print(f"\nPlayer 1 rolled: {player1_Round4_roll}")
print(f"Player 2 rolled: {player2_Round4_roll}")

if player1_Round4_roll > player2_Round4_roll:
        print("Player 1 wins Round 4!")
elif player2_Round4_roll > player1_Round4_roll:
        print("Player 2 wins Round 4!")
else:
        print("Round 4 is a tie!")

# Game Summary
print("Game Over! Here's the round-by-round summary:")

rounds = [
("Round 1", player1_Round1_roll, player2_Round1_roll),
("Round 2", player1_Round2_roll, player2_Round2_roll),
("Round 3", player1_Round3_roll, player2_Round3_roll),
("Round 4", player1_Round4_roll, player2_Round4_roll)
]

for round_name, player1_roll, player2_roll in rounds:
        print(f"{round_name}: Player 1 rolled {player1_roll}, Player 2 rolled {player2_roll}")

    # Game Summary

print("Game Over! Here's the round-by-round summary:")

rounds = [
    ("Round 1", player1_Round1_roll, player2_Round1_roll),
    ("Round 2", player1_Round2_roll, player2_Round2_roll),
    ("Round 3", player1_Round3_roll, player2_Round3_roll),
    ("Round 4", player1_Round4_roll, player2_Round4_roll)
]

import random
def rollD4():
    return random.randint(1, 4)
def rollD6():
    return random.randint(1, 6)
def rollD8():
    return random.randint(1, 8)
def rollD10():
    return random.randint(1, 10)
def rollD12():
    return random.randint(1, 12)
def rollD20():
    return random.randint(1, 20)

import random

def rollD6():
    return random.randint(1, 6)

player1_wins = 0
player2_wins = 0
num_rounds = 4
player1_rolls = []
player2_rolls = []

rounds_played = 0   # Track rounds played
game_over = False   # Flag for early game end (not used here, but ready for future use)

print("🎲 Welcome to Battle of dice! 🎲")

for round_num in range (1,num_rounds + 1): 

    input(f"Press Enter to roll the dice and start the game {round_num}...")
    

    player1_roll = rollD6()
    print(f"Player 1 rolled: {player1_roll}")
    player1_rolls.append(player1_roll)
    player2_roll = rollD6()
    player2_rolls.append(player2_roll)
    print(f"Player 2 rolled: {player2_roll}")

    if player1_roll > player2_roll: 
        print(f"Player 1 wins this round {round_num} !")
        player1_wins +=1
    elif player2_roll > player1_roll:
        print(f" Player 2 wins this round {round_num} !")
        player2_wins +=1
    else: 
        print(f"Round {round_num} a tie! The excitement continues!")

     # After the game ends
print("Game Summary")
print("Round | Player 1 | Player 2 | Dice Used")
print("This was fun!")

for i in range(num_rounds):
    print(f"{i+1}: {player1_rolls[i]}  {player2_rolls[i]}      D6")

print(f"\nFinal Score: Player 1 Wins = {player1_wins}, Player 2 Wins = {player2_wins}")
