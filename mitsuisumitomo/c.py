x = int(input())

q = int(x/100)

if(100*q <= x and x <= 105*q):
    print(1)
    exit()
print(0)
