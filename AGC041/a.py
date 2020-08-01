import math

n, a, b = (int(i) for i in input().split())

x = b-a
if ((x % 2) == 0):
    print(math.floor(x/2))
    exit()
else:
    print(min(a-1, n-b) + 1 + (b-a-1)//2)
    exit()
