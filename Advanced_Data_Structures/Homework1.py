# Binary Search

def binarySearch(List, key):

    ans = -1
    first = 0
    last = len(List)-1

    while first <= last:
        mid = int((first + last)/2)
        if List[mid] == key:
            ans = mid
            return ans
        else:
            if List[mid] > key:
                last = mid - 1
            else:
                first = mid + 1
    return ans

List = [4,7,2,23,9,11,52,78,5,6]
key = int(input("Please enter an integer: "))
List.sort()
print(List)
print(binarySearch(List, key))
