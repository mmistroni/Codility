
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
def solution(input_array):
    mn, mx= input_array[0], input_array[0]
    mnCount=0
    mxCount=0

    for item in input_array[1:]:
        current_mx = max(mx, item)
        current_min = min(mx, item)
        if current_mx > mx:
            mxCount +=1
            mx = current_mx
        if current_min < mn:
            mnCount +=1
            mn  = current_min

    return mxCount, mnCount