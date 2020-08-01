s = input()
n = int(s)
l = len(s)
ans = 0
if(n < 10):
    print(n)
elif(n < 100):
    print(9)
elif(n < 1000):
    ans = 9
    ans += n-99
    print(ans)
elif(n < 10000):
    print(909)
elif(n < 100000):
    ans = 9+900
    ans += n-9999
    print(ans)
else:
    print(90909)
