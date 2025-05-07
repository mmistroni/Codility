from src.rhinestone_cowboy import cowboys_dollars
import unittest
import math

class MyTestCase(unittest.TestCase):
    def test_one(self):
        left ='''
    ,|___|,
    |[(1)]|
    |     |
    |[(1)]|
    | ==  |
    |[(1)]|
    /    &|
    .-'`  ,   )****
    |         |   **
    `~~~~~~~~~~    ^'''
        right ='''
    ,|___|,
    |[(1)]|
    |     |
    |[(1)]|
    | ==  |
    |[(1)]|
    /    &|
    .-'`  ,   )****
    |         |   **
    `~~~~~~~~~~    ^'''
        boots = [left, right]
        
        self.assertEqual(cowboys_dollars(boots),'This Rhinestone Cowboy has 3 dollar bills in his right boot and 3 in the left' )
    
    def test_two(self):
    
        left ='''
    ,|___|,
    |[(1)]|
    |     |
    |[(1)]|
    | ==  |
    |[(1)]|
    /    &|
    .-'`  ,   )****
    |         |   **
    `~~~~~~~~~~    ^'''
        right ='''
    ,|___|,
    |[(1)]|
    |     |
    |[(1)]|
    | ==  |
    |[(1)]|
    /    &|
    .-'`  ,   )****
    |[(1)]    |   **
    `~~~~~~~~~~    ^'''
        boots = [left, right]
        self.assertEqual(cowboys_dollars(boots),'This Rhinestone Cowboy has 3 dollar bills in his right boot and 3 in the left' )

    def test_three(self):
    
        left ='''
    ,|___|,
    |[{1}]|
    |[{1}]|
    |[{1}]|
    | ==  |
    |[{1}]|
    /    &|
    .-'`  ,   )****
    |[{1}]    |   **
    `~~~~~~~~~~    ^'''
        right ='''
    ,|___|,
    |[(5)]|
    |[(5)]|
    |[(5)]|
    | ==  |
    |[(5)]|
    /    &|
    .-'`  ,   )****
    |[(5)]    |   **
    `~~~~~~~~~~    ^'''
        boots = [left, right]
        self.assertEqual(cowboys_dollars(boots),'This Rhinestone Cowboy has 0 dollar bills in his right boot and 0 in the left' )

    def test_four(self):
    
        left ='''
    ,|___|,
    |     |
    |     |
    |[(1)]|
    | ==  |
    |[(1)]|
    /    &|
    .-'`  ,   )****
    |         |   **
    `~~~~~~~~~~    ^'''
        right ='''
    ,|___|,
    |[(1)]|
    |     |
    |[(1)]|
    | ==  |
    |[(1)]|
    /    &|
    .-'`  ,   )****
    |[(1)]    |   **
    `~~~~~~~~~~    ^'''
        boots = [left, right]
        self.assertEqual(cowboys_dollars(boots),'This Rhinestone Cowboy has 3 dollar bills in his right boot and 2 in the left' )

    