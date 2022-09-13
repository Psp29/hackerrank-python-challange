import numpy

r, c = [int(i) for i in input().split()]
f = numpy.array([list(map(int, input().split())) for _ in range(r)])
print(numpy.transpose(f))
print(f.flatten())