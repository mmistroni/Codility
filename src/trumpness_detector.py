#https://www.codewars.com/kata/57829376a1b8d576640000d6/train/python
import itertools

vowels = ['a', 'e', 'i', 'o', 'u']

def group_consecutive_letters_itertools(sentence: str) -> list:
    """
    Groups consecutive identical letters using itertools.groupby.
    """
    return [(key, len(list(group))) for key, group in itertools.groupby(sentence)]        


def trump_detector(sentence):
    grouped_letters = group_consecutive_letters_itertools(sentence.lower())
    sampled = [t for t in grouped_letters if t[0].lower() in vowels]
    reduced = [t[1]-1 for t in sampled]
    numv = [t[0] for t in sampled]

    return round(sum(reduced) / len(numv), 2)
