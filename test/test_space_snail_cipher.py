import unittest
from src.space_snail_cipher import encode, decode

"""
Description:
verview
Spaced Snail Cipher is a variation of spiral transposition ciphers, where the characters of a plaintext are placed along a spiral path and then read row by row.

Encoding
The spiral always starts at the center, and the key determines the spiral arrangement.

The key consists of:

The first digit
This digit determines the orientation of the spiral.
There are 8 unique orientations, so the digit will range from 1-8 (inclusive)
Click to show spiral orientations
The second digit
This digit determines the width of the gap formed by the spiral.
This digit ranges from 0 to 9 (inclusive)
Click to show visual example of spiral gaps
Sign
The sign of the key determines the direction of the string arrangement
If the key is positive, the characters will be arranged center-out
If the key is negative, the characters will be arranged outside-in
Example :
string = '123456789ABCDE'

  Positive key              Negative key            

    7654                     89AB
    8  3                     7  C
    9 12                     6 ED
    A                        5
    BCDE                     4321
  
Some key examples :

-10 : orientation 1 (down from center, clockwise), no gaps, outside-in arrangement.
62 : orientation 6 (up from center, counterclockwise), gap width 2, center-out arrangement.
After the spiral is determined :

Place each character of the plaintext along the spiral path according to the direction specified by the key.
Read the resulting layout row by row (top to bottom, left to right) to get the cipher text.
Any empty cells created by the gaps are not included in the cipher text.
Task
Implement two functions :

encode(plaintext,key)
decode(cipher,key)
encode should return the cipher text after placing the plaintext along the spiral path and reading it row by row.

decode should return the original plaintext using the same key used during encoding.

Input specification:

5 <= message length <= 1000
All keys are valid



"""

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(zeros(1), 2)

    def test_two(self):
        self.assertEqual(zeros(2), 2)

    def test_three(self):
        self.assertEqual(zeros(3), 3)
    
    def test_big_n(self):
        n = 10**4
        res = zeros(n)
        print(f'{n} == {res}')
        


if __name__ == '__main__':
    unittest.main()
