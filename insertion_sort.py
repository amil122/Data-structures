#---------------------------------------------------------------Insertion Sort on Strings----------------------------------------------------------------
def insertion_sort_strings(words):
    print("Initial List:", words)
    for i in range(1, len(words)):
        current = words[i]
        j = i - 1
        while j >= 0 and words[j] > current:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = current
        print(f"After inserting '{current}': {words}")

# Test
names = ['amil', 'zayan', 'basil']
insertion_sort_strings(names)
print("Sorted Names:", names)


def insertion_sort(arr):
    print("Initial Array:", arr)
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
        print(f"After inserting {current}: {arr}")

# Test
arr = [12, 6, 32, 9, 44]
insertion_sort(arr)
print("Sorted Array:", arr)
