h = int(input())
w = int(input())
n = int(input())
x = max(h, w)
if(n % x == 0):
    print(int(n/x))
    exit()
print(int(n/x) + 1)
