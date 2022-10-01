import numpy as np
# np.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(np.array(list(map(int, input().split()))))

mean = np.mean(array, axis= 1)
var = np.var(array, axis= 0)
std = np.std(array, axis = None)

print(mean, var, round(std, 11), sep="\n")