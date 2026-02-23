#https://www.codewars.com/kata/5bed96b9a68c19d394000b1d

VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
'''
To solve this in linear time $O(n)$, we need to answer these sub-questions:
Substring Mechanics: 
If a character is at index $i$ in a string of length $n$, 
1 - how many total substrings contain that specific character?
  for a string of lengh N, substrings containing a letter at index I
  are calculated with fomula 

    (i + 1) * (n - i)


2 - Vowel Identification: How do we efficiently check if a character is a vowel during a single pass?
Mathematical Pattern: 
Is there a formula to determine the "weight" 
of a position $i$ based on its distance from the start and the end of the string?

baceb
if char is in VOWELS

'''

def calculate_substrings(i, n):
    return (i + 1) * (n - i)

def is_vowel(chr):
    return chr in VOWELS


def vowel_recognition(s):
    total = 0
    for idx, chr in enumerate(s):
        if is_vowel(chr):
            total += calculate_substrings(idx, len(s))
    return total