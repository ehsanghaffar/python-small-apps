# Python Program to Shuffle Deck of Cards

import itertools, random

# Create a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
  print(deck[i][0], "of", deck[i][1])