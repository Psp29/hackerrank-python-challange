# With namedtuple
from collections import namedtuple as nt
n, students =int(input().strip()) ,nt('Students', input().strip().split())
print(sum([int(students(*input().split()).MARKS) for _ in range(n)])/n)

# without namedtuple
# n, rows = int(input().strip()), input().strip().split()
# print(sum([int(input().strip().split()[rows.index('MARKS')]) for _ in range(n)])/n)