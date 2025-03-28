# Find index of the peak number
def peak(arr : list) -> int:
    start = 0
    end = len(arr)-1
    
    while end-start > 1:
        middle = (end+start)//2
        if arr[middle] < arr[middle+1]:
            start = middle
        else:
            end = middle
    
    return end if arr[start] <= arr[end] else start

# INPUT
# n - length of array
n = input()
# inputing the array
arr = [float(x) for x in input().split()]

# OUTPUT
# Returns index
print(peak(arr))