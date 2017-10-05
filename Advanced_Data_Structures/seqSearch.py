#sequential search

#input data
L = [4,6,7,8,3,3,8]
n = len(L)
key = 4

def seqSearch(key, L):
    #step
    ans = -1
    for i in range(len(L)):
        if L[i] == key:
            ans = i
            break
    return ans

print(seqSearch(key,L))
