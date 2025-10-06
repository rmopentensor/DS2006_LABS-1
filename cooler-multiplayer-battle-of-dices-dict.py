import random
import copy 

def rollD6():
    return random.randint(1, 6)
print(" Welcome to Cooler Battle of Dices!")
winning_score = 3
player_info = {

    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []

}

# Use list to store each players information
players = []

# User command to determine the number of players participating 
number_of_players = int(input("How many players are playing?"))

for i in range(number_of_players):

    player = copy.deepcopy(player_info)

    # Add information about each player to the dictionary using seperate lists
    player ["name"] = input (f"Enter player name {i+1}")
    player ["email"] = input (f"Enter player email {i+1}")
    player ["country"] = input(f"Enter the country of the player {i+1}")

    players.append(player)

gameover = False
rounds_played = 0
while gameover is False:
    
    rounds_played += 1
    print(f"\n This is round {rounds_played}!")

    enter = input("Press enter to continue")

    # Use list to store dice rolls for each player in current round
    current_rolls = []

    for each_player in players:
        roll = rollD6()
        current_rolls.append(roll)
        each_player['rolls'].append(roll)
        print(f"Player {each_player['name']}, rolled: {roll}")


    # Continue gameplay 
    input("\n Press Enter to continue..")


    # Determine the highest roll 
    max_roll = max(current_rolls)

    # Use list to store round winners
    round_winners = []

    for each_player in players:
        if (each_player["rolls"][-1] == max_roll): 
            each_player["wins"] += 1
            round_winners.append(each_player['name'])

    print(f"The winners of this round are: {round_winners}!")

    for each_player in players:
        if (each_player["wins"] >= winning_score):
            print(f"\n {each_player['name']} wins the game with {each_player['wins']} wins! Great Battle!")
            gameover = True
            break 
    if gameover is False: 
        print(F"Continuing to next round {rounds_played}!")
        print(" --------------------- ")

# Save logs to text file if desired by user
filename = input("Enter a filename to save the log history: ")
with open(filename, 'w') as file:
    file.write("player information: \n")
    for each_player in players:
        file.write(
            f" Name: {each_player['name']}\n"
            f"* E-mail: {each_player['email']}\n"
            f"* Country: {each_player['country']}\n"
            f"* Wins: {each_player['wins']}\n\n"
        )
    file.write("\n Game rounds: \n")
    # Round history 
    for r in range(rounds_played):
        rolls_str = ""
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"
            if i < len(players) - 1:
                rolls_str += ",  "
        file.write(f"Round {r+1}: {rolls_str}\n")

print("\n Game over! Results saved succesfully.")

