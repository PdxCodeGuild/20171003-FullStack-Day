"""
Lab 7: generate a random password
"""

import random

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJK@$%#^'

password = ''
i = 0
while i < 20:
    password += random.choice(alphabet)
    i = i + 1
print(password)

# alternatively, use a for-loop instead of a while-loop
# for i in range(20):
#     password += random.choice(alphabet)
# print(password

