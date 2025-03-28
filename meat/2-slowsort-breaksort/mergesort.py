# O(n) memory mergesort
def mergesort(arr : list, left : int = 0, right : int = None, buf : list = None, counter = 0) -> None:

    if right is None:
        right = len(arr)-1
    if buf is None:
        buf = [None]*len(arr)

    if right == left:
        buf[right] = arr[right]
        return

    middle = (left+right)//2
    mergesort(arr, left, middle, buf, counter+1)
    mergesort(arr, middle+1, right, buf, counter+1)

    ind1 = ind2 = 0    
    for i in range(left, right+1):
        if ind1 >= middle-left+1:
            arr[i] = buf[middle+1+ind2]
            ind2 += 1
        elif ind2 >= right-middle:
            arr[i] = buf[left+ind1]
            ind1 += 1
        elif buf[left+ind1] <= buf[middle+1+ind2]:
            arr[i] = buf[left+ind1]
            ind1 += 1
        else:
            arr[i] = buf[middle+1+ind2]
            ind2 += 1
    buf[left:right+1] = arr[left:right+1]


# INPUT
# n - length of an array
n = input()
# inputing the array
arr = [int(x) for x in input().split()]

mergesort(arr)

# OUTPUT
# Returns index
print(arr)