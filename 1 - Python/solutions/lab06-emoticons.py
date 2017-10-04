"""
Lab 6: generate emoticons
"""

import random


def create_emoticon():

    list_eyes = [':', '=', ';']
    list_noses = ['', '-', '\'', '^', '+']
    list_mouths = [')', ']', '|', '/', '\\', 'D', 'P', '3']

    eyes = random.choice(list_eyes)
    nose = random.choice(list_noses)
    mouth = random.choice(list_mouths)

    emoticon = eyes + nose + mouth

    return emoticon


for i in range(10):
    print(create_emoticon())
