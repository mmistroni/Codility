from modulefinder import test
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
from src.space_snail_cipher import encode,decode
#

cipher_orientation = (('HelloWorld',10,'oWolHrleld'),
                      ('HelloWorld',20,'oWorHlleld'),
                      ('HelloWorld',30,'orldWHeoll'),
                      ('HelloWorld',40,'ollWHeorld'),
                      ('HelloWorld',50,'dlelrHloWo'),
                      ('HelloWorld',60,'dlellHroWo'),
                      ('HelloWorld',70,'lloeHWdlro'),
                      ('HelloWorld',80,'dlroeHWllo'),
                      ('Tis a perfect code',10,'deoa pc Te sirtcef'),
                      ('Tis a perfect code',20,'edp aoeT cris fect'),
                      ('Tis a perfect code',30,'perf Tieea scdoc t'),
                      ('Tis a perfect code',40,'doc tea sc Tieperf'),
                      ('Tis a perfect code',50,'fectris eT cp aoed'),
                      ('Tis a perfect code',60,'tcef sirc Teoa pde'),
                      ('Tis a perfect code',70,'t codcs aeeiT frep'),
                      ('Tis a perfect code',80,'frepeiT cs aet cod'),
                      ('immunoelectrophoretically',10,'reticonoeahuillpmmelortcy'),
                      ('immunoelectrophoretically',20,'citeraeonolliuhlemmpyctro'),
                      ('immunoelectrophoretically',30,'callyielectoimtenumrrohpo'),
                      ('immunoelectrophoretically',40,'rohpoenumrtoimtieleccally'),
                      ('immunoelectrophoretically',50,'yctrolemmplliuhaeonociter'),
                      ('immunoelectrophoretically',60,'ortcypmmelhuillonoearetic'),
                      ('immunoelectrophoretically',70,'ophorrmunetmiotceleiyllac'),
                      ('immunoelectrophoretically',80,'yllacceleitmiotrmuneophor'))

cipher_inward = (('Fluffy Bunny',-10,'B yuyfnnfFlu'),
                 ('Groovy',-20,'Gryovo'),
                 ('absolute leprosy',-30,'l eteysuprolabso'),
                 ('I am Groot',-40,'Gro toma I'),
                 ('Nothing Beats a Jet2 Holiday!',-50,'htoNi2teJn ya gH!da oli Beats'),
                 ('To be, or not to be?',-60,'or n beo, ?teot b oT'),
                 ('Hi Hungry! I\'m Dad!',-70,'gnuH raD iyd!mH! I\''),
                 ('Galvanized Square Steel',-80,'Galuarevqel aSetSn dezi'))

cipher_gaps = (('Supercalifragilisticexpialidocious',10,'sticeircaxsleSlpuipuiiogarfaicodil'),
               ('Supercalifragilisticexpialidocious',11,'usoiifragclioaSldcuiirepsltaipxeci'),
               ('Supercalifragilisticexpialidocious',12,'gilistiacrefSxiuplpiacrealisuoicod'),
               ('Supercalifragilisticexpialidocious',13,'sticexpiailliidgSoaucrpifeoilacrus'),
               ('Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long',14,
                'opicsilicovcoslocgrancPnoinolmec auosrmnrtluonoieotstiesl evif-ytrof si '),
               ('Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long',15,
                'silicovolcanocciopnoicosPsonirescu imimosartluon fortygnol srettel evif-'),
               ('Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long',16,
                'covolcanoconiosiilsi sicsi pPfonocersutomyro-cnfimartluoive letgnol sret'),
               ('Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long',17,
                'lcanoconiosis is ofvoorctiyl-ifsPicnvieepu omlcoesntootrcimartluers long'),
               ('Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long',18,
                'oconiosis is forty-nfaicvleo vloectiPtlneiersuscm iolpnoooncugsorcimartl'),
               ('Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long',19,
                'iosis is forty-five lneotctoenrasc lloovPnongceiulmiosncoiuplocsorcimart'))

cipher_mix = (('aibohphobia',32,'aibohpaiboh'),
              ('Squirrel in My Pants',-60,'l inent rasMrP yiuqS'),
              ('Diamond Under Pressure',-21,'nder UP erdrenussomaiD'),
              ('Pop Goes the Weasel!',67,'saeW eht esle!oG poP'),
              ('ILLEGALLY',-19,'YLLAGELLI'),
              ('Spooky Scary Skeleton!',74,'ry Skeletona!cS ykoopS'),
              ('Hey!! This is a Secret Message! You\'re not Supposed to Read This',-82,
               'Hey!! re not SupT\'phuoioThisssY e  ddi!aeR ot se gaasseM terceS '),
              ('Yummy Pen Pineapple Apple Pen and Baby Shark dodo dodo dodo',45,
               'elppA elppaen iPPe nn eaYummy Pndo dBoadby Shark dodo dodo '))

class MyTestCase(unittest.TestCase):


    def test_orientation_encode(self):
        for text,key,expected in cipher_orientation:
            self.assertEqual(encode(text,key),expected, msg=f'Input : "{text}", {key}')

    def test_direction_encode(self):
        for text,key,expected in cipher_inward:
            self.assertEqual(encode(text,key),expected, msg=f'Input : "{text}", {key}')

    def test_gap_encode(self):
        for text,key,expected in cipher_gaps:
            self.assertEqual(encode(text,key),expected, msg=f'Input : "{text}", {key}')


    def test_mix_encode(self):
        for text,key,expected in cipher_mix:
            self.assertEqual(encode(text,key),expected, msg=f'Input : "{text}", {key}')

    def test_orientation_decode(self):
        for expected,key,text in cipher_orientation:
            self.assertEqual(decode(text,key),expected, msg=f'Input : "{text}", {key}')

    def test_direction_decode(self):
        for expected,key,text in cipher_inward:
            self.assertEqual(decode(text,key),expected, msg=f'Input : "{text}", {key}')

    def test_gap_decode(self):
        for expected,key,text in cipher_gaps:
            self.assertEqual(decode(text,key),expected, msg=f'Input : "{text}", {key}')

    def test_mix_decode(self):
        for expected,key,text in cipher_mix:
            self.assertEqual(decode(text,key),expected, msg=f'Input : "{text}", {key}')
            

if __name__ == '__main__':
    unittest.main()
