"""
Lab 9: break an amount into quarters, dimes, nickles, pennies
"""

# version 1: the user will enter something like 136, representing $1.36
# amount = input('enter the total amount, in pennies: ')

# version 2: the user will enter something like 1.36
amount = input('enter the amount: $')
amount = int(float(amount)*100)  # convert it to pennies

n_quarters = amount // 25
amount -= n_quarters*25

n_dimes = amount // 10
amount -= n_dimes*10

n_nickles = amount // 5
amount -= n_nickles*5

n_pennies = amount

print('quarters: ' + str(n_quarters))
print('dimes: ' + str(n_dimes))
print('nickles: ' + str(n_nickles))
print('pennies: ' + str(n_pennies))
