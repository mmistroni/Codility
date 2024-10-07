from give_me_data import has_permission
import unittest
SAMPLE_TESTS = [
    ({'books_allow', 'movies_deny'}, 'movies', False),
    ({'books_allow', 'movies_deny'}, 'books', True),
    ({'*_allow', 'books_allow', 'movies_deny'}, 'games', True),
    ({'*_allow', '*_deny'}, 'movies', False),
    ({'*_deny', '*_allow'}, 'movies', False),
    (set(), 'movies', False)
]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        for user_info, accessing_data, result in SAMPLE_TESTS:
            print(f'{user_info} - {accessing_data} = {result}')
            self.assertEquals(result, has_permission(user_info, accessing_data))
if __name__ == '__main__':
    unittest.main()
