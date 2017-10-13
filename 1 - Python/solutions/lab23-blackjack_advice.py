
def card_value(card):
    if card == 'A':
        return 1
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    return int(card)


def main():
    card1 = input('what is your first card? ')
    card2 = input('what is your second card? ')
    card3 = input('what is your third card? ')

    total = card_value(card1) + card_value(card2) + card_value(card3)
    if total < 17:
        print('hit!')
    elif total < 21:
        print('stay!')
    elif total == 21:
        print('blackjack!')
    else:
        print('busted!')

main()