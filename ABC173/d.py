n = int(input())
a = list(map(int, input().split()))


def find_index(l):
    x = []
    length = len(l)-1
    for i in range(length):
        x.append(min(l[i], l[i+1]))
    max_value = max(x)
    return [x.index(max_value) + 1, max_value]


ans = 0
a.sort(reverse=True)
l = [a[0], a[0]]
x = []
length = len(l)-1
for i in range(length):
    x.append(min(l[i], l[i+1]))

for i in a[1:]:
    index_value = find_index(l)
    l.insert(index_value[0], i)
    ans += index_value[1]
print(ans)
