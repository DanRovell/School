def fibW(n):
    f = 0
    f1 = 0
    f2 = 1
    x = 0
    while x < n:
        print(f)
        f = f2
        f2 = f1 + f2
        f1 = f
        x += 1
    return f
key = 10
print(fibW(key))
