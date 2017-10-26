
import random


class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []
        self.board = []
        for j in range(height):
            row = []
            for i in range(width):
                row.append(' ')
            self.board.append(row)

    def random_location(self):
        i = random.randint(0, self.width-1)
        j = random.randint(0, self.height-1)
        return i, j

    def random_location_unique(self):
        while True:
            i, j = self.random_location()

            # for entity in self.entities:
            #     if entity.loc_i == i and entity.loc_j == j:
            #         break
            # else:
            #     return i, j

            unique = True
            for entity in self.entities:
                if entity.loc_i == i and entity.loc_j == j:
                    unique = False
                    break
            if unique:
                return i, j

    def find_entities(self, loc_i, loc_j):
        r = []
        for entity in self.entities:
            if entity.loc_i == loc_i and entity.loc_j == loc_j:
                r.append(entity)
        return r

    def draw(self):
        for j in range(self.height):
            for i in range(self.width):
                entities = self.find_entities(i, j)
                if len(entities) == 0:
                    print(self.board[j][i], end='')
                else:
                    print(entities[0].symbol, end='')
            print()

















