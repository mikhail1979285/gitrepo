#4. Определить, какое число в массиве встречается чаще всего
# Щилов Михаил
import random

size = 20
min_item = 1
max_item = 20
array = [random.randint(min_item,max_item) for i in range(size)]
max_index = 0
print(f'исходный массив {array}')
for i in range(size):
    item = 1
    for k in range(i+1,size):
        if array[i] == array[k]:
            item+=1
            chislo = array[i]
        if item > max_index:    
            max_chislo = chislo
            max_index = item
print(f' Число ={max_chislo} встречается больше всего раз,  а точнее - {max_index} раз')     