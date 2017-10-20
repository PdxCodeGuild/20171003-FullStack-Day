

def one_hop(city, city_graph):
    return city_graph[city]


def two_hops(city, city_graph):
    two_hop_cities = set()
    for one_hop_city in city_graph[city]:
        two_hop_cities.update(city_graph[one_hop_city])
    return two_hop_cities


def n_hops_iterative(n, city, city_graph):
    city_set = city_graph[city].copy()
    for i in range(n-1):
        temp_city_set = set()
        for temp_city in city_set:
            temp_city_set.update(city_graph[temp_city])
        city_set = temp_city_set
    return city_set


def n_hops_recursive(n, city, city_graph):
    if n == 1:
        return city_graph[city]
    accumulated_cities = set()
    for next_city in city_graph[city]:
        next_city_set = n_hops_recursive(n-1, next_city, city_graph)
        accumulated_cities.update(next_city_set)
    return accumulated_cities


'''
def n_hops_distance(n, city, city_graph):
    solution = {}
    n_hops_distance_recurse(n, city, solution, city_graph)
    return solution

def n_hops_distance_recurse(n, city, solution, city_graph):
    if n == 0:
        return
    next_cities = city_graph[city]
    for next_city in next_cities:
        distance = next_cities[next_city]
        if next_city in solution:
'''


def set_to_str(s):
    s = list(s)
    s.sort()
    return ', '.join(s)





def main():

    city_graph = {
        'Boston': {'New York', 'Albany', 'Portland'},
        'New York': {'Boston', 'Albany', 'Philadelphia'},
        'Albany': {'Boston', 'New York', 'Portland'},
        'Portland': {'Boston', 'Albany'},
        'Philadelphia': {'New York'}
    }

    city_graph_weighted = {
        'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
        'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
        'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
        'Portland': {'Boston': 3, 'Albany': 7},
        'Philadelphia': {'New York': 9},
    }

    print(', '.join(list(city_graph.keys())))
    city = input('enter a city: ')
    print('one hop: ' + set_to_str(one_hop(city, city_graph)))
    print('two hops: ' + set_to_str(two_hops(city, city_graph)))
    print()

    n_hops = int(input('enter the number of hops: '))
    print('n-hops iterative: ' + set_to_str(n_hops_iterative(n_hops, city, city_graph)))
    print('n-hops recursive: ' + set_to_str(n_hops_recursive(n_hops, city, city_graph)))


main()








