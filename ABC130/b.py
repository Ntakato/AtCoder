n,x = (int(i) for i in input().split())
l = [int(i) for i in input().split()]
d=0

for i in range(n):
    d += l[i]
    if(d>x):
        print(i+1)
        exit(0)
print(n+1)