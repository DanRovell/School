

a = 0
b = 1
x = 0
key = 10
while x <= key:
    if x < 2:
        fib = x
    else:
        fib = a + b
    a = b
    b = fib
    x  = x + 1

print(fib)
