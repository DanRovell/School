def fib(n):

    if n < 2:
        f = n
    else:
        f1 = fib(n-1)
        f2 = fib(n-2)
        f = f1 + f2
    return f

key = 10
print(fib(key))
