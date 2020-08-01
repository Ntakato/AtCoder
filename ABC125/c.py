n = int(input())
a = [int(i) for i in input().split()] 

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
    
tmp = []
tmp.append(a[0])
if n==1:
    print(a[0])
    exit(0)
else:
    element = gcd(a[0], a[1])
    tmp.append(element)
    if n==2:
        print(element)
        exit(0)
    else:
        for i in range(2,n):
            element=gcd(element,a[i])
            print(element)
            tmp.append(element)
GCD = tmp[n-2]
ans = 0
gcd_tmptmp=a[n-1]
for i in range(1,n-2):
    print("GCDtmp:{}".format(GCD))
    x=n-i-3
    if(x<0):
        gcd_tmp = gcd_tmptmp
        print("gcd_tmp{},{}".format(gcd_tmptmp,gcd_tmptmp))
    else:
        gcd_tmp=gcd(tmp[n-i-2],gcd_tmptmp)
        print("gcd/tmp{},{}".format(gcd_tmptmp,tmp[n-i-2]))
    print(gcd_tmp)
    print("{},{}".format(gcd_tmptmp,a[n-i-2]))
    print("GCDtmp:{}".format(gcd_tmp))
    if(gcd_tmp > GCD):
        GCD = gcd_tmp
    gcd_tmptmp = gcd(gcd_tmptmp,a[n-i-2])
    print(gcd_tmptmp)
print(GCD)
