N = int(input())
v = [int(i) for i in input().split()] 
c = [int(i) for i in input().split()] 

ans = 0
for i in range(N):
    tmp = v[i] - c[i]
    if(tmp>0):
        ans+=tmp
print(ans)
    
