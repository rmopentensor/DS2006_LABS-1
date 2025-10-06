import random

def roll_dice():
    return random.randint(1, 6)

winning_score = 3
players = []
rounds = 0
game_over = False

# Dictionary template for player info
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

# Obtain number of players
num_players = int(input("Enter the number of players: "))

# Gather player info
for i in range(num_players):
    player = player_info.copy()
    player["name"] = input(f"Enter name for player {i + 1}: ")
    player["email"] = input(f"Enter email for player {i + 1}: ")
    player["country"] = input(f"Enter country for player {i + 1}: ")
    players.append(player)

# Game loop
while not game_over:
    rounds += 1
    print(f"\nRound {rounds}")
    input("Press Enter to roll the dice...")

    current_rolls = []

    for player in players:
        roll = roll_dice()
        player["rolls"].append(roll)
        current_rolls.append((player["name"], roll))
        print(f"{player['name']} rolled a {roll}")

    # Get highest roll value
    max_roll_value = max(roll for _, roll in current_rolls)

    # Find winners for this round
    winners = []
    for player in players:
        if player["rolls"][-1] == max_roll_value:
            player["wins"] += 1
            winners.append(player["name"])
            print(f"{player['name']} wins this round!")

    print(f"Winners of this round: {', '.join(winners)}")

    # Check if any player reached winning score
    for player in players:
        if player["wins"] >= winning_score:
            print(f"\n{player['name']} is the our Battle of Dices Champion!!")
            game_over = True
            break

    if not game_over:
        print("This heated battle of Dices is still going on! Who will win in the end?")

# Save results to a file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    file.write("Player Information:\n\n")
    for player in players:
        file.write(
            f"Name = {player['name']}\n"
            f"Email = {player['email']}\n"
            f"Country = {player['country']}\n"
            f"Wins = {player['wins']}\n\n"
        )

    file.write("\nGame rounds:\n")
    for r in range(rounds):
        file.write(f"Round {r+1}:\n")
        rolls_str = ", ".join(f"{player['name']} rolled {player['rolls'][r]}" for player in players)
        file.write(rolls_str + "\n\n")

print("\nGame over! Results saved successfully.")