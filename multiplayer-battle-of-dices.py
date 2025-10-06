import random

# Game setup
winning_score = 3  # Number of wins needed to win the game
player_names = []  # List to store player names
player_wins = []  # List to store player win counts
player_rolls_history = []  # List to store each player's roll history
game_over = False  # Game over flag
rounds_played = 0  # Count of rounds played

# Get player information
print("🎲 Welcome to Multiplayer Battle of Dice! 🎲")
number_of_players = int(input("How many players? "))
for i in range(number_of_players):
    name = input(f"Enter name for player {i + 1}: ")
    player_names.append(name)
    player_wins.append(0)  # Initialize win count for each player
    player_rolls_history.append([])  # Initialize roll history for each player

# Main game loop
while not game_over:
    print(f"\nRound {rounds_played + 1}!")
    current_rolls = []

    # Each player rolls the dice
    for i in range(number_of_players):
        roll = random.randint(1, 6)
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"{player_names[i]} rolled a {roll}")

    # Determine round winners
    max_roll = max(current_rolls)
    winners = []
    for i in range(number_of_players):
        if current_rolls[i] == max_roll:
            winners.append(player_names[i])
            player_wins[i] += 1

    print(f"Winners of this round: {', '.join(winners)}")

    # Check for end game
    for i in range(number_of_players):
        if player_wins[i] == winning_score:
            print(f"\n{player_names[i]} is the overall winner! 🏆")
            game_over = True
            break

    rounds_played += 1