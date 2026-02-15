import sys


def can_form_permutation(found, s):
	max_b = max(found)
	found_set = set(found)

	missing_sum = 0
	for value in range(1, max_b + 1):
		if value not in found_set:
			missing_sum += value

	if missing_sum > s:
		return False

	remaining = s - missing_sum
	next_val = max_b + 1
	while remaining > 0:
		remaining -= next_val
		next_val += 1

	return remaining == 0



input = sys.stdin.read().strip().split()
t = int(input[0])
idx = 1
out_lines = []
for _ in range(t):
    m = int(input[idx])
    s = int(input[idx + 1])
    idx += 2
    found = list(map(int, input[idx:idx + m]))
    idx += m

    out_lines.append("YES" if can_form_permutation(found, s) else "NO")

print("\n".join(out_lines))
