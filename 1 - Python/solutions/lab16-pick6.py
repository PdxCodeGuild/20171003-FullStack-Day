"""
lab 16: pick 6
"""

import random


def pick6():
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket


def calc_payout(ticket, winners):

    n_matches = 0
    for i in range(6):
        if ticket[i] == winners[i]:
            n_matches += 1

    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    return payout[n_matches]


def main():
    winners = pick6()
    earnings = 0
    expenses = 0
    for i in range(100000):
        ticket = pick6()
        expenses += 2
        earnings += calc_payout(ticket, winners)
    balance = earnings-expenses
    roi = balance/expenses
    print('earnings: $'+str(earnings))
    print('expenses: $'+str(expenses))
    print('balance: $'+str(balance))
    print('ROI: '+str(roi))


main()
