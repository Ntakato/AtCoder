n = int(input())
a = [int(i) for i in input().split()]
a.extend(a)
ans = 0
k = 0
for i in range(n):
    ans += a[i]*(-1)**k
    k += 1
print(ans,end=" ")
for i in range(n-1):
    ans = 2*a[i]-ans 
    print(ans,end=" ")