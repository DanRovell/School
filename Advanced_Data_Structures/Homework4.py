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



#delete key

def recDelete(al, key):

    if al.nil:
        nl = al
    elif key == al.first():
        nl = al.rest()
    else:
        fl = recDelete(al.rest(), key)
        nl = fl.cons(al.first())

    return nl

key = 7
print(recDelete(al, key))
