#Binary search

#input

key = 999
L = [n for n in range(1000)]
#L = [4,6,7,10,2,9,2,8]
L.sort()
print("input", key, L)
#step

ans = -1
first = 0
last = len(L) - 1

x = 0
while True:
    item = last - first
    if item < 0: #empty
        break
    mid = first + item//2

    print("first, last, mid", first, last, mid)
    x = x + 1
    if key == L[mid]: # basic operation
        ans = mid
        break
    if key < L[mid]:
        last = mid -1
    if key > L[mid]:
        first = mid + 1
print("x", x)

#output
print("output", ans)
