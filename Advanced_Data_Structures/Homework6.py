import random

List = [10,1,2,3,4,5,6,7,8,9]
#List = [random.randrange(100) for x in range (100)]

def getMinMax(List):

    Minmax = [0,0]
    if len(List) == 1:
        Minmax[1] = List[0]
        Minmax[0] = List[0]
        return Minmax

    if List[0] > List[1]:
        Minmax[1] = List[0]
        Minmax[0] = List[1]
    else:
        Minmax[1] = List[1]
        Minmax[0] = List[0]

    for i in range(2,len(List)):
        if List[i] > Minmax[1]:
            Minmax[1] = List[i]
        elif List[i] < Minmax[0]:
            Minmax[0] = List[i]

    return Minmax

print(List)
print(getMinMax(List))
