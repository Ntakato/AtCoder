import itertools

h, w, k = list(map(int, input().split()))
s = []
a = []
h_index = []
w_index = []
for i in range(h):
    h_index.append(i)
for i in range(w):
    w_index.append(i)
for i in range(h):
    s.append(input())
    a.append([])
    for j in s[i]:
        if(j == '.'):
            a[i].append(0)
        else:
            a[i].append(1)

ans = 0
h_list = []
for i in range(h+1):
    h_list.extend(list(itertools.combinations(h_index, i)))

w_list = []
for i in range(w+1):
    w_list.extend(list(itertools.combinations(w_index, i)))

for selected_hs in h_list:
    for selected_ws in w_list:
        for i in selected_hs:
            a[i] = [0] * w
        for j in selected_ws:
            for i in range(h):
                a[i][j] = 0
        kuro = 0
        for a_sub in a:
            kuro += sum(a_sub)
        if(kuro == k):
            ans += 1
        for i in range(h):
            for j in range(w):
                if(s[i][j] == '.'):
                    a[i][j] = 0
                else:
                    a[i][j] = 1

print(ans)
