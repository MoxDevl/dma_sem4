# Returns index of the first element what is not less than `boy`.
# If there's none, returns -1.
def lower_bound(arr : list, boy : int) -> int:
    start = 0
    end = len(arr)-1

    while end-start > 1:
        middle = (end+start)//2
        if boy <= arr[middle]:
            end = middle
        else:
            start = middle

    if (boy <= arr[start]):
        return start
    return end if boy <= arr[end] else -1


# INPUT
# n - length of array
# x - key for lower_bound()
n, x = input().split()
# inputing the array
arr = [float(x) for x in input().split()]

# OUTPUT
# Returns index or -1
print(lower_bound(arr, float(x)))