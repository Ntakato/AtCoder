a1, a2, a3 = (int(i) for i in input().split())

if(a1 + a2 + a3 > 21):
    print("bust")
    exit()
print("win")
