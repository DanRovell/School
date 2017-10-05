
def seqSearch(E, num, K):
	return seqSearchRec(E, 0, num, K)


def seqSearchRec(E, index, num, K):
    if index >= num:
        ans = -1
    elif E[index] == K and index < num:
        ans = index
    else:
        ans = seqSearchRec(E, index+1, num, K)

    return ans

E = [1,2,3,4,5]
num = 2
K = 5

print(seqSearch(E, num, K))
