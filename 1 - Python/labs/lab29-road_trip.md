# Lab 29: Road Trip

We've mapped what cities are directly connected by roads and stored them in a dictionary:

```python
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
```

Traveling from one city to an adjacent one is called a **hop**. Let the user enter a city.
Print out all the cities connected to that city. Then print out all cities that could be reached through two hops.



## Version 2 (optional)

Let the user enter a city and a number of hops. Print out all cities that could be reached through that number of hops.

We've also mapped the travel time of each hop. When the user enters a city and a number of hops, print out the shortest travel times to each city. Paths with fewer hops are not necessarily those with the shorter travel times.

```python
city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}
```

