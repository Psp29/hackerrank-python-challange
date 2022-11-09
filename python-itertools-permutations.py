from itertools import permutations

str, n = input().split()
ans = list(permutations(str, int(n)))

ans.sort()
for _ in ans:
    print("".join(_))