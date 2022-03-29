
parenthesisDict =   { "(" : ")",
                      "{" : "}",
                      "[" :  "]"}

reversesParentesisDict = dict((v,k) for k, v in parenthesisDict.items())

def solution(A):

    holder = []
    for item in A:
        try:
            if item in parenthesisDict.keys():
                holder.append(item)
            else:
                expected = reversesParentesisDict[item]
                popped = holder.pop()
                if popped != expected:
                    return 0
        except Exception as e:
            return 0
    if not holder:
        return 1
    return 0
