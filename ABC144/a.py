a, b = (int(i) for i in input().split())
if(a < 10 and a > 0 and 0 < b and b < 10):
    print(a*b)
    exit()
print(-1)
