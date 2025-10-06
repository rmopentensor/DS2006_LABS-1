import random 

def battle_of_dices_multiplayer(): 
    print("Welcome to Battle of Dices Multiplayer Edition!")

    num_players = int(input("How many players will join the battle? "))
    player_names = []
    for i in range(num_players):
        name = input(f" Enter name for Player {i+1}: ")
        player_names.append(name)
    player_wins = {name: 0 for name in player_names}
    round_number = 1

    while max(player_wins.values()) < 3:
        print(f"\n--- Round {round_number} ---")
        input("Press Enter to roll the dice...")
        contenders = player_names [:] 

        while True: # Introduce tie-breaking loop
            player_rolls = {}
            for name in contenders: 
                print(f"{name}'s turn to roll the dice.")
                roll = random.randint(1,6) 
                player_rolls[name] = roll
                print(f" {name} rolled: {roll}") 
            highest_roll = max(player_rolls.values())
            winners = [name for name, roll in player_rolls.items() if roll == highest_roll]
            if len(winners) == 1:
                winner = winners[0]
                player_wins[winner] +=1 
                print (f" {winner} wins this round!") 
                break # Exit tie-breaker loop on winner 
            else:
                print(f"Tie between: {', '.join(winners)}! Rolling again!")
                contenders = winners # Only tied players should roll again 

        print("Current Wins:")
        for name in player_names: 
            print(f"{name}: {player_wins[name]}")
        round_number += 1
        input ("Press Enter to continue to next round")

    top_winners = [name for name, wins in player_wins.items() if wins == 3]
    print("\n Champion: ", ', '.join(top_winners))
    print(f"Game finished in {round_number-1} rounds. \n")

    # Score summary
    print ("Final Score Summary:")
    for name in player_names:
        print (f"Player {name} won {player_wins[name]} rounds.")

# Sart game mode
battle_of_dices_multiplayer()