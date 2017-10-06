"""
Lab 12: a simple REPL calculator
"""

while True:
    op = input('enter the operator (or \'done\') if done: ')
    if op == 'done':
        break
    else:
        num1 = float(input('what is the first number? '))
        num2 = float(input('what is the second number? '))
        if op == '+':
            print(num1+num2)
        elif op == '-':
            print(num1-num2)
        elif op == '*':
            print(num1*num2)
        elif op == '/':
            print(num1/num2)
