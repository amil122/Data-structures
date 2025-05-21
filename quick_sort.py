

# ###########################################################################################QUICK-SORT################################################################################
#example one 
import random
def pivot_element(list1, first, last):
    random_value = random.randint(first,last)
    list1[last],list1[random_value]= list1[random_value],list1[last]
    pivot_value = list1[last]
    left = first 
    right = last - 1 
    while True:
        while left <= right and list1[left] <= pivot_value:
            left += 1
        while left <= right and list1[right] >= pivot_value:
            right -= 1
        if right < left:
            break
        list1[left], list1[right] = list1[right], list1[left]
    list1[last], list1[left] = list1[left], list1[last]
    return right

def quicksort(list1, first, last):
    if first < last:
        p = pivot_element(list1, first, last)
        quicksort(list1, first, p - 1)
        quicksort(list1, p + 1, last)

list1 = [34,32,41,6,2,13,493,83,34]
first = 0
n = len(list1)-1
quicksort(list1,first,n)
print(list1)


#example 2
import statistics
def pivot_element(list1,first,last):
    low = first
    high = last
    mid = (low+high)//2
    pivot_index = statistics.median([low,mid,high])
    if pivot_index == low :
        pivot_value = first
    elif pivot_index == high :
        pivot_value = last
    else:
        pivot_value = mid
    list1[last],list1[pivot_value] = list1[pivot_value],list1[last]
    pivot_element = list1[last]
    left = first
    right = last - 1
    while True:
        while list1[left]<=pivot_element and left<= right :
            left = left + 1
        while list1[right]>= pivot_element and left<= right :
            right = right - 1
        if right < left :
            break
        list1[left],list1[right] = list1[right],list1[left]
    list1[last],list1[left] = list1[left], list1[last]
    return left


def quicksort(list1,first,last):
    if first<last:
        p = pivot_element(list1,first,last)
        quicksort(list1,first , p -1)
        quicksort(list1,p+1,last)
        
list1 = [23,4,19,34,83,92,0]
first = 0
n = len(list1)-1
quicksort(list1,first, n)
print(list1)


# example 3

def pivot_element(list1,first,last):
    pivot_element = list1[first]
    left = first + 1
    right = last
    while True:
        while list1[left]<= pivot_element and  left <= right :
            left = left + 1
        while list1[right]>= pivot_element and left <= right :
            right = right - 1
        if right < left :
            break
        list1[left],list1[right] = list1[right],list1[left]
    list1[first],list1[right] = list1[right],list1[first]
    return right



def quicksort(list1, first, last):
    if first < last:
        p = pivot_element(list1, first, last)
        quicksort(list1, first, p - 1)
        quicksort(list1, p + 1, last)

list1 = [3, 534, 28, 2, 0]
first = 0
last = len(list1) - 1
quicksort(list1, first, last)
print("Sorted list:", list1)  # Add this line to print the sorted list