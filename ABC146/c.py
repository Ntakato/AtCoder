a, b, x = (int(i) for i in input().split())

if(a*1000000000+b*10 <= x):
    print(1000000000)
    exit()
if(a+b > x):
    print(0)
    exit()

L = 0
R = 1000000000
flag = 1
while(flag == 1):
    n = int((L+R)/2)
    length = len(str(n))
    if (a*n+b*length > x):
        R = n
    else:
        L = n
    if((a*n+b*length <= x) and (a*(n+1)+b*len(str(n+1)) > x)):
        flag = 0

print(n)
