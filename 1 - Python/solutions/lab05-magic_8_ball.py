"""
Lab 5: this program simulates a magic 8-ball
"""

import random

responses = ['Yes', 'Outlook not so good', 'Certainly', 'Without a doubt', 'Ask again later']
question = input('what is your question? ')
response = random.choice(responses)
print(response)