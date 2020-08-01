n = int(input())
a = []
x = [[] for i in range(n)]
y = [[] for i in range(n)]
for i in range(n):
    a.append(int(input()))
    for j in range(a[i]):
        xx, yy = (int(i) for i in input().split())
        x[i].append(xx)
        y[i].append(yy)

testimony = [[2]*n for i in range(n)]

for i in range(n):
    for j in range(a[i]):
        if(y[i][j] == 1):
            testimony[i][x[i][j]-1] = 1
        elif(y[i][j] == 0):
            testimony[i][x[i][j]-1] = 0

ans = 0
for i in range(2**n):
    bit_list = []
    for j in range(n):
        if ((i >> j) & 1):
            bit_list.append(1)
        else:
            bit_list.append(0)
    flag = 1
    for k in range(n):
        if(bit_list[k] == 1):
            for l in range(n):
                if(testimony[k][l] != 2):
                    if(testimony[k][l] != bit_list[l]):
                        flag = 0
                        break
    if(flag == 1):
        ans = max(sum(bit_list), ans)
print(ans)
