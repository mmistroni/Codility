from src.deal_shufflled_deck_card import shuffled_deck, suits, DECK
import unittest
import math

class MyTestCase(unittest.TestCase):
    def test1(self):
        deck1, deck2 = shuffled_deck(), shuffled_deck()
        self.assertEqual(len(set(deck1)), 52, "deck #1 should consist of 52 cards")
        self.assertEqual(len(set(deck2)), 52, "deck #2 should consist of 52 cards")
        self.assertEqual(sorted(deck1), sorted(deck2), "decks should contain the same cards")
        self.assertNotEqual(deck1, deck2, "decks should be shuffled")

    def test2(self):
        from pprint import pprint
        pprint(DECK)