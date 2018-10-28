# Задание-1: 7 урок normal Щилов Михаил
import random
import sys
 
 
ballsp = 89
igrok = 15 # количество цифр  на карточке  игрока
comp = 15 # количество цифр на карточке компьютера
balls = random.sample(range(1,91),90)
vsenomera = random.sample(range(1,91), 30)
nomigroka = random.sample(vsenomera, 15)
karta_igroka = [nomigroka[:5], nomigroka[5:10], nomigroka[10:]]
for stroka in karta_igroka:
    stroka.sort()
    stroka.insert(random.randint(0, 4), ' ')
    stroka.insert(random.randint(0, 5), ' ')
    stroka.insert(random.randint(0, 6), ' ')
    stroka.insert(random.randint(0, 7), ' ')
nomcomp = [i for i in vsenomera if not i in nomigroka]	
karta_comp = [nomcomp[:5], nomcomp[5:10], nomcomp[10:]]
for stroka in karta_comp:
    stroka.sort()
    stroka.insert(random.randint(0, 4), ' ')
    stroka.insert(random.randint(0, 5), ' ')
    stroka.insert(random.randint(0, 6), ' ')
    stroka.insert(random.randint(0, 7), ' ')
 
 
 
def kartochki():
        print('{:-^24}'.format(' Ваша карточка '))
        for line1 in karta_igroka:
            for n1 in line1:
                print('{}'.format(n1),end=' ') 
            print()
        print('{:-^24}'.format('-'))
        print('{:-^24}'.format(' Карточка компьютера '))
        for line2 in karta_comp:
            for n2 in line2:
                print('{}'.format(n2), end=' ')
            print()
        print('{:-^24}'.format('-'))
 
 
def move():
    if ball in nomcomp:
        for i in karta_comp:
            try:
                print('номер выпал на карточке компьютера')
                i.insert(i.index(ball), '><')
                i.pop(i.index(ball))
            except ValueError:
                continue
        return 2 
    a = input('Зачеркнуть цифру? (y/n): ')
    if a == 'y':
        if ball in nomigroka:
            for l in karta_igroka:
                try:
                    l.insert(l.index(ball), '><')
                    l.pop(l.index(ball))
                except ValueError:
                    continue
            print('ВЕРНО')
            return 0
        else:
            print('Игра закончена ')
            sys.exit()
    elif a == 'n':
        if ball in nomigroka:
            print('Игра закончена ')
            sys.exit()
        else:
            print('ВЕРНО')
            return 1
    else: 
        print('Не верно введена буква') 
        return move() 

 
for ball in balls:
    print('Номер нового  бочонка: {} (осталось еще : {} бочонков '.format(ball, ballsp))
    kartochki() 
    f=move()
    if f == 0:
        igrok -= 1
        ballsp -= 1
    elif f == 2:      
        comp -= 1
        ballsp -= 1
    elif f == 3:
        pass    
    else: 
        ballsp -= 1
    if igrok == 0:
        print('Ты выиграл')
        sys.exit()
    if comp == 0:
        print('Ты проиграл')
        sys.exit()
    if ballsp == 0:
        print('Игра закончена')
        sys.exit()
 