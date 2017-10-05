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

key = 6

#search for key
def search(key, al):

    ans = False
    while not al.nil:
        if al.first() == key:
            ans = True
            break
        else:
            al = al.rest()
    return ans

print(search(key, al))
