a, b, t = (int(i) for i in input().split())
x=1
flag=True
while(flag):
    if(x*a>t):
        flag=False
    x+=1
print(b*(x-2))
        
