

# lab 4 -----------------------------------------------

def letter_grade(number_grade):
    if number_grade >= 90:
        return 'A'
    elif number_grade >= 80:
        return 'B'
    elif number_grade >= 70:
        return 'C'
    elif number_grade >= 60:
        return 'D'
    else:
        return 'F'

number_grade = int(input('what is the number grade? '))
print(letter_grade(number_grade))


# lab 5 ------------------------------------------------


import random


def shake_magic_8_ball():
    responses = ['Yes', 'Outlook not so good', 'Certainly', 'Without a doubt', 'Ask again later']
    return random.choice(responses)


question = input('what is your question? ')
response = shake_magic_8_ball()
print(response)


# lab 6 -------------------------------------------------


def create_emoticon():

    list_eyes = [':', '=', ';']
    list_noses = ['', '-', '\'', '^', '+']
    list_mouths = [')', ']', '|', '/', '\\', 'D', 'P', '3']

    eyes = random.choice(list_eyes)
    nose = random.choice(list_noses)
    mouth = random.choice(list_mouths)

    emoticon = eyes + nose + mouth

    return emoticon

n_emoticons = int(input('how many emoticons would you like to see? '))
for i in range(n_emoticons):
    emoticon = create_emoticon()
    print(emoticon)


# lab 7 ----------------------------------------------------

def random_password(n_letters):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJK@$%#^'
    password = ''
    for i in range(n_letters):
        password += random.choice(alphabet)
    return password

n_letters = int(input('how many letters would you like your password to be? '))
print(random_password(n_letters))


# lab 11 ---------------------------------------------


def average_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)


print(average_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
