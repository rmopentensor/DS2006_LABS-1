
import random 

class dice:
    def rollD4():
        return random.randint(1,4)
    def rollD12(): 
        return random.randint(1,12)

def battle_of_dices():
    player1_wins = 0
    player2_wins = 0
    round_number = 1

    while player1_wins < 3 and player2_wins < 3:
        print(f"\n--- Round {round_number} ---")
        input("Press ENTER to roll the dice...")

        player1_roll = dice.rollD4()
        player2_roll = dice.rollD12()

        print("Player 1 rolled:", player1_roll)
        print("Player 2 rolled:", player2_roll)

        if player1_roll > player2_roll:
            player1_wins += 1
            print("Player 1 wins this round!")
        elif player2_roll > player1_roll:
            player2_wins += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")

        print(f"Score: Player 1 [{player1_wins}] vs Player 2 [{player2_wins}]")

        if player1_wins == 3:
            print("\n🏆 Player 1 is the world champion! 🏆")
        elif player2_wins == 3:
            print("\n🏆 Player 2 is the world champion! 🏆")
        
        # Round_increment added here 
        round_number += 1
    


    
    # Don't forget to call the function
battle_of_dices()
