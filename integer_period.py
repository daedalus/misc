# code translated to python from: https://codereview.stackexchange.com/questions/197807/c-code-to-calculate-the-binary-period-of-an-integer

import math

n = 6230699590438730861365449567108381380284939 ** 2


def find_period(n):
    shifted = n
    l = int(math.log(n, 2))
    mask = (1 << l) - 1

    for period in range(1, l):
        shifted >>= 1
        mask >>= 1
        if ((n ^ shifted) & mask) == 0:
            return period
    return -1


print(find_period(n))  # should be 281
