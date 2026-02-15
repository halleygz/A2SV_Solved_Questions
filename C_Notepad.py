t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    if n < 2:
        print("NO")
        continue

    earliest = {}
    ok = False
    for i in range(n - 1):
        pair = s[i : i + 2]
        if pair in earliest:
            if i - earliest[pair] >= 2:
                ok = True
                break
        else:
            earliest[pair] = i

    print("YES" if ok else "NO")
