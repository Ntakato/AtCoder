l,r = [int(i) for i in input().split()]
ans = 100000
L = min(r,l+2019)
for i in range(l,L):
    R = min(l+2019,r)
    for j in range(i+1,R+1):
        tmp = (i*j)%2019
        if(ans>tmp):
            ans = tmp
print(ans)