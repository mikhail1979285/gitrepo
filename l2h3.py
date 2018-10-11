#author=Щилов Михаил
# HARD 3 задание

n=int(input('введи число'))
a=1
y=0
i=1
z=0
s=0
while y<n:
    y=y+a**2
    a=a+1
y=y-(a-1)**2
while i<=(a-2):
    z=z+i
    i=i+1
while s<=(a-1):
    if ((n-y)/(a-1))<s : 
        st=int(1+(n-y)/(a-1))
        slevo=(n-y-((s-1)*(a-1)))
        break
    elif ((n-y)/(a-1))==s:    
        st=int((n-y)/(a-1))
        slevo=(a-1)
        break
    s=s+1      
print('количество столбцов',z+st)
print('слево столбцов',slevo)



