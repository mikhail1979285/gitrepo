import random
import time
class XO:
    def __init__(self, nomer, mesto_g, mesto_v, znak='_'): #nomer- для обозначения ячейки, mesto- Список в виде координат, znak - по умолчанию это пустой знак
        self.nomer = nomer
        self.mesto_g = mesto_g
        self.mesto_v = mesto_v
        self.znak = znak


Pole=[XO(1,1,1),XO(2,1,2),XO(3,1,3),XO(4,1,4),XO(5,1,5),XO(6,2,1),XO(7,2,2),XO(8,2,3),XO(9,2,4),XO(10,2,5),XO(11,3,1),XO(12,3,2),XO(13,3,3),XO(14,3,4),
      XO(15,3,5),XO(16,4,1),XO(17,4,2),XO(18,4,3),XO(19,4,4),XO(20,4,5),XO(21,5,1),XO(22,5,2),XO(23,5,3),XO(24,5,4),XO(25,5,5)]

Pole1=[]
def greatspisok():
    for i in range(1,26):
        Pole1.append(i)
        
def printpole():  
    print ("-------------------------")
    for i in range(5):
        if i>=2:
            print ("|", Pole1[0+i*5], "|", Pole1[1+i*5], "|", Pole1[2+i*5], "|", Pole1[3+i*5], "|", Pole1[4+i*5], "|")
        else:
            print ("| ", Pole1[0+i*5], "| ", Pole1[1+i*5], "| ", Pole1[2+i*5], "| ", Pole1[3+i*5], "| ", Pole1[4+i*5], "|")     
        print ("------------------------")   

          

def input_token(token):
    a=int(input("Введите номер ячейки, куда поставить : "+' '+ token + ' '))
    for i in range(0,25):
        if Pole1[i]==a:
            Pole1[i]=str(token)        
    printpole()  

def check_win(Pole1):
    win_pole=((0,1,2),(1,2,3),(2,3,4),(5,6,7),(6,7,8),(7,8,9),(10,11,12),(11,12,13),(12,13,14),(15,16,17),(16,17,18),(17,18,19),(20,21,22),(21,22,23),(22,23,24),(2,6,10),(3,7,11),(7,11,15),(4,8,12),(8,12,16),(12,16,20),(9,13,17),(13,17,21),(14,18,22),(2,8,14),(1,7,13),(7,13,19),(0,6,12),(6,12,18),(12,18,24),(5,11,17),(11,17,23),(10,16,22),(0,5,10),(5,10,15),(10,15,20),(0,5,10),(5,10,15),(10,15,20),(0,5,10),(5,10,15),(10,15,20),
              (1,6,11),(6,11,16),(11,16,21),(2,7,12),(7,12,17),(12,17,22),(3,8,13),(8,13,18),(13,18,23),(4,9,14),(9,14,19),(14,19,23),
              )
    for i in win_pole:
        if Pole1[i[0]]==Pole1[i[1]]==Pole1[i[2]]:
            return Pole1[i[0]]
    return False        
           
    
def main():
    greatspisok()  
    schetchik=0 
    win=False
    printpole()
    while not win:
        input_token("X")
        schetchik+=1
        win=check_win(Pole1)
        if win:
            print(win, "Выиграл")
            win=True
            break
        input_token("O")
        schetchik+=1
        win=check_win(Pole1)
        if win:
            print(win, "Выиграл")
            win=True
            break
        if schetchik==25:
           print('Ничья')
           break
           

    
def poiskhoda_ii(token):
    if token=="X":
        a="O"   
    else:
        a="X"
    win_pole=((0,1,2),(1,2,3),(2,3,4),(5,6,7),(6,7,8),(7,8,9),(10,11,12),(11,12,13),(12,13,14),(15,16,17),(16,17,18),(17,18,19),(20,21,22),(21,22,23),(22,23,24),(2,6,10),(3,7,11),(7,11,15),(4,8,12),(8,12,16),(12,16,20),(9,13,17),(13,17,21),(14,18,22),(2,8,14),(1,7,13),(7,13,19),(0,6,12),(6,12,18),(12,18,24),(5,11,17),(11,17,23),(10,16,22),(0,5,10),(5,10,15),(10,15,20),(0,5,10),(5,10,15),(10,15,20),(0,5,10),(5,10,15),(10,15,20),
              (1,6,11),(6,11,16),(11,16,21),(2,7,12),(7,12,17),(12,17,22),(3,8,13),(8,13,18),(13,18,23),(4,9,14),(9,14,19),(14,19,23),
              )
    for i in win_pole:
        if  Pole1[i[0]]==Pole1[i[1]]==a:
            return Pole1[i[2]]
        elif Pole1[i[1]]==Pole1[i[2]]==a:
            return Pole1[i[0]]  
        elif Pole1[i[0]]==Pole1[i[2]]==a:
            return Pole1[i[1]]      
    return False 
    
def go_ii(token):
    print("Ходит и думает",token)
    time.sleep(5)
    f=False
    a=random.randint(1,25)
    print(token,"пошел на клетку",a)
    for i in range(0,25):
        if Pole1[i]==a:
            Pole1[i]=str(token)
            f=Pole1[i]          
    if f:
        pass
    else:    
        print("эта клетка занята")
        go_ii(token)         
    printpole() 
    
def main_ii():
    greatspisok()  
    schetchik=0 
    win=False
    printpole()
    while not win:
        go_ii("X")
        schetchik+=1
        win=check_win(Pole1)
        if win:
            print(win, "Выиграл")
            win=True
            break
        go_ii("O")
        schetchik+=1
        win=check_win(Pole1)
        if win:
            print(win, "Выиграл")
            win=True
            break
        if schetchik==25:
           print('Ничья')
           break
           
def zapusk():
    a=int(input("Введите 1, если будет играть игрок с игром и 2 если играет ИИ с ИИ : "))        
    if a==1:
        main()
    if a==2:
        main_ii()       

zapusk()    