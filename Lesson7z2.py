#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
#Выведите на экран исходный и отсортированный массивы

import random
size = 10
min_item = 0
max_item = 50
array = [random.uniform(min_item,max_item-1) for i in range(size)]
print(array)

def sort_(left, right):
    lst = []
    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if len(left) > 0:
        lst.extend(left)
    else:
        lst.extend(right) 
    return lst
 
def mid_sort(lst):
    if len(lst) >= 2:
        middle = int(len(lst) / 2)
        lst = sort_(mid_sort(lst[:middle]), mid_sort(lst[middle:]))
    return lst
    
print(mid_sort(array))  