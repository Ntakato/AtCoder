n, k = (int(i) for i in input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

a.sort()
f.sort(reverse=True)

for i in range(n):
    if(k-a[i] > 0):
        k = k-a[i]
        a[i] = 0
    else:
        a[i] = a[i]-k
        break

ans = 0
for i in range(n):
    ans += a[i]*f[i]

print(ans)
