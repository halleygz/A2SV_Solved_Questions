t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]

    total = 0
    layers = min(n, m) // 2
    target = "1543"

    for layer in range(layers):
        top = layer
        left = layer
        bottom = n - 1 - layer
        right = m - 1 - layer

        seq = []
        for j in range(left, right + 1):
            seq.append(grid[top][j])
        for i in range(top + 1, bottom):
            seq.append(grid[i][right])
        for j in range(right, left - 1, -1):
            seq.append(grid[bottom][j])
        for i in range(bottom - 1, top, -1):
            seq.append(grid[i][left])

        if len(seq) >= 4:
            s = "".join(seq)
            extended = s + s[:3]
            for i in range(len(s)):
                if extended[i : i + 4] == target:
                    total += 1

    print(total)

