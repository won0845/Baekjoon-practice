n = int(input())
f = {0: 0, 1: 1}


def fibo(n):
    for i in range(2, n+1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

print(fibo(n))