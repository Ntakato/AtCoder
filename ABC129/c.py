n,m = (int(i) for i in input().split())
a = [-1]

for i in range(m):
    a.append(int(input()))
a .append(n+1)
fibo = [1,2,3]

ans = 1
start =0
if(a[1]==1):
    start =1
for x in range(start,m+1):
    if(abs(a[x+1]-a[x])==1):
       ans = 0
    else:
        l = len(fibo)
        while(a[x+1]-a[x]-3>l-1):
            fibo.append(fibo[-1]+fibo[-2])
            l += 1
        ans = (ans*fibo[a[x+1]-a[x]-3])%1000000007
print(ans)
