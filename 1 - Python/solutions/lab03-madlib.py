"""
Lab 3: Mad Lib
give a series of words, generate a silly sentence
  "_____________! he said ________ as he jumped into his convertible
    exclamation            adverb
   ______ and drove off with his __________ wife."
    noun                          adjective
"""



# get words from the user
exclamation = input('give me an exclamation! ')
adverb = input('give me a verb: ')
noun = input('give me a noun: ')
adjective = input('give me an adjective: ')

# putting together the words into an output
output = exclamation + '! he said ' + adverb + ' as he jumped into his convertible '
output += noun + ' and drove off with his ' + adjective + ' wife.'

# alternatively, use an f-string
output = f'{exclamation}! he said {adverb} as he jumped into his convertable {noun} and drove off with his {adjective} wife'

# print the output
print(output)

