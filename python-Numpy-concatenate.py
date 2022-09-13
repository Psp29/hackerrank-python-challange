import numpy

m, n, p = map(int, input().split())

array1 = numpy.array([list(map(int, input().split())) for _ in range(m)])
array2 = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.concatenate((array1, array2)))