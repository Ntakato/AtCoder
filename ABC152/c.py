n = int(input())
p = list(map(int, input().split()))

mini = p[0]
ans = 0
for i in range(n):
    if(mini >= p[i]):
        ans += 1
        mini = p[i]
print(ans)
