
# ////////////////////////////////////////////////////////////////////////////////MERGE SORT//////////////////////////////////////////////////////////////////////////////////////////

def mergesort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i = 0
        j = 0
        k = 0
        while i<len(left_list) and  j < len(right_list):
            if left_list[i]>right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else :
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i + 1
            j = j + 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j  + 1
            k = k + 1

list1 = [43,2,92,0,21,53]
mergesort(list1)
print(list1)




def mergesort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list  = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i = 0 
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i]<= right_list[j]:
                list1[k] = left_list[i]
                i = i + 1 
                k = k + 1
            else:
                list1[k]= right_list[j]
                j = j + 1
                k = k + 1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i + 1 
            k = k + 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1


list1= [23,4,13,53,21,33,93]
mergesort(list1)
print(list1)