n = int(input())
robots = []
for i in range(n):
    x_tmp, l_tmp = (int(i) for i in input().split())
    robots.append([x_tmp - l_tmp, x_tmp + l_tmp])

robots.sort()
ans = n
right = robots[0][1]
for i in range(n-1):
    if(robots[i+1][0] < right):
        ans -= 1
        right = min(right, robots[i+1][1])
    else:
        right = robots[i+1][1]
print(ans)
