t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    pref = 0
    first_from_x = -1
    first_from_zero = -1

    for i, ch in enumerate(s, 1):
        if ch == 'L':
            pref -= 1
        else:
            pref += 1

        if first_from_x == -1 and x + pref == 0:
            first_from_x = i

        if first_from_zero == -1 and pref == 0:
            first_from_zero = i

    if first_from_x == -1 or first_from_x > k:
        print(0)
        continue

    ans = 1
    remaining = k - first_from_x

    if first_from_zero != -1:
        ans += remaining // first_from_zero

    print(ans)


