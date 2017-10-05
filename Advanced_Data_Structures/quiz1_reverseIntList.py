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
al = al.cons(4)
al = al.cons(3)
print(al)

def reverseList(al):

    newList = IntList()
    while not al.nil:
        newList = newList.cons(al.first())
        al = al.rest()
    return newList

print(reverseList(al))
