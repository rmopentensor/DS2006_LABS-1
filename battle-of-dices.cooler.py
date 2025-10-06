import random 

class dice:
    def rollD4(self):
        return random.randint(1,4)
    def rollD12(self): 
        return random.randint(1,12)

def battle_of_dices():
    dice_instance = dice()  # Create an instance of dice

    # Variables to keep track of the score 
    player1_wins = 0
    player2_wins = 0
    round_number = 1

    # Repeat rounds until one player reaches 3 wins

    while player1_wins < 3 and player2_wins < 3:
        print(f"\n--- Round {round_number} ---")
        input("Press ENTER to roll the dice...")

        # Each player rolls two dice and results are summed

        player1_roll = dice_instance.rollD4() + dice_instance.rollD12()
        player2_roll = dice_instance.rollD4() + dice_instance.rollD12()

        # Display the sum of dice rolls of each player 

        print("player 1 rolled a total of:", player1_roll)
        print("player 2 rolled a total of:", player2_roll)

        # Determine the winner of the round or if it's a tie

        if player1_roll > player2_roll:
            player1_wins += 1
            print("Player 1 wins this round!")
        elif player2_roll > player1_roll:
            player2_wins += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")

        # Display the current score after the round

        print(f"Score: Player 1 [{player1_wins}] vs Player 2 [{player2_wins}]")

        # Check if either player has won the game

        if player1_wins == 3:
            print("\n🏆 Player 1 is the world champion! 🏆")
        elif player2_wins == 3:
            print("\n🏆 Player 2 is the world champion! 🏆")
        
        round_number += 1

# Start the dice battle game
battle_of_dices()