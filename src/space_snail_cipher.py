# https://www.codewars.com/kata/6a37e118ef0c62f1772b6c6d

def encode(plaintext : str, key : int) -> str:
    return ''
                                

def decode(cipher : str ,key : int) -> str:
    return ''


def get_direction(key : str) -> int:
    # 1st digit orientation
    # 2nd digit gap
    '''
    Positive key $\rightarrow$ fill center-out (character 0 goes to the spiral center).
    Negative key $\rightarrow$ fill outside-in (character 0 starts at the outer tip of the spiral).
    
    '''
    if key > 0:
        return 1
    else:
        return -1