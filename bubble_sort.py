def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [40, 10, 30, 20]
print("Before sorting:", arr)

bubble_sort(arr)

print("After sorting:", arr)



# Bubble Sort and Count Duplicates

list1 = [3, 6, 8, 2, 6, 1, 3, 8, 3, 6]

# Step 1: Bubble Sort
n = len(list1)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print("Sorted List:", list1)

# Step 2: Count Duplicates
duplicates = {}
for num in list1:
    if num in duplicates:
        duplicates[num] += 1
    else:
        duplicates[num] = 1

# Optional: Filter only actual duplicates
actual_duplicates = {k: v for k, v in duplicates.items() if v > 1}

print("Duplicate Counts:", actual_duplicates)