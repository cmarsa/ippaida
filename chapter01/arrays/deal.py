# deal.py

# 1.4.8 Compose a program deal.py that takes a command-line argument n and
# writes n poker hands (five cards each) from a shuffled deck, separated
# by blank lines.

import random
import sys
import stdarray
import stdio

n = int(sys.argv[1])
if n > 10:
    raise ValueError, 'n must be 10 or less.'

SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']

# create deck
deck = []
for rank in RANKS:
    for suit in SUITS:
        card = rank + '-' + suit
        deck += [card]

# shuffle the deck several times
deck_length = len(deck)
for i in range(0, deck_length):
    r = random.randrange(i, deck_length)
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp

# draw cards
draw_index = 0
for i in range(0, n):
    for j in range(0, 5):
        stdio.write(deck[draw_index] + str(', '))
        draw_index += 1
    stdio.writeln()
