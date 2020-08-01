n, m = (int(i) for i in input().split())
a = list(map(int, input().split()))

vote_sum = sum(a)
threshold = vote_sum / (4*m)

pick = 0
for a_i in a:
    if(a_i >= threshold):
        pick += 1
if (pick >= m):
    print('Yes')
else:
    print('No')
