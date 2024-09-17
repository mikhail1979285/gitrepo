#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). 
#Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. 
#По возможности доработайте алгоритм (сделайте его умнее).

import random
size = 10
min_item = -100
max_item = 100
array = [random.randint(min_item,max_item-1) for i in range(size)]

print(array)
def p_sort(lst):
    n = 1
    while n < size:
        for i in range(size-n):
            if lst[i] < lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
        n += 1
    return lst               
print(p_sort(array))        