import numpy as np

N, M = map(int, input().split())    # first input
array = []

for _ in range(N):
    array.append(np.array(list(map(int, input().split())))) # Next inputs
print (np.max(np.min(array, axis=1), axis=0))