
import random


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for i in range(self.height):
            self.board.append([])
            for j in range(self.width):
                self.board[i].append(' ')

    def draw(self, entities, player):
        for i in range(self.height):
            for j in range(self.width):
                d = abs(player.location_i - i) + abs(player.location_j - j)
                visibility = 5
                if 'torch' in player.inventory:
                    visibility = 10
                if d < visibility:
                    for k in range(len(entities)):
                        if i == entities[k].location_i and j == entities[k].location_j:
                            print(entities[k].character, end='')
                            break
                    else:
                        print(' ', end='')
                else:
                    print('#', end='')
            print()


class Entity:
    def __init__(self, name, character, location_i, location_j):
        self.name = name
        self.character = character
        self.location_i = location_i
        self.location_j = location_j


class LivingEntity(Entity):
    def __init__(self, name, character, location_i, location_j, health):
        super(LivingEntity, self).__init__(name, character, location_i, location_j)
        self.health = health


class Item(Entity):
    def __init__(self, name, character, location_i, location_j):
        super(Item, self).__init__(name, character, location_i, location_j)


class Portal(Item):
    def __init__(self, location_i, location_j, portal_i, portal_j):
        super(Portal, self).__init__('portal', '֍', location_i, location_j)
        self.portal_i = portal_i
        self.portal_j = portal_j


class Player(LivingEntity):
    def __init__(self, location_i, location_j):
        super(Player, self).__init__('player', '☺', location_i, location_j, 10)
        self.inventory = {}

    def add_item_to_inventory(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1


def roll_die():
    return random.randint(1, 6)


def battle(player, enemy):
    print(f'you\'ve encountered an enemy!')
    print(f'your health is: {player.health}, enemy health is: {enemy.health}')
    while True:
        action = input('attack, run, play dead: what will you do? ')
        if action == 'run':
            return 'ran'
        if action == 'play dead':
            print('foolish move!')
            return 'death'
        if action == 'attack':
            player_die = roll_die()
            enemy_die = roll_die()
            print(f'player rolled {player_die}, enemy rolled {enemy_die}')
            if player_die == enemy_die:
                continue
            elif player_die > enemy_die:
                damage = player_die - enemy_die
                enemy.health -= damage
                if enemy.health < 0:
                    enemy.health = 0
            elif player_die < enemy_die:
                damage = enemy_die - player_die
                player.health -= damage
                if player.health < 0:
                    player.health = 0
            print(f'player health: {player.health}, enemy health: {enemy.health}')
            if player.health <= 0:
                return 'death'
            elif enemy.health <= 0:
                return 'won'


def standardize_command(command):
    command = command.lower().strip()
    if command in ['left', 'west', 'l', 'w']:
        return 'w'
    elif command in ['right', 'east', 'r', 'e']:
        return 'e'
    elif command in ['up', 'north', 'u', 'n']:
        return 'n'
    elif command in ['down', 'south', 'd', 's']:
        return 's'
    return command


def random_location(width, height):
    return random.randint(0, height - 1), random.randint(0, width - 1)


def ask_riddle():
    riddles = ['What flies without wings? ',
               'What goes through towns and over hills but never moves? ',
               'What has cities, but no houses; forests, but no trees; and water, but no fish? ']
    answers = ['time', 'a road', 'a map']
    riddle_id = random.randint(0, len(riddles)-1)
    answer = input(riddles[riddle_id]).lower().strip()
    return answer == answers[riddle_id]


def main():
    width = 60
    height = 30
    board = Board(width, height)
    player = Player(0, 0)
    entities = [player]

    enemies = []
    for i in range(4):
        enemy_i, enemy_j = random_location(width, height)
        enemy = LivingEntity('enemy', '§', enemy_i, enemy_j, 5)
        entities.append(enemy)
        enemies.append(enemy)

    for i in range(4):
        treasure_i, treasure_j = random_location(width, height)
        treasure = Item('gold', '҂', treasure_i, treasure_j)
        entities.append(treasure)


    for i in range(2):
        hp_i, hp_j = random_location(width, height)
        hp = Item('health pack', '+', hp_i, hp_j)
        entities.append(hp)

    for i in range(2):
        portal_i, portal_j = random_location(width, height)
        location_i, location_j = random_location(width, height)
        portal = Portal(location_i, location_j, portal_i, portal_j)
        portal2 = Portal(portal_i, portal_j, location_i, location_j)
        entities.append(portal)
        entities.append(portal2)

    for i in range(2):
        torch_i, torch_j = random_location(width, height)
        torch = Item('torch', '!', torch_i, torch_j)
        entities.append(torch)

    while True:
        board.draw(entities, player)
        #board.draw2(player, entities)
        command = input('what is your command? ')
        command = standardize_command(command)
        if command == 'help':
            print('list of commands:')
            print('\thelp: print this text')
        elif command == 'w':
            if player.location_j > 0:
                player.location_j -= 1
        elif command == 'e':
            if player.location_j < width-1:
                player.location_j += 1
        elif command == 'n':
            if player.location_i > 0:
                player.location_i -= 1
        elif command == 's':
            if player.location_i < height-1:
                player.location_i += 1
        elif command == 'inventory':
            for item in player.inventory:
                print(f'{item}: {player.inventory[item]}')
        else:
            print('did not recognize command \'' + command + '\'')

        for i in range(len(enemies)):
            if random.randint(0, 1) == 0:
                if random.randint(0, 1) == 0:
                    enemies[i].location_i += 1
                else:
                    enemies[i].location_i -= 1
            else:
                if random.randint(0, 1) == 0:
                    enemies[i].location_j += 1
                else:
                    enemies[i].location_j -= 1


        for i in range(len(entities)):
            if entities[i] is player:
                continue
            if player.location_i == entities[i].location_i \
                    and player.location_j == entities[i].location_j:
                if type(entities[i]) is Item:
                    if entities[i].name == 'gold':
                        if ask_riddle():
                            player.add_item_to_inventory(entities[i].name)
                            entities.pop(i)
                    else:
                        player.add_item_to_inventory(entities[i].name)
                        entities.pop(i)
                elif entities[i].name == 'enemy':
                    result = battle(player, entities[i])
                    if result == 'death':
                        print('you died!')
                        exit()
                    elif result == 'ran':
                        print('you\'re a coward, but alive!')
                    elif result == 'won':
                        print('triumph!!!!')
                        entities.pop(i)
                elif entities[i].name == 'portal':
                    player.location_i = entities[i].portal_i
                    player.location_j = entities[i].portal_j

                break

main()