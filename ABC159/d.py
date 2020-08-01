n = int(input())
a = list(map(int, input().split()))
x = [0]*(n+1)
tmp = [0]*(n+1)
for i in a:
    x[i] += 1
ans = 0
for i in range(1, n+1):
    tmp[i] = (x[i] * (x[i]-1))//2
    ans += tmp[i]
for i in range(1, n+1):
    print(ans - tmp[a[i-1]] + (x[a[i-1]]-1)*(x[a[i-1]]-2)//2)
