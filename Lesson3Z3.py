#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
# Щилов Михаил
import random

size = 10
min_item = 1
max_item = 20
max_chislo = 0
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
array[max_index],array[min_index]=min_chislo,max_chislo
print(f'массив в котором поменялись максимальный {max_chislo} и минимальный {min_chislo} элемент{array}')
