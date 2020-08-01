p,q,r = (int(i) for i in input().split())
min = 1000
x = [p+q,q+r,r+p]
for i in x:
    if(i<min):
        min=i
print(min)
