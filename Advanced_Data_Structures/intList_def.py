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

print(al.nil)

al = al.cons(7)
al = al.cons(6)
al = al.cons(5)

#print each of the items in the List
def printL(al):

    while not al.nil:
        print(al.first())
        al = al.rest()

printL(al)
