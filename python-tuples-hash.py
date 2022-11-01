# using pypy3(instead of python) gives right answer according to the community

n = int(input())
numbers = map(int, input().split())
tup1 = tuple(numbers)
print(hash(tup1))
print(numbers)
