import numpy
array = []
a = (input().split())
for i in a:
    array.append(int(i))
print(numpy.reshape(array,(3,3)))