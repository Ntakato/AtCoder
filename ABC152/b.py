a, b = (int(i) for i in input().split())
ans = ""
if(a < b):
    for i in range(b):
        ans = ans + str(a)
else:
    for i in range(a):
        ans = ans + str(b)

print(ans)
