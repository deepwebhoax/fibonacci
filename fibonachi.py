def fib(n):
    f = [0, 1]
    if n<2:
        return f[n-1]

    for i in range(2, n):
        next = f[1] + f[0]
        f = [f[1], next]

    return f[1]

n = int(input("Input the index (i>0) of a fibonachi number:"))

print(fib(n))

