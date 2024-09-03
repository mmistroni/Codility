import codewars_test as test
from like_or_dislike import  import like_or_dislike
from preloaded import Like, Dislike, Nothing

@test.describe("Fixed tests")
def fixed_tests():
    @test.it('Basic Tests')
    def _():
        test.assert_equals(like_or_dislike([Dislike]), Dislike, repr([Dislike]))
        test.assert_equals(like_or_dislike([Like, Like]), Nothing, repr([Like, Like]))
        test.assert_equals(like_or_dislike([Dislike, Dislike]), Nothing, repr([Dislike, Dislike]))
        test.assert_equals(like_or_dislike([Like, Like, Like]), Like, repr([Like, Like, Like]))
        test.assert_equals(like_or_dislike([Like, Dislike]), Dislike, repr([Like, Dislike]))
        test.assert_equals(like_or_dislike([Dislike, Like]), Like, repr([Dislike, Like]))
        test.assert_equals(like_or_dislike([Like, Dislike, Dislike]), Nothing, repr([Like, Dislike, Dislike]))
        test.assert_equals(like_or_dislike([Dislike, Like, Dislike]), Dislike, repr([Dislike, Like, Dislike]))
        test.assert_equals(like_or_dislike([Like, Like, Dislike, Like, Like, Like, Like, Dislike]), Dislike, repr([Like, Like, Dislike, Like, Like, Like, Like, Dislike]))
        test.assert_equals(like_or_dislike([]), Nothing, repr([]))