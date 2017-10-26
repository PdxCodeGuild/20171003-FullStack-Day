
from world import World
from entities import Player, Skeleton


world = World(10, 10)

player_i, player_j = world.random_location()
player = Player(player_i, player_j)
world.entities.append(player)

for i in range(10):
    skeleton_i, skeleton_j = world.random_location()
    skeleton = Skeleton(skeleton_i, skeleton_j)
    world.entities.append(skeleton)


while True:
    world.draw()
    command = input('what is your command? ').lower()
    if command in ['done', 'quit', 'exit']:
        break
    if command in ['l', 'left', 'w', 'west']:
        player.loc_i -= 1
    elif command in ['r', 'right', 'e', 'east']:
        player.loc_i += 1
    elif command in ['u', 'up', 'n', 'north']:
        player.loc_j -= 1
    elif command in ['d', 'down', 's', 'south']:
        player.loc_j += 1
    else:
        print('command not recognized')






