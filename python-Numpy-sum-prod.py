import numpy as np

N, M = map(int, input().split())    # first input
array = []

for _ in range(N):
    array.append(np.array(list(map(int, input().split())))) # Next inputs

print(array)
print (np.prod((np.sum(array, axis = 0)), axis = 0))