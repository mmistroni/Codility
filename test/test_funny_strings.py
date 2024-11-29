import unittest
from src.funny_strings import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
        s = 'lmnop'
        self.assertEqual("Funny", solution(s))

    def test_something2(self):
        s = 'acxz'
        self.assertEqual("Funny", solution(s))

    def test_something3(self):
        s = 'bcxz'
        self.assertEqual("Not Funny", solution(s))


    def test_something4(self):
        s = 'ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq'
        self.assertEqual("Not Funny", solution(s))

    def test_something5(self):
        s = 'holtm'
        self.assertEqual("Funny", solution(s))

    def test_something6(self):
        s = 'uvzxrumuztyqyvpnji'
        self.assertEqual("Funny", solution(s))

    def test_something7(self):
        s = '10'
        self.assertEqual("Funny", solution(s))


''''
10
ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq
holtm
uvzxrumuztyqyvpnji
tmruzxzuwoskqysxztuvosuyrswrnmtxvzsrqwytzrxpltrwusxupw
wxstwxuzuyuvyzrsxysxyuvyqxuxyskqwsyqumqrvopvowqumnvrxpwqpwsrnvrztxrxpvuxunvyzvupvupowvyzvzuzwvsrwv
yrzxrxskrtlpwpmtpxvowrxrpxq
pryumtuntmovpwvowslj
nosklrxrtyuxtmnurzsryuxtywqwqpxts
fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury
jkmsxzwrxzy

Funny
Not Funny
Funny
Funny
Funny
Not Funny
Funny
Not Funny
Not Funny
Not Funny

'''


if __name__ == '__main__':
    unittest.main()
