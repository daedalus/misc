import gmpy2
import sys

a = 0xF5A6F3821EE321D136E8A13FED75FC54B7C645163185348ABCC5E97F29735CDC
p = gmpy2.next_prime(a)
q0 = gmpy2.next_prime(p)
q1 = gmpy2.next_prime(q0 + 110000000000)

N0 = p * q0
N1 = p * q1

print("p:", p)
print("q0:", q0)
print("q1:", q1)
print("N0:", N0)
print("N1:", N1)


def factor_related(N0, N1, epsilon=1000):
    sys.stderr.write("Trying to factor pair:\n%d\n%d\n" % (N0, N1))
    result = []
    a = gmpy2.isqrt(N0)
    b = gmpy2.isqrt(N1)

    c = min(a, b)
    d = max(a, b)

    # print("q0-c:",q0-c)
    # print("q1-d:",q1-d)

    e = d - c + epsilon

    sys.stderr.write("sqrt_min: %d\n" % c)
    sys.stderr.write("sqrt_max: %d\n" % d)
    sys.stderr.write("range: %d\n" % e)

    N = N0 * N1

    # y = gmpy2.next_prime(c-e)
    y = gmpy2.next_prime(d - e)

    for x in range(1, e):
        # y = c + x
        sys.stderr.write("%d %d %d %d\r" % (x, e - x, (e - x) / x, y))
        if N % y == 0:
            if N0 % y == 0:
                f = [y, N0 // y]
                sys.stderr.write("Factor found: %s in %d\n" % (str(f), x))
                result += f
            if N1 % y == 0:
                f = [y, N1 // y]
                sys.stderr.write("Factor found: %s in %d\n" % (str(f), x))
                result += f
            if len(result) >= 4:
                break
        y = gmpy2.next_prime(y)
    return result


print(factor_related(N0, N1, epsilon=100000))
N0 = 39578251185560508765789986436883915796407930659608281975081398825997486593363942764450954587346725410729324861726130026998308053052410610297612320083038591
N1 = 39578251185560508765789986436883915796407930659608281975081398825997853603095770096367419621912275547461664662039085358780927515509450598370923477750251521
print(factor_related(N0, N1))
