#https://www.codewars.com/kata/5bed96b9a68c19d394000b1d

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


def vowel_recognition(s):
    sts = set(s)
    if not vowels.intersection(sts):
        return 0
    # your code here