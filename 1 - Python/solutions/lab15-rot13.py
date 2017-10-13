"""
lab 15: rot 13
"""

# start with a blank output string
# loop through every character of the string that the user entered
# find the index of that character in the alphabet
# using that index, find the character in the rotated alphabet
# append that character to the output string


def rot13(text):

    alphabet         = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'

    output = ''
    for char in text:
        index = alphabet.find(char)
        output += alphabet_rotated[index]
    return output


def rotn(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n

        while index >= len(alphabet):
            index -= len(alphabet)

        #if index >= len(alphabet):
        #    index -= len(alphabet)
        output += alphabet[index]
    return output

# print(rotn('hello', 2))


# add support for non-letter characters
# use the modulus operator to wrap the index around
def rotn_v2(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            output += char
        else:
            index += n
            index %= len(alphabet)
            output += alphabet[index]
    return output

print(rotn_v2('hello world!', 13))