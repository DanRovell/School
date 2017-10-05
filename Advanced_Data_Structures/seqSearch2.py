#sequentialSearch V2

def seqSearch(key,L):
    if key in L:
        ans = L.index(key)
    else:
        ans = -1
    return ans

#testing
L = [5,6,7,3,2,10,11]
key = 7

print(seqSearch(key,L))
