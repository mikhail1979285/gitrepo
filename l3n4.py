# Задача-4 NORMAL  
#author=Щилов Матвей

x1=4
y1=4
x2=4
y2=2
x3=3
y3=3
x4=5
y4=3

if (abs(x2-x1)==abs(x4-x3) and abs(y2-y1)==abs(y4-y3)):
    print('точки являются вершинами параллелограмма')
elif (abs(x2-x3)==abs(x1-x4) and abs(y2-y3)==abs(y1-y4)):
	print('точки являются вершинами параллелограмма')
else:
    print('фигня')
	
