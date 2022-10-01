# Find Matrix Product.
# Tip: use 'dot' function of numpy or directly use 'matmul' fuction of Numpy.

import numpy as np

N = int(input())

A = []
B = []

for _ in range(N):
    A.append(np.array(list(map(int, input().split()))))
    
for _ in range(N):
    B.append(np.array(list(map(int, input().split()))))

print (np.dot(A, B))