#7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n=int(input('Введите  натуральное число n: '))
rav1=0
i=0
rav2=int(n*(n+1)/2)
while i<n:
    i+=1
    rav1=rav1+i
if rav1==rav2:
    print(f'равенство 1+2+..+n=n(n+1)/2 верно, так как левое равенство равно ={rav1} и  правое равенство равно ={rav2}')       