# lab 24: count words
# count the number of occurances of each word using a dict

# 1) open a text file, looping through the lines (look back at lab 9)
# 2) loop over the lines
# 3) convert line to lower-case, strip punctuation, convert to list
# 4) add words from list to dictionary, incrementing the value if it already exists

import string


# returns a clean list of words for a line of text
def convert_line(line):
    line = line.strip()  # remove \n from end
    line = line.lower()
    word_list = line.split(' ')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip(string.punctuation)
    return word_list


word_set = {}

# http://www.gutenberg.org/cache/epub/32226/pg32226.txt
file_name = 'the_flower_princess.txt'
with open(file_name, 'r') as f:
    for line in f:
        word_list = convert_line(line)
        for word in word_list:

            if word == '':  # skip over empty string
                continue

            if word in word_set:  # 'if the word is in the dict'
                word_set[word] += 1  # increment the value of the entry of that word
            else:
                word_set[word] = 1  # add it to the dict



#for word in word_set:
#    if word_set[word] > 20:
#        print(word + ' ' + str(word_set[word]))


words = list(word_set.items())
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])