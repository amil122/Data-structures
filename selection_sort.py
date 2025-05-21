
# ---------------------------------------------------------------------------------SELECTION SORT -------------------------------------------------------------------------------------------
list1 = [33,189,4,0,23,90.2,189]
for i in range(len(list1)):
    min_value = min(list1[i:])
    min_value_index = list1.index(min_value,i)
    list1[i],list1[min_value_index]= list1[min_value_index],list1[i]
    print(list1)
print(list1)




list1=[32,53,21,3,12,0,32,53]
for i in range(len(list1)-1):
    min_val_index = i
    for j in range(i+1,len(list1)):
        if list1[j]<list1[min_val_index]:
            min_val_index= j
    if list1[i] != list1[min_val_index]:
        list1[i],list1[min_val_index]=list1[min_val_index],list1[i]
    
print(list1)
            
            
        
list1 = [32, 1, 53, 29, 0]
for i in range(len(list1)):
    min_index = i
    for j in range(i + 1, len(list1)):
        if list1[j] < list1[min_index]:
            min_index = j
    list1[i], list1[min_index] = list1[min_index], list1[i]
print("Sorted List:", list1)
