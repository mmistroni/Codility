from src.give_me_data import has_permission
import unittest
SAMPLE_TESTS = [
    ({'books_allow', 'movies_deny'}, 'movies', False),
    ({'books_allow', 'movies_deny'}, 'books', True),
    ({'*_allow', 'books_allow', 'movies_deny'}, 'games', True),
    ({'*_allow', '*_deny'}, 'movies', False),
    ({'*_deny', '*_allow'}, 'movies', False),
    (set(), 'movies', False),
    ({'books_allow', '*_allow', '*_deny', 'movies_deny'}, 'books', True),
    ({'movies_allow', '*_deny', 'movies_deny', '*_allow'}, 'movies', False),
    ( {'books_allow', 'books_deny'}, 'games', False),
    ( {'movies_allow', 'movies_deny'}, 'books', False)

]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        for user_info, accessing_data, result in SAMPLE_TESTS:
            print(f'U:{user_info} - A:{accessing_data} = {result}')
            self.assertEquals(result, has_permission(user_info, accessing_data))

    def test_somethign2(self):

        tpl  = ({'books_allow', 'movies_deny'}, 'books', True)
        u, a, r = tpl

        self.assertEquals(r, has_permission(u, a))


if __name__ == '__main__':
    unittest.main()
