
# Lab: Tree

A tree is a type of data structure, one that represents a hierarchy. Try running the code below and implement the following functions.

- `count_leaves(node)` returns the number of leaves
- `rename_leaves(node, to_find, to_replace)` finds leaves with the name `to_find` and replaces their name with `to_replace`.



```python
import random

names = ['virginia', 'christine', 'carl', 'lillian']


def generate_tree(depth):
    n_children = int(random.random()*10/depth)
    if n_children == 0:
        return {'type': 'leaf', 'name': random.choice(names)}
    cell = {'type': 'branch', 'children': []}
    for i in range(n_children):
        child = generate_tree(depth+1)
        cell['children'].append(child)
    return cell


def print_node(cell, indentation):
    if cell['type'] == 'leaf':
        print(indentation + cell['name'])
    else:
        print(indentation + '-')
        for i in range(len(cell['children'])):
            print_node(cell['children'][i], indentation + '\t')


# count all trees and branches
def count_nodes(cell):
    if cell['type'] == 'leaf':
        return 1
    r = 1
    for i in range(len(cell['children'])):
        r += count_nodes(cell['children'][i])
    return r


root = generate_tree(1)
print_node(root, '')
print(count_nodes(root))
```




