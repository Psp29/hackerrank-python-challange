cube = lambda x: x**3

def fibonacci(n):
    a0, a1 = 0, 1
    fibo = []
    for _ in range(n):
        fibo.append(a0)
        a0, a1 = a1, a0 + a1
    return fibo


n = int(input())
print(list(map(cube, fibonacci(n))))