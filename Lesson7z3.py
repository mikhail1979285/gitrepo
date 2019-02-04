#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
#Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random
m = int(input('Введите натуральное число:'))
min_item = 0
max_item = 20
array = [random.randint(min_item,max_item) for i in range(2 * m  + 1)]
print(array)

for i in range(len(array)):
    min_ = 0
    max_ = 0
    for j in range(len(array)):
        if array[i] != array[j]:
            if array[j] > array[i]:
                max_ += 1
            else:
                min_ += 1
    if (min_ == m) and  (max_ == m) :
        print(f'медиана = {array[i]}')
        break 
	
if (min_ != m) and (max_ != m):
	print(f'медиану не получилось найти')		
                
        
        
        
        
    

