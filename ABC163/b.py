n,m = (int(i) for i in input().split())
a = list(map(int,input().split()))

syukudai_day = sum(a)
if(n-syukudai_day >= 0):
    print(n-syukudai_day)
else:
    print('-1')
