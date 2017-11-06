'''

drop dead - dice game

'''
import random

# create dice, number of players, roll all 5 dice
# if any dice are 2 & 5, the whole roll is dead
# and those dice are discarded until the player has
# no dice left to roll.
# go through all of the players, and the player
# with the highest score wins.


num_players = 1000000 #int(input('How many players? '))

player_scores = []
player_rolls_counts = []
player_rolls = []
for i in range(num_players):
    #print(f'player {i}\'s turn')
    player_dice = 5
    player_score = 0
    player_roll_count = 0
    player_rolls.append([])
    while player_dice > 0:
        die_values = []
        for r in range(player_dice):
            die_values.append(random.randint(1, 6))
        #print('\t' + str(die_values))
        if 2 in die_values or 5 in die_values:
            player_dice -= die_values.count(2)
            player_dice -= die_values.count(5)
        else:
            player_score += sum(die_values)
        #print('\t' + str(player_score))

        player_roll_count += 1
        player_rolls[i].append(die_values)
    player_scores.append(player_score)
    player_rolls_counts.append(player_roll_count)
    if i%1000 == 0:
        print(f'{i/num_players*100}%')


winning_score = max(player_scores)
winner = player_scores.index(winning_score)
winning_rolls = player_rolls_counts[winner]

print(player_scores)
print(player_rolls_counts)
print(f'Player {winner} won with {winning_score} points and {winning_rolls} rolls')
print('winning rolls:')
for roll in player_rolls[winner]:
    print(roll)
print(f'{player_scores.count(0)} players got 0, it brought dishonor upon their respective houses... excellent')
print(f'{player_rolls_counts.count(1)} players lost on their first turn')

num_over_30 = 0
for score in player_scores:
    if score > 30:
        num_over_30 += 1
print(f'number of rolls over 30: {num_over_30}')
print(f'most rolls: {max(player_rolls_counts)}')

