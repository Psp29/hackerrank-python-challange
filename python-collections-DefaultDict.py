from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    d[input()].append(i+1)
for j in range(m):
    x = input()
    if x in d:
        print(*d[x])
    else:
        print('-1')