n = int(input())

sum = 0
for i in range(n):
    s = input().lower()
    
    if s=="tetrahedron":
        sum+=4
    elif s=="cube":
        sum+=6
    elif s == "octahedron":
        sum+=8
    elif s == "dodecahedron":
        sum+=12
    elif s == "icosahedron":
        sum+=20
    else:
        continue
    

    
print(sum)



