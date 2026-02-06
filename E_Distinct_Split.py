t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    suff =[0] * (n+1)
    seen = set()
    
    for i in range(n-1, -1,-1):
        seen.add(s[i])
        suff[i] = len(seen)
        
    seen.clear()
    best = 0
    for i in range(n-1):
        seen.add(s[i])
        left = len(seen)
        right = suff[i+1]
        if left + right > best:
            best = left + right
    print(best)