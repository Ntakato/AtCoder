N=int(input())
S=input()

flag=0
count1=0
for i in range(N):
    if(flag==1):
        if(S[i]=="."):
            count1+=1
    if(S[i]=="#"):
        flag=1
flag=0
count2=0
for s in reversed(S):
    if(flag==1):
        if(s=="#"):
            count2+=1
    if(s=="."):
        flag=1

print(min(count1,count2))
