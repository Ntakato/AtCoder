n = int(input())
a = [int(x) for x in input().split()]
b = [0] * n

for i in range(n):
    x = n-i
    if(a[x-1] == 0):
        tmp = 0
        for j in range(int(n/x)):
            if(b[x*(j + 1)-1] == 1):
                tmp += 1
        if(tmp % 2 == 1):
            b[x-1] = 1
    else:
        tmp = 0
        for j in range(int(n/x)):
            if(b[x*(j + 1)-1] == 1):
                tmp += 1
        if(tmp % 2 == 0):
            b[x-1] = 1

ans = 0
ANS = []
for i in range(n):
    if(b[i] == 1):
        ans += 1
        ANS.append(i)
print(ans)
for i in range(len(ANS)):
    print(ANS[i]+1, end=' ')
