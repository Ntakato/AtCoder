n, k = (int(i) for i in input().split())

n = n % k
ans = n

if(ans > abs(n-k)):
    ans = abs(n-k)

print(ans)
