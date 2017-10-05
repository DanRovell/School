#intList def

class IntList:
    def __init__(self, iL = []):
        self.aList = iL

    def cons(self, newElem):
        return IntList([newElem]+self.aList[:])

    def first(self):
        return self.aList[0]

    def rest(self):
        return IntList(self.aList[1:])

    @property
    def nil(self):
        return len(self.aList) == 0

    def __str__(self):
        return str(self.aList)

#def object

al = IntList()

al = al.cons(7)
al = al.cons(6)
al = al.cons(5)
al = al.cons(3)
al = al.cons(1)
al = al.cons(4)
al = al.cons(2)

key = 3

#search for key
def recSearch(key, al):
    ans = False

    if al.nil:
        ans = False
    elif al.first() == key:
        ans = True
    else:
        al = al.rest()
        ans = recSearch(key, al)
    return ans

print(recSearch(key, al))
