import unittest
from reverse_inside_parenthesis import solution

def parsestr(runner, stack, acc):
    # Not good enough as we cannot trap anything
    input = runner[0] if runner else None
    if input == None:
        return stack
    if input == "(": # not quite right, h and  lo shold be mayb sampe container?
        acc = []
    elif input == ')':
        stack.append(acc)
        acc = None
    else:
        if acc is None:
            stack.append(input)
        else:
            acc.append(input)
    return parsestr(runner[1:], stack, acc)

    # Not good enough, we need to capture all parenthesis

class MyTestCase(unittest.TestCase):
    def test_something(self):
        teststr  = "h(el)lo"
        res = parsestr(teststr, [], None)

        # this is ok....

        print(res)
        #self.assertEquals(solution("h(el)lo)"), "h(le)lo")

    def test_two(self):
        teststr = "a (b c (d e))"
        res = parsestr(teststr, [], None)

        print(res)
        #self.assertEquals(solution("a ((d e) c b)") , "a (b c (d e))")

    def test_three(self):
        self.assertEqual(solution("one (two (three) four)"), "one (ruof (three) owt)")

    def test_four(self):
        self.assertEqual(solution("one (ruof ((rht)ee) owt)"), "one (two ((thr)ee) four)")

if __name__ == '__main__':
    unittest.main()
