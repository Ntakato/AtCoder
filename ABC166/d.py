import math
x = int(input())
sqrt_x = int(math.sqrt(x))
for i in range(1, sqrt_x):
    if(x % i == 0):
        X = i
        Z = x/i
        Y = math.sqrt(1/3*(-7*X + math.sqrt(52*X*X*X*X+48*Z)))
        a = round((X+Y)/2)
        b = round((X-Y)/2)
        if(a*a*a*a*a - b*b*b*b*b == x):
            print(a, b)
            exit()
