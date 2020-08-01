N = int(input())
ans = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for i in range(N):
    s = input()
    if(s == 'AC'):
        ans['AC'] = ans['AC'] + 1
    elif(s == 'WA'):
        ans['WA'] = ans['WA'] + 1
    elif(s == 'TLE'):
        ans['TLE'] = ans['TLE'] + 1
    elif(s == 'RE'):
        ans['RE'] = ans['RE'] + 1
print('AC x {}' .format(ans['AC']))
print('WA x {}'.format(ans['WA']))
print('TLE x {}'.format(ans['TLE']))
print('RE x {}'.format(ans['RE']))
