n = int(input())
W = [int(i) for i in input().split()]
S1 = sum(W)
S2 = 0
ans = abs(S1-S2)
for w in W:
    S1 -= w
    S2 += w
    if(ans>abs(S1-S2)):
        ans = abs(S1-S2)
print(ans)
