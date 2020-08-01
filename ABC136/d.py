s = input()
l = len(s)
s = s+"RL"
flag = 0
point = 0
ans = [0]*l
tmpR = 0
tmpL = 0
for i in range(l+2):
    if(flag == 0):
        if(s[i] == "R"):
            tmpR += 1
        else:
            flag = 1
            point = i
            tmpL = 1
    else:
        if(s[i] == "L"):
            tmpL += 1
        else:
            flag = 0
            if(tmpR % 2 == 0):
                if(tmpL % 2 == 0):
                    ans[point-1] = int(tmpR/2) + int(tmpL/2)
                    ans[point] = int(tmpR/2) + int(tmpL/2)
                else:
                    ans[point-1] = int(tmpR/2) + int(tmpL/2)
                    ans[point] = int(tmpR/2) + int(tmpL/2) + 1
            else:
                if(tmpL % 2 == 0):
                    ans[point-1] = int(tmpR/2) + int(tmpL/2) + 1
                    ans[point] = int(tmpR/2) + int(tmpL/2)
                else:
                    ans[point-1] = int(tmpR/2) + int(tmpL/2) + 1
                    ans[point] = int(tmpR/2) + int(tmpL/2) + 1
            tmpR = 1
for i in ans:
    print(i, end=' ')
