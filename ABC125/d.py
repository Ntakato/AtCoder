n=int(input())
a = [int(i) for i in input().split()] 
counta = 0
tmp = []
ans = 0
flag = 0
for i in range(n):
    if(a[i]<0):
        counta+=1
        flag=1
        tmp.append(abs(a[i]))
        tmp.sort()
    else:
        flag=0
        ans += a[i]
