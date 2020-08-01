n = int(input())

tmp = n
digit = 0
while(tmp > 1):
    tmp = tmp/10
    digit += 1

if(n < 10):
    print(n)
    exit()
elif(10 <= n and n < 100):
    ans = 9
    # aが一桁
    for i in range(1, 10):
        if(n >= i*10 + i):
            ans += 2
    for i in range(1, 10):
        for j in range(1, 10):
            a = i*10 + j
            b = j*10 + i
            if(n >= a and n >= j*10 + i):
                ans += 1
    print(ans)
    exit()
ans = 108
a = 0
b = 0
for d in range(digit):
    for i in range(1, 10):
        for j in range(1, 10):
            if(d > 2):
                r = 10**(d-1)
                for k in range(r):
                    if((i*10**d + j) <= n):
                        A = i*10**d + k*10 + j
                        if(A <= n):
                            print("A", A)
                            a += 1
                    if((j*10**d + i) <= n):
                        B = j*10**d + k*10 + i
                        if(B <= n):
                            print("B", B)
                            b += 1
print(a, b, a*b)
print(ans+a*b)

# elif(100 <= n and n < 1000):
#     # a,bともに一桁
#     ans = 9
#     # aが一桁,bが二桁/その逆
#     ans += 18
