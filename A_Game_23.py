n, m = map(int, input().split())


def count_steps(quotient):
    count = 0
    while quotient % 2 == 0:
        count += 1
        quotient //= 2
    while quotient % 3 == 0:
        count += 1
        quotient //= 3

    return count, quotient


if m == n:
    print(0)
elif m % n == 0:
    steps, rest = count_steps(m // n)
    print(steps if rest == 1 else -1)
else:
    print(-1)
