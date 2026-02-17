import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = 8

    for i in range(n):
        if i + 1 < n and s[i] == 'a' and s[i + 1] == 'a':
            ans = 2
            break

        if i + 2 < n and s[i] == 'a' and s[i + 2] == 'a':
            ans = min(ans, 3)

        if i + 3 < n and s[i] == 'a' and s[i + 3] == 'a' and s[i + 1] != s[i + 2]:
            ans = min(ans, 4)

        if (
            i + 6 < n
            and s[i] == 'a'
            and s[i + 3] == 'a'
            and s[i + 6] == 'a'
            and s[i + 1] == s[i + 2]
            and s[i + 4] == s[i + 5]
            and s[i + 1] != s[i + 4]
        ):
            ans = min(ans, 7)

    print(ans if ans < 8 else -1)

