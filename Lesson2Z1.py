#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
#Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

znak = '1'
while  znak!='0': 
    a = int(input('введите первое число '))
    b = int(input('введите второе число '))
    znak = input('введи знак операции') 
    if znak=='+':
        print(a+b)
    elif znak=='-': 
        print(a-b)
    elif znak=='/':
        if znak=='/' and b==0:
            print('деление на 0 невозможно')
        else:
            print(a/b)
    elif znak=='*':
        print(a*b)           
    else:
        while znak not in ('-','+','/','*','0'):
            if znak!='0':
                znak = input('введи еще раз знак операции ')          
        if znak!='0':
            if znak=='+':
                print(a+b)
            elif znak=='-': 
                print(a-b)
            elif znak=='/':
                if znak=='/' and b==0:
                    print('деление на 0 невозможно')
                else:
                    print(a/b)
            elif znak=='*':
                print(a*b)         
print('END')    