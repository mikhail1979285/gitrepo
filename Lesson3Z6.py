#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать
# Щилов Михаил
import random

size = 10
min_item = 1
max_item = 20
max_chislo = 0
sum_= 0
array = [random.randint(min_item,max_item) for i in range(size)]
print(f'исходный массив {array}')
for i in range(size):
    if array[i] > max_chislo:
        max_chislo = array[i]
        max_index = i
min_chislo=max_chislo       
for k in range(size):       
    if array[k] < min_chislo:
        min_chislo = array[k]
        min_index = k
for i in range(size):
    if array[i] > min_chislo and array[i] < max_chislo:
        sum_ = sum_ + array[i]	
		
print(f'сумма элементов, находящихся между минимальным и максимальным элементами равно {sum_} ')		

