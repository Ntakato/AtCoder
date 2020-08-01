N=int(input())
S=input()

a=0
S2=[]
minimum=1000000
for i in range(N):
    if(S[i]=="."):
        S2.append(-1)
    else:
        S2.append(1)

for tmp in range(N+1):
    count=0
    for i in range(N):
        if(i<tmp):
            if( S2[i]*-1 == -1):
                count+=1
        else:
            if(S2[i]*1==-1):
                count+=1
    if(count<minimum):
        minimum=count
print(minimum)
