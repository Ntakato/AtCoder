n, m = (int(i) for i in input().split())
h = list(map(int,input().split()))
A = []
B = []
for i in range(m):
    a, b = (int(i) for i in input().split())
    A.append(a)
    B.append(b)

x = [True]*n

for i in range(m):
    if(h[A[i]-1] >= h[B[i]-1]):
        x[B[i]-1] = False
    if(h[A[i]-1] <= h[B[i]-1]):
        x[A[i]-1] = False
ans = 0
for i in x:
    if(i):
        ans += 1
print(ans)
