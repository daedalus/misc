list_compare0 = lambda A,B: all(A[n] == B[n] for n in range(0, len(A)))

def list_compare1(A,B):
    """
    Compare elementwise two lists.
    Args:
        Lists: A,B.
    Returns:
        Boolean
    Comment:
        Still faster than: return all(A[n] == B[n] for n in range(0, len(A)))
    """
    for n in range(0,len(A)):
        if A[n] != B[n]:
            return False
    return True


def list_compare2(A,B):
    tmp = 0
    n = 0
    lA = len(A)
    while tmp == 0 and n < lA:
        tmp += abs(A[n]-B[n])
        n += 1
    return n == lA - 1
