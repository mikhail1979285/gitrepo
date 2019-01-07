#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Щилов Михаил
import random

size = 20
min_item = -100
max_item = 100
array = [random.randint(min_item,max_item) for i in range(size)]
max_chislo = min_item
print(f'исходный массив {array}')
for i in range(size):
    if array[i] < 0 and  array[i] > max_chislo :
            max_chislo = array[i]
            max_index = i
print(f' максимальный отрицательный элемент  {max_chislo} и его индекс {max_index} ')