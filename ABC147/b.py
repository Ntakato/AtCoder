s = input()

length = len(s)
ans = 0
for i in range(int(length/2)):
    if(s[i] != s[-1*i-1]):
        ans += 1
print(ans)
