s, dragons = map(int, input().split())


dragons_to_slay = []

for _ in range(dragons):
    ds, bonus = map(int, input().split())
    dragons_to_slay.append((ds,bonus))


dragons_to_slay.sort()

wins = True

for i,j in dragons_to_slay:
    if i < s:
        s += j
    else:
        wins = False
        break
        

if wins:
    print("YES")
else:
    print("NO")