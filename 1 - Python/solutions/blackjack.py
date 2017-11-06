
"""
Black Jack program
"""
import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def value(self):
        if self.rank == 'A':
            return 1
        elif self.rank in ['J', 'Q', 'K']:
            return 10
        return int(self.rank)




class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                # print(suit + ' - ' + rank)
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        random.shuffle(self.cards)

    def cut(self):
        cut_point = random.randint(4, 46)
        top_cards = self.cards[:cut_point]
        bottom_cards = self.cards[cut_point:]
        bottom_cards.extend(top_cards)
        self.cards = bottom_cards

        # cut_point = random.randint(4, 46)
        # temp = []
        # for i in range(cut_point, len(self.cards)):
        #     temp.append(self.cards[i])
        # for i in range(0, cut_point):
        #     temp.append(self.cards[i])
        # self.cards = temp

    def __len__(self):
        return len(self.cards)

    def draw_card(self):
        return self.cards.pop(0)


class Hand:
    def __init__(self):
        self.cards = []

    #add card to hand
    def in_hand(self, card):
        self.cards.append(card)

    def print_cards(self):
        for card in self.cards:
            print(card)

    def hand_value(self):
        hand_total = 0
        for card in self.cards:
            hand_total += card.value()
        return hand_total


deck = Deck()
deck.shuffle()
deck.cut()

#init hand, draw two cards
hand = Hand()
card = deck.draw_card()
hand.in_hand(card)
card = deck.draw_card()
hand.in_hand(card)
hand.print_cards()
print(hand.hand_value())

command = input('Hit or stay?').lower()
if command == 'hit':
    card = deck.draw_card()
    hand.in_hand(card)
    hand.print_cards()
    print(hand.hand_value())

print('deck ' + '-'*40)
for card in deck.cards:
    print(card)

# print('hand ' + '-'*40)
# for card in hand.cards:
#     print(card)




