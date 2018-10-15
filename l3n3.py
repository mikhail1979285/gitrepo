# Задача-3 NORMAL  
#author=Щилов Михаил
li=[2, 10, -12, 2.5, 20, -11, 4, 4, 0]

def func(list):
    numbers_under_4 = []
    for number in list:
         if number < 4:
             numbers_under_4.append(number)
    print(numbers_under_4)  
	
print(func(li))