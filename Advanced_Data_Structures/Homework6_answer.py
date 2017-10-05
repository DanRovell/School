def findMinMax(L):
    if len(L)%2 != 0:
        c = 0
        minv = maxv = L[0]
        i = 1
    else:
        c = 1
        (minv,maxv) = (L[0], L[1]) if L[0] <= L[1] else (L[1], L[0])
        i = 2

    for n in range(i, len(L), 2):
        c = c + 3
        if L[n] <= L[n + 1]:
            minv = minv if minv <= L[n] else L[n]
            maxv = maxv if maxv >= L[n + 1] else L[n + 1]
        else:
            miv = minv if minv <= L[n + 1] else L[n + 1]
            maxv = maxv if maxv >= L[n] else L[n]
    print(c, 1.5*len(L))
    return minv, maxv

from random import randrange as rand
L = [rand(100) for x in range(193)]
print(L, len(L))
print(findMinMax(L))
