#https://app.codility.com/programmers/task/largest_string/

def replaceabc(input, largest=None):
    if input.find('abb') >= 0:
        tmp =  input.replace('abb', 'baa')
        if not largest:
            return replaceabc(tmp, tmp)
        else:
            minstr = min(tmp, largest)
            return replaceabc(tmp, minstr)
    else:
        return input



def solution(A):
    # Replace with while loop
    return replaceabc(A)