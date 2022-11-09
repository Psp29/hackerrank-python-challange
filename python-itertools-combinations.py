from itertools import combinations

str, n = input().split()

lst = list(str)
lst.sort()

for i in range(1, int(n)+1):
    [print("".join(x)) for x in list(combinations(lst, i))]