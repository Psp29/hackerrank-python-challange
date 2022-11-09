from itertools import product

A, B = list(map(int, input().split())), list(map(int, input().split()))
ans = list(product(A, B))

print(*ans)