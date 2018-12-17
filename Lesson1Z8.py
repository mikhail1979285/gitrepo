X = int(input('введите год '))
Y = X % 400
if Y == 0:
    print('Год високосный')
else:
    Y = X % 100
    if Y == 0:
            print('Год невисокосный')
    else:
        Y = X % 4
        if Y == 0:
            print('Год високосный')
        else:
            print('Год невисокосный')       
