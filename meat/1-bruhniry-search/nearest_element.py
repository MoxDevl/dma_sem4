# Returns index of the number with least absolute difference.
# If there's is two with equal difference, returns the lesser index.
def nearest_element(arr : list, boy : int) -> int:
    start = 0
    end = len(arr)-1

    while end-start > 1:
        middle = (end+start)//2
        if boy <= arr[middle]:
            end = middle
        else:
            start = middle

    return start if abs(arr[start]-boy) <= abs(arr[end]-boy) else end


# INPUT
# n - length of array
# x - key for lower_bound()
n, x = input().split()
# inputing the array
arr = [float(x) for x in input().split()]

# OUTPUT
# Returns index
print(nearest_element(arr, float(x)))