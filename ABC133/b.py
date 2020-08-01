import math

def dis(n,x,y):
    distance = 0
    for i in range(len(x)):
        distance += (x[i]-y[i])*(x[i]-y[i])
    # print(distance)
    return math.sqrt(distance)



n,d = [int(i) for i in input().split()]
x = [[int(i) for i in input().split()] for i in range(n)] 
# print(x)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        # print(dis(d,x[i],x[j]))
        # print(dis(d,x[i],x[j]).is_integer())
        if(dis(d,x[i],x[j]).is_integer()):
            ans += 1
print(ans)

