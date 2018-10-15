# Задача-1 NORMAL:
#author=Щилов Михаил

def fibonacci(n, m):
    fibonacci_list=[1,1,2] 
    i=0
    while i<(m-3):
        new=int(fibonacci_list[-1])+int(fibonacci_list[-2])
        print('число:', new)
        fibonacci_list.append(new)
        i=i+1
    print(fibonacci_list[n:]) 
 
 
fibonacci(5,10)