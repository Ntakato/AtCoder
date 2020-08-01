n = int(input())

tmp = int(n/1.08)
if(int(tmp*1.08) == n):
    print(tmp)
    exit()
elif(int((tmp+1)*1.08) == n):
    print(tmp+1)
    exit()
print(":(")
