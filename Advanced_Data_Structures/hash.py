
def hashCode(k):
    return (5*k)%8

for k in [1055,1492,1776,1812,1918,1945]:
    print(hashCode(k))
