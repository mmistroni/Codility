import unittest
from reverse_inside_parenthesis import solution

'''
In this kata, you will be given a string of text and valid parentheses, such as "h(el)lo". 
You must return the string, with only the text inside parentheses reversed, so "h(el)lo" becomes "h(le)lo". 
However, if said parenthesized text contains parenthesized text itself, then that too must reversed back, so it faces the original direction.
When parentheses are reversed, they should switch directions, so they remain syntactically correct (i.e. "h((el)l)o" becomes "h(l(el))o").
This pattern should repeat for however many layers of parentheses. 
There may be multiple groups of parentheses at any level (i.e. "(1) (2 (3) (4))"), so be sure to account for these.


'''



class Node:
    def __init__(self, parent):
        self.parent = parent
        self.holder = []

    def add(self, item):
        self.holder.append(item)

    def reverse(self):
        new_holder = []
        for item in self.holder:
            if isinstance(item, Node):
                item.reverse()
            new_holder.append(item)
        self.holder = new_holder[::-1]


    def __str__(self):
        return f"({''.join([str(i) for i in self.holder])})"

def buildstack(runner, stack):
    # Not good enough as we cannot trap anything
    # Not working yet, we need to build a stack, and we always add element to the top element of the stack
    # whenever we encounter an open parenthesis, we create a new container and put it on stack
    # whenever we encounter a close parenthesis, we go back to the parent. So mayb we need to keep track
    # of the last index.
    input = runner[0] if runner else None
    if input == None:
        return stack
    if input == "(": # not quite right, h and  lo shold be mayb sampe container?
        # we create a new accumulator
        node = Node(stack)
        stack.add(node)
        stack = node

    elif input == ')':
        # go back to original stack
        stack = stack.parent
    else:
        stack.add(input)


    return buildstack(runner[1:], stack)


def reverse(stack):
    holder = []
    for item in stack.holder:
        if isinstance(item, Node):
            item.reverse() # need new ideas.. 1 more week to think and then we move up to kyu 6
        holder.append(str(item))
    # Not good enough, we need to capture all parenthesis
    return holder

class MyTestCase(unittest.TestCase):
    def test_something(self):
        teststr  = "h(el)lo"
        stack = Node(None)
        res = buildstack(teststr, stack)

        # this is ok....

        print(res)

        result = reverse(res)

        print(result)

        joined = ''.join(result)

        self.assertEquals(joined, "h(le)lo")

    def test_two(self):
        # this is a good test to try

        teststr = "a (b c (d e))"
        stack = Node(None)

        res = buildstack(teststr, stack)

        print(res)

        reversed = reverse(res)

        print('-------------')
        print(reversed)

        # ['a', ' ', '((e d) c b)'] #

        # a ((d e) c b)
        # start from inner, reverse so that it's a ((ed) c b)
        # and then we reverse what is n parenthesis  bc de



        #self.assertEquals(solution("a ((d e) c b)") , "a (b c (d e))")

    def test_three(self):
        self.assertEqual(solution("one (two (three) four)"), "one (ruof (three) owt)")

    def test_four(self):
        self.assertEqual(solution("one (ruof ((rht)ee) owt)"), "one (two ((thr)ee) four)")

if __name__ == '__main__':
    unittest.main()
