#author=Щилов Михаил
# normal 1 задание
import math

my_list = [1, 3, 9, 3.45, 'ddd', 's', 333,25,64]
new_list=[]
for x in my_list:
    if type(x)==int:
        if math.sqrt(x)%1==0:
            new_list.append(int(math.sqrt(x)))
print(new_list)