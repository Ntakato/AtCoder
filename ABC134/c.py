n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

sortedA = sorted(a)
max = sortedA[-1]
max2 = sortedA[-2]
x = 0
maxIndex = []
for i in range(n):
    if(max == a[i]):
        x += 1
        maxIndex.append(i)

if(x > 1):
    for i in range(n):
        print(max)
else:
    for i in range(n):
        if(a[i] == max):
            print(max2)
        else:
            print(max)
