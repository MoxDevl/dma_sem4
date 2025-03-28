from random import randint

# in-place quicksort
def quicksort(arr : list, left : int = 0, right : int = None) -> None:
    if right is None:
        right = len(arr)-1

    if left < 0 or right <= left:
        return

    pindex = randint(left, right)
    p = arr[pindex]

    for i in range(pindex+1, right+1):
        if arr[i] <= p:
            arr.insert(left, arr.pop(i))
            pindex += 1
    for i in range(pindex, left, -1):
        if arr[i] > p:
            arr.insert(pindex, arr.pop(i))
            pindex -= 1

    quicksort(arr, left, pindex-1)
    quicksort(arr, pindex+1, right)
    

# INPUT
# n - length of an array
n = input()
# inputing the array
arr = [int(x) for x in input().split()]

quicksort(arr)

# OUTPUT
# Returns index
print(arr)