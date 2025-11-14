import random

def roll():
    return random.randint(1, 6)

print("\n_______WELCOME_TO_PIG______\n")

while True:
    min_players = int(input("Minimum Players : "))
    max_players = int(input("Maximum Players : "))
    players = input(f"Enter total number of players({min_players}-{max_players}): ")
    if players.isdigit():
        players = int(players)
        if min_players <= players <= max_players:
            break
        elif players < min_players:
            print(f"Minimum {min_players} players allowed")
        else:
            print(f"Only {min_players} - {max_players} allowed")
    else:
        print("Invalid Number. Please do not enter alphanumerics or symbols.")

max_score = 100
player_scores = [0 for _ in range(players)]

current_player = 0
while True:
    print(f"\nPlayer No. {current_player + 1} turn has now started")
    curr_score = 0

    while True:
        player_roll = input("Would you like to roll (y/n)? ")
        if player_roll.lower() == 'y':
            value = roll()
            print(f"You rolled: {value}")
            if value == 1:
                print("Rolled 1! No points earned this turn.")
                curr_score = 0
                break
            else:
                curr_score += value
                print(f"Current Turn Score: {curr_score}")
        elif player_roll.lower() == 'n':
            print(f"Player stops with {curr_score} points this turn.")
            break
        else:
            print("Invalid input, please type 'y' or 'n'.")

    player_scores[current_player] += curr_score
    print(f"Player {current_player + 1} Total Score: {player_scores[current_player]}")

    if player_scores[current_player] >= max_score:
        print(f"\nPlayer {current_player + 1} wins with {player_scores[current_player]} points! 🎉")
        break

    current_player = (current_player + 1) % players
