n = int(input())
r = int(n**0.5)+1
min = n-1
for i in range(2, r):
    if(n % i == 0):
        a = i
        b = int(n/i)
        tmp = a+b-2
        if(min > tmp):
            min = tmp
print(min)
