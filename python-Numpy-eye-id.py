import numpy
# numpy.set_printoptions(legacy='1.13')

n, m = input().split()

n = int(n)
m = int(m)

print(numpy.eye(n, m))