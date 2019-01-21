# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
first = deque(input('введите первое число:'))
second = deque(input('введите второе число:'))
sum_f = 0
sum_s = 0
def Int(n):
    try:
        int(n) 
        return True
    except ValueError:
        return False
    

for i in range(len(first)):
    if Int(first[i]) is True:
        chislo = int(first[i]) * (16 ** (len(first)-1-i))
    else:
        if first[i]=='A':
            chislo = 10 * (16 ** (len(first)-1-i))
        elif first[i]=='B':
            chislo = 11 * (16 ** (len(first)-1-i))
        elif first[i]=='C':
            chislo = 12 * (16 ** (len(first)-1-i))
        elif first[i]=='D':
            chislo = 13 * (16 ** (len(first)-1-i))
        elif first[i]=='E':
            chislo = 14 * (16 ** (len(first)-1-i))
        elif first[i]=='F':
            chislo = 15 * (16 ** (len(first)-1-i))   
        else: 
            print('неверное введено первое число')
            break       
    sum_f = sum_f + chislo
    
for i in range(len(second)):
    if Int(second[i]) is True:
        chislo = int(second[i]) * (16 ** (len(second)-1-i))
    else:
        if second[i]=='A':
            chislo = 10 * (16 ** (len(second)-1-i))
        elif second[i]=='B':
            chislo = 11 * (16 ** (len(second)-1-i))
        elif second[i]=='C':
            chislo = 12 * (16 ** (len(second)-1-i))
        elif second[i]=='D':
            chislo = 13 * (16 ** (len(second)-1-i))
        elif second[i]=='E':
            chislo = 14 * (16 ** (len(second)-1-i))
        elif second[i]=='F':
            chislo = 15 * (16 ** (len(second)-1-i))   
        else: 
            print('неверное введено второе число')
            break
    sum_s = sum_s + chislo

sum_ = sum_f + sum_s
proiz_= sum_f * sum_s
 
array = deque()
newarray = deque()
array_pr = deque()
newarray_pr = deque()
ost = sum_
while sum_ > 16:
    ost = sum_ % 16
    sum_ = sum_ // 16
    array.append(ost)

array.append(sum_) 
array.reverse()

while proiz_ > 16:
    ost = proiz_ % 16
    proiz_ = proiz_ // 16
    array_pr.append(ost)

array_pr.append(proiz_) 
array_pr.reverse()


for i in range(len(array)):
    if int(array[i]) == 10:
        newarray.append('A')
    elif int(array[i]) == 11:
        newarray.append('B')
    elif int(array[i]) == 12:
        newarray.append('C')
    elif int(array[i]) == 13:
        newarray.append('D')
    elif int(array[i]) == 14:
        newarray.append('E')
    elif int(array[i]) == 15:
        newarray.append('F') 
    else:
        newarray.append(array[i])    

for i in range(len(array_pr)):
    if int(array_pr[i]) == 10:
        newarray_pr.append('A')
    elif int(array_pr[i]) == 11:
        newarray_pr.append('B')
    elif int(array_pr[i]) == 12:
        newarray_pr.append('C')
    elif int(array_pr[i]) == 13:
        newarray_pr.append('D')
    elif int(array_pr[i]) == 14:
        newarray_pr.append('E')
    elif int(array_pr[i]) == 15:
        newarray_pr.append('F') 
    else:
        newarray_pr.append(array_pr[i])   

print(f'сумма чисел равно {newarray},произведение чисел равно {newarray_pr}')

