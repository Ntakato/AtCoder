k = int(input())
a = [100]*15
a[0] = 1


def runrun_generater(x):
    for i in range(14):
        if(x[i]+1 - x[i+1] < 2 and (x[i] < 9 or x[i] == 100)):
            if(x[i] == 100):
                x[i] = 1
                if(i != 0):
                    x[:i] = [0]*i
            else:
                x[i] += 1
                if(i != 0):
                    k = i
                    for xx in range(i):
                        if(x[k] == 0):
                            x[k-1] = 0
                        else:
                            x[k-1] = x[k]-1
                        k -= 1
            return x


for i in range(k-1):
    a = runrun_generater(a)
ans = 0
keta = 1
for y in a:
    if(y != 100):
        ans += y * keta
        keta *= 10
print(ans)
