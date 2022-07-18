import unittest
from Codility.src.guru import Guru, NlpEngine

class TestGuru(unittest.TestCase):

    def test_ask(self):
        guru: Guru = Guru()
        # note these values may change a little as time moves on
        self.assertEqual('68', guru.ask('how old is Tony Blair'))
        self.assertEqual('75', guru.ask('how old is trump'))
        self.assertEqual('8908081', guru.ask('what is the population of London'))
        self.assertEqual('2175601', guru.ask('what is the population of Paris'))

    def test_result(self):
        e = NlpEngine()
        res = e.buildSparqlQuery('how old is Tony Blair')
        print(res)

    def test_object(self):
        e = NlpEngine()
        qry = 'how old is Tony Blair'
        res = e._extractObject(qry, 'is')
        print(res)

    def test_object2(self):
        e = NlpEngine()
        qry = 'what is the population of Paris'
        res = e._extractObject(qry, 'of')
        print(res)

    def testGuru1(self):
        guru: Guru = Guru()
        # note these values may change a little as time moves on
        self.assertEqual('68', guru.ask('how old is Tony Blair'))

    def testGuru2(self):
        guru: Guru = Guru()
        # note these values may change a little as time moves on
        self.assertEqual('68', guru.ask('what is the population of Paris'))


if __name__ == '__main__':
    unittest.main()
