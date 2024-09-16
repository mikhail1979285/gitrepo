a = int(input('введите первое число'))
b = int(input('введите второе число'))
c = int(input('введите третье число'))
if a > b:
    if a <c:
        print(f'среднее число = {a}')
    else:
        if c > b:
            print(f'среднее число = {c}')
        else:
            print(f'среднее число = {b}')       
else:
    if b < c:
        print(f'среднее число = {b}')
    else:   
        if a > c: 
            print(f'среднее число = {a}')
        else:
            print(f'среднее число = {c}')       

            
    
