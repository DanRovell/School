#Define a function to return an IntList that is the result of inserting
#an integer i, before another in key given an original IntList called al.

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
al = al.cons(9)
al = al.cons(1)
al = al.cons(3)

def insert(i, key, al):

    if al.nil:
        nl = al
    elif key == al.first():
        nl = al.cons(i)
    else:
        tl = insert(i, key, al.rest())
        nl = tl.cons(al.first())

    return nl

print(insert(10, 3, al))
