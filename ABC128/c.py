n, m = (int(i) for i in input().split())

k_s = []
for i in range(m):
    k_s.append([int(x) for x in input().split()])
p = [int(x) for x in input().split()]
ans = 0
sw = [[0]*n for i in range(m)]

for i in range(m):
    for j in range(len(k_s[i])-1):
        sw[i][k_s[i][j+1]-1]=1
for i in range(2**n):
    s = [0]*n
    k=n-1
    while(i>=1):
        s[k] = (i%2)
        i = int(i/2)
        k -= 1
    tmp = [0]*m
    for j in range(m):
        f = 1
        for x in range(n):
            tmp[j] += sw[j][x]*s[x]
        if(tmp[j]%2!=p[j]):
            f = 0
            break
    ans += 1*f
print(ans)
