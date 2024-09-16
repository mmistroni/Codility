
from like_or_dislike import  like_or_dislike, Test
import unittest


class MyTestCase(unittest.TestCase):

    def test_fixed_tests(self):
        self.assertEquals(like_or_dislike([Test.Dislike]), Test.Dislike)
        self.assertEquals(like_or_dislike([Test.Like, Test.Like]), Test.Nothing)
        self.assertEquals(like_or_dislike([Test.Dislike, Test.Dislike]), Test.Nothing)
        self.assertEquals(like_or_dislike([Test.Like, Test.Like, Test.Like]), Test.Like)
        self.assertEquals(like_or_dislike([Test.Like, Test.Dislike]), Test.Dislike)
        self.assertEquals(like_or_dislike([Test.Dislike, Test.Like]), Test.Like)
        self.assertEquals(like_or_dislike([Test.Like, Test.Dislike, Test.Dislike]), Test.Nothing)
        self.assertEquals(like_or_dislike([Test.Dislike, Test.Like, Test.Dislike]), Test.Dislike)
        self.assertEquals(like_or_dislike([Test.Like, Test.Like, Test.Dislike,
                                           Test.Like, Test.Like, Test.Like, Test.Like, Test.Dislike]),
                                            Test.Dislike)
        self.assertEquals(like_or_dislike([]), Test.Nothing)
        