n, d = [int(i) for i in input().split()]
for i in range(20):
    if((2*d+1)*i >= n):
        print(i)
        exit()
