"""  
Given a function that generates perfectly random numbers between 1 and k (inclusive), 
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

from random import randint


def shuffleDeck(deck):
    shuffledDeck = deck.copy()
    deckSize = len(deck)
    for i in range(0, deckSize - 1):
        swapIdx = randint(i, deckSize - 1)
        shuffledDeck[i], shuffledDeck[swapIdx] = shuffledDeck[
            swapIdx], shuffledDeck[i]

    return shuffledDeck


deck = [n for n in range(52)]

print(shuffleDeck(deck))
