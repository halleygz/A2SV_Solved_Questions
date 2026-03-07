t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    
    pref_red = [0] * len(r)
    pref_red[0] = r[0]
    
    for i in range(1, len(r)):
        pref_red[i] = pref_red[i - 1] + r[i]
        
    pref_blue = [0] * len(b)
    pref_blue[0] = b[0]
    
    for i in range(1, len(b)):
        pref_blue[i] = pref_blue[i - 1] + b[i]
        
    
    val = max(0, max(pref_red)) + max(0, max(pref_blue))
    
    print(val)