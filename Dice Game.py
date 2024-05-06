import random 

class DiceGame:
    def __init__(mainp, number_players, high_score):
        # Initialize the game 
        mainp.number_players = number_players
        mainp.high_score = high_score
        mainp.players = [0] * number_players
        mainp.currently_players = 0

    def rolling_dice(mainp):
    # Roll the dice and returen the value 
        return [random.randint(1, 6) for _ in range(3)]

    def play_turning(mainp):

        print(f"Player {mainp.currently_players + 1}'s turn")
        score = 0
        fixed_diced = [] 

    while True:
        dice = mainp.rolling_dice()
        print(f"Dice roll: {dice}")

        def play_turn(mainp):
            # Play a turn for the current player
            print(f"Player {mainp.current_player + 1}'s turn:")
            score = 0
            fixed_dice = []  # Store the values of dice that are fixed
            
            while True:
                dice = mainp.roll_dice()  # Roll three dice
                print(f"Dice roll: {dice}")
                
                if len(set(dice)) == 1:
                    # If all three dice have the same value, the player "tuples out" and gets zero points
                    print("Tupled out! Zero points for this turn.")
                    return 0
                
                choice = input("Enter the indices of dice to fix (comma-separated), or 's' to stop: ")
                if choice.lower() == 's':
                    # If the player chooses to stop, exit the loop
                    break
                
                # Parse the input to fix dice
                indices = [int(i) - 1 for i in choice.split(',') if i.strip().isdigit()]
                for index in indices:
                    if 0 <= index < 3:
                        fixed_dice.append(dice[index])  # Add the value of the fixed dice to the list
                    else:
                        print("Invalid input. Try again.")

            # Calculate the score for turn
            for die in dice:
                if die not in fixed_dice:
                    score += die
            
            # Add the score to the current player's total score
            mainp.players[mainp.currently_players] += score
            print(f"Player {mainp.currently_players + 1} scored {score} points this turn.")
            return score

        def next_player(mainp):
            # Move to the next player
            mainp.currently_players = (mainp.currently_players + 1) % mainp.number_players

        def play_game(mainp):
            # Start the game
            print("Let's play the dice game!")
            while max(mainp.players) <mainp.high_score:
                # Play turns until a player reaches the target score
                mainp.play_turn()
                mainp.next_player()  # Move to the next player
            
            # Determine the winner
            winner = mainp.players.index(max(mainp.players)) + 1
            print(f"Player {winner} wins with a score of {max(mainp.players)}!")

