
import random


def socks1a():

    sock_types = ['ankle', 'crew', 'calf', 'thigh']
    socks = []
    for i in range(100):
        sock = random.choice(sock_types)
        socks.append(sock)
    print(socks)

    pairs = {}
    unmatched = {}
    while len(socks) > 0:
        sock_to_match = socks.pop()
        for i in range(len(socks)):
            sock = socks[i]
            if sock == sock_to_match:
                socks.pop(i)
                if sock in pairs:
                    pairs[sock] += 1
                else:
                    pairs[sock] = 1
                break
        else:
            unmatched[sock_to_match] = 1

    print(pairs)
    print(unmatched)


def socks1b():
    sock_types = ['ankle', 'crew', 'calf', 'thigh']
    socks = []
    for i in range(100):
        sock = random.choice(sock_types)
        socks.append(sock)
    print(socks)

    pairs = {}
    unmatched = {}
    while len(socks) > 0:
        sock_to_match = socks.pop()
        try:
            ind = socks.index(sock_to_match)
            socks.pop(ind)
            if sock_to_match in pairs:
                pairs[sock_to_match] += 1
            else:
                pairs[sock_to_match] = 1
        except ValueError:
            unmatched[sock_to_match] = 1

    print(pairs)
    print(unmatched)


def socks2():
    sock_types = ['ankle', 'crew', 'calf']
    sock_colors = ['black', 'white']

    socks = []
    for i in range(20):
        random_type = random.choice(sock_types)
        random_color = random.choice(sock_colors)
        socks.append((random_type, random_color))

    pairs = {}
    unmatched = {}
    while len(socks) > 0:
        sock_to_match = socks.pop()
        try:
            ind = socks.index(sock_to_match)
            socks.pop(ind)
            if sock_to_match in pairs:
                pairs[sock_to_match] += 2
            else:
                pairs[sock_to_match] = 2
        except ValueError:
            unmatched[sock_to_match] = 1

    print(pairs)
    print(unmatched)




