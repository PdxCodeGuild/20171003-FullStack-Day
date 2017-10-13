# lab 19: palindrome + anagram

# Part 1: check if the user's string is a palindrome (e.g. 'racecar')
# we first compare the first and last letters
# then we compare the second and the second-to-last letters
# and so on, comparing each half to the other half
# if any of our checks fail, return false
# if all our tests succeed, return true


def check_palindrome(string):
    half_len = len(string) // 2 #loop through half the string
    for i in range(half_len):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

user_input = input('what is your word? ') #get the word from the user
print(check_palindrome(user_input)) #show the user the result of check_palindrome


# detect whether two words are anagrams of eachother
# 1) get two words from user
# 2) convert to lowercase
# 3) remove all spaces (replace ' ' with '')
# 4) sort the letters (sorted)
# 5) check if they're equal

def convert_word(word):
    word = word.lower()
    word = word.replace(' ', '')
    word = str(sorted(word))
    return word

#word1 = input('what is the first word? ')
#word2 = input('what is the second word? ')
word1 = 'anagram'
word2 = 'nag a ram'
print('word 1: '+word1)
print('word 2: '+word2)
if convert_word(word1) == convert_word(word2):
    print('those are anagrams!')
else:
    print('those are not anagrams')



