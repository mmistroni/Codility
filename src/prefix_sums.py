
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def generate_prefix_sum(A):
    holder = [0] * (len(A)+1)
    for i in range(1, len(A)+1):
        holder[i] = holder[i-1] +  A[i-1]

    return holder