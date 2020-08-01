n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

ans = [-1]
for i in range(n):
    tmp = list(map(lambda x: x-a[i], ans))
    index = 0
    if(min(tmp) >= 0):
        ans.append(a[i])
    else:
        xx = len(ans)
        for i in range(xx):
            if(tmp[i] >= 0):
                tmp[i] = -1000000000
        index = tmp.index(max(tmp))
        ans[index] = a[i]
print(len(ans))
