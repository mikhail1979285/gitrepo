#author=Щилов Михаил
# HARD 2 задание
data=input('введите дату:')
len=len(data)
a=int(data[0:2])
b=int(data[3:5])
c=int(data[6:10])
if (len==10 and (a+b+c)>=0):   
    if (c>=1 and c<=9999 and (b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12)):
        if (a>=1 and a<=31):
            print('корректная дата')
        else: 
            print('Некорректная дата')
    elif (c>=1 and c<=9999 and (b==2 or b==4 or b==6 or b==9 or b==11)): 
        if (a>=1 and a<=30):
            print('корректная дата')
        else: 
            print('Некорректная дата')   
    else: 
        print('Некорректная дата')			
else: 
    print('Некорректная дата')
#дата =  ' 01.22.1001 '
#date =  ' 1.12.1001 '
#date =  ' -2.10.3001 '