#author=Щилов Михаил
# HARD 1 задание 
ur='y=-12x+11111140.2121'
x=2.5 
x=float(x)
plus=ur.find('+')
len_ur=len(ur)
ravno=ur.find('=')
xx=ur.find('x')
neiz1=float(ur[(plus+1):len_ur])
neiz2=int(ur[(ravno+1):xx])
y=neiz2*x+neiz1
print(y)

