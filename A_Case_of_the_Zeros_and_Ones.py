# n = int(input())
# m = input().strip()

# c0 = m.count('0')
# c1 = m.count('1')

# print(abs(c0 - c1))

frs = [1,4,3,2,0]

sorted(frs)

print(type(enumerate(frs)))

nums = [[i,j] for i in range(2)  for j in range(3) if i!=j]


fitcha = [[0]] * 5
fitcha[0][0] = 1
print(fitcha)