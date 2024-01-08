# https://gitlab.com/snippets/1879264

from math import sqrt


def fib_eig(k):
    import gmpy2

    ctx = gmpy2.get_context()
    ctx.precision += 1000
    sqrt5 = gmpy2.sqrt(5)

    lambda1 = (1 + sqrt5) / 2
    lambda2 = (1 - sqrt5) / 2
    fk = (lambda1**k - lambda2**k) / (lambda1 - lambda2)
    return int(fk)


fibonacci = [0, 1]


def fib_mem(k):
    try:
        return fibonacci[k]
    except IndexError:
        fibonacci.append(fib_mem(k - 2) + fib_mem(k - 1))
    return fibonacci[k]


print(fib_mem(1000))
print(fib_eig(1000))
