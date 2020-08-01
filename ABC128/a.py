n = int(input())
s = []
p = []
items = []
for i in range(n):
    a, b = (x for x in input().split())
    s.append(a)
    p.append(int(b))
    items.append({'i':i+1, 's':a, 'p':-int(b)})
sorted_items = sorted(items,key = lambda x: (x['s'],x['p']))
for i in range(n):
    print(sorted_items[i]['i'])
        
