n = int(input())
h = [int(i) for i in input().split()]
max = 0
for i in h:
    if(i > max):
        max = i
    if(max-2 >= i):
        print("No")
        exit()
print("Yes")
