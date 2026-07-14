#snake and ladder

import random
players = ["player1","player2"]
player_pos = [0,0]
i=0
while True:
    input(f"{players[i]}'s turn. Press Enter to roll the dice...")
    dice_roll = random.randint(1,6)
    print(f"{players[i]} rolled a {dice_roll}")

    if player_pos[i] == 0 and dice_roll == 6:
        print(f"{players[i]} rolled a 6. You can start now!")
        player_pos[i] = 1
        print(f"{players[i]} is now at, {player_pos[i]}")

    elif player_pos[i] != 0:
        player_pos[i] += dice_roll
        print(f"{players[i]} rolled a {dice_roll} and is currently at, {player_pos[i]}")

    if player_pos[i] > 100:
        player_pos[i] -= dice_roll
        print(f"{players[i]} cannot move beyond 100. Staying at {player_pos[i]}.")

    snakes = {27:5, 40:3, 43:18, 54:31, 66:45, 76:58, 89:53, 99:41}
    ladders = {4:25, 13:46, 33:49, 42:63, 50:69, 62:81, 74:92}
    
    if player_pos[i] in snakes:
        print(f"Oh no! {players[i]} landed on a snake. Sliding down to {snakes[player_pos[i]]}.")
        player_pos[i] = snakes[player_pos[i]]
    
    elif player_pos[i] in ladders:
        print(f"Yay! {players[i]} climbed a ladder and is now at {ladders[player_pos[i]]}.")
        player_pos[i] = ladders[player_pos[i]]
    
    if player_pos[i] == 100:
        print(f"Congratulations! {players[i]} has won the game!")
        break
    
    i = (i + 1) % len(players)
