import numpy

n, m = numpy.array(input().split(" "), int)

# Convert all string to int  e.g. ['1', '2', '3'] => [1, 2, 3] using eval
# a = [eval(i) for i in a]
# b = [eval(i) for i in b]

# or use numpy
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

result_list = [numpy.add(a, b), numpy.subtract(a, b), numpy.multiply(a, b), numpy.floor_divide(a, b), numpy.mod(a, b), numpy.power(a, b)]   # floor_divide means integer division.

for final in result_list:
    print (final)
