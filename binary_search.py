def binary_search(arr, tar):
    low = 0
    high = len(arr) - 1  # Corrected to len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if tar == arr[mid]:
            print("Target found at index", mid)
            return mid
        elif tar > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    print("Target not found in the list")
    return -1

# Example usage
arr = [1, 2, 4, 5, 6, 79]
tar = 1
binary_search(arr, tar)



#------------------------------------------------------------------Recursive Binary search-----------------------------------------------------------------

def binary_recursive(arr, tar, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return binary_recursive(arr, tar, start, mid - 1)
    else:
        return binary_recursive(arr, tar, mid + 1, end)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tar = 5
res = binary_recursive(arr, tar, 0, len(arr) - 1)

if res != -1:
    print("Target found at index", res)
else:
    print("Target not found in the list")
