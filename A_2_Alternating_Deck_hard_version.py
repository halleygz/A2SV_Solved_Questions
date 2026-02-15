def solve_case(n):
    aw = ab = bw = bb = 0

    remaining = n
    step_len = 1
    player = 0 
    block_remaining = 1
    color = 0  # 0 for White 1 for Black

    while remaining > 0:
        take = min(step_len, remaining)
        if color == 0:
            whites = (take + 1) // 2
        else:
            whites = take // 2
        blacks = take - whites

        if player == 0:
            aw += whites
            ab += blacks
        else:
            bw += whites
            bb += blacks

        if take % 2 == 1:
            color ^= 1

        remaining -= take
        step_len += 1

        block_remaining -= 1
        if block_remaining == 0:
            player ^= 1
            block_remaining = 2

    return aw, ab, bw, bb




t = int(input())
out_lines = []
for _ in range(t):
    n = int(input())
    aw, ab, bw, bb = solve_case(n)
    out_lines.append(f"{aw} {ab} {bw} {bb}")

print("\n".join(out_lines))


