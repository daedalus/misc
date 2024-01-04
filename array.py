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
    return all(A[n] == B[n] for n in range(0, len(A)))


def list_compare2(A,B):
    tmp = 0
    n = 0
    lA=len(A)
    while tmp == 0 and n < lA:
        tmp += abs(A[n]-B[n])
        n += 1
    return n == lA


def fixed_sliding_window(arr, k):
    result = [sum(arr[:k])]
    result.extend(result[i] + arr[i+k] - arr[i] for i in range(0, len(arr)-k))
    return result
print(fixed_sliding_window(list(range(1,7)),3))


def dynamic_sliding_window(arr, x):
    min_length = len(arr)
    start = 0
    end = 0
    current_sum = 0
    while end < min_length:
        current_sum += arr[end]
        end += 1
        while start < end and current_sum >= x:
            current_sum -= arr[start]
            start += 1
            min_length = min(min_length, end-start+1)
    return min_length
print(dynamic_sliding_window(list(range(1,7)), 7))

