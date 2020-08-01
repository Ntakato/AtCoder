n, a, b = (int(i) for i in input().split())

x = b-a
if ((x % 2) == 0):
    print(x//2)
    exit()
else:
    print(min(a-1, n-b) + (x+1)//2)
    exit()
