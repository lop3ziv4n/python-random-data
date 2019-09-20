import random

deck = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
        'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
        'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
        'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS']

# clone
deck2 = deck[:]
print(deck2)

# set shuffle
random.shuffle(deck2)
print(deck2)

#######
words = ['rabbit', 'horse', 'goat', 'bear', 'chicken']
print(words)

ls_words = [list(w) for w in words]
print(ls_words)

for w in ls_words:
    random.shuffle(w)

scrambled_words = [''.join(w) for w in ls_words]
print(scrambled_words)

