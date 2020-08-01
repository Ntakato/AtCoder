s, t = (i for i in input().split())
a, b = (int(i) for i in input().split())
u = input()

if(s == u):
    print(a-1, b)
else:
    print(a, b-1)
