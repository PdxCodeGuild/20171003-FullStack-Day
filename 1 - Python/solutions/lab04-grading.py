"""
Lab 4: convert a number grade into a letter grade
"""

grade = int(input('what is the number grade? '))
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

