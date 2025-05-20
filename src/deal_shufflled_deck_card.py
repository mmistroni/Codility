#https://www.codewars.com/kata/5810ad962b321bac8f000178/train/python
import random 
suits = ['H', 'C', 'D', 'S']

cards = range(1, 14)

DECK = [f"{suit} {value}" for suit in suits for value in cards]


def shuffled_deck():
    # your smart code here
    return random.sample(DECK, len(DECK))
    