n, k = (int(i) for i in input().split())
d = []
A = []
for i in range(k):
    d.append(int(int(input())))
    A.append(list(map(int,input().split())))

x = [0] * n
for a in A:
    for i in a:
        x[i-1] += 1

ans = 0
for i in x:
    if(i == 0):
        ans += 1
print(ans)
