


import random

player_names = ['Matthew', 'Jean', 'Caroline', 'Adrienne', 'Ron', 'Dot', 'Roger', 'Gary', 'Julissa']

while True:
    num_players = int(input('How many players? '))
    if num_players < 3 or num_players > 9:
        print('Fool! You can only play with 3-9 players.')
    else:
        break


def pick_players():
    players = []
    for player in range(num_players):
        player_name = random.choice(player_names)
        player_names.remove(player_name)            # removes name from list so we don't have two poeple with the same name
        num_chips = 3
        players.append({'name': player_name, 'chips': num_chips})
    return players

# print(pick_players())

def roll_bones():
    faces = ['L', 'C', 'R', '.', '.', '.']
    roll = random.choice(faces)
    return roll

# print(roll_bones())

def find_winner():
    winner = None
    for player in players:  # player is a dictionary
        if player['chips'] >= 1:
            if winner is None:  # if we find a player with chips, they become the winner, if there isn't one already
                winner = player
            else:
                return None  # if there's already a player called winner, we exit the loop, game isn't over yet
    return winner

pot = 0
player_id = 0
players = pick_players()

while True:
    player = players[player_id]
    num_chips = player['chips']
    player_id_lf = player_id - 1
    player_id_rt = player_id + 1
    if player_id_rt == len(players):
        player_id_rt = 0
    if num_chips >= 3:
        num_rolls = 3
    else:
        num_rolls = num_chips
    for roll in range(num_rolls):
        outcome = roll_bones()   # if outcome is '.', nothing happens
        if outcome == 'C':
            pot += 1
            num_chips -= 1
        if outcome == 'R':
            players[player_id_rt]['chips'] += 1
            num_chips -= 1
        if outcome == 'L':
            players[player_id_lf]['chips'] += 1
            num_chips -= 1
    player['chips'] = num_chips

    for player in players:
        print(player['chips'], end=' ')
    print()

    winner = find_winner()      # if the function returns a value, assign a variable to call the function
    if winner is not None:
        winner['chips'] += pot
        print(winner)
        break

    player_id += 1
    if player_id >= len(players):
        player_id = 0






'''
ew, dice
    randomizer

gameplay
    who goes first?
    each player
        roll -- # of dice = number of chips (up to three dice)
        resolve roll
        pass chips depending on roll
        turn over
    
    check if game is over
        who wins?

'''




