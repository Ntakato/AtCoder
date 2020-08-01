n, k = (int(i) for i in input().split())
p = list(map(int, input().split()))

ans = 0
tmp = 0
for i in range(k):
    tmp += (p[i]+1)/2
ans = tmp
for i in range(1, n-k+1):
    tmp += -(p[i-1]+1)/2 + (p[i+k-1]+1)/2
    if(ans < tmp):
        ans = tmp

print(ans)
