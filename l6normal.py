# Задание-1: 6 урок normal Щилов Михаил
class Teacher:
    def __init__(self, teacher_surname, subject, class_room):
        self.teacher_surname = teacher_surname
        self.subject = subject
        self.class_room = list(class_room)


teachers=[Teacher('Sidorov', 'Math',('5С','5А','7А')),
          Teacher('Ivanov', 'Russia',('5С','5В','7А')),
          ]
     
def spisok_predmetovvklasse():
    b=str(input('введите класс, по которому нужен список предметов:')) 
    list_pred=[] 
    for i in teachers:
        a=list(i.class_room)
        for v in a:
            full_name=i.teacher_surname
            if str(v)==str(b):
                list_pred.append(full_name)
    print("в {} классе преподают:{} ".format(b,list_pred))
spisok_predmetovvklasse() 

class Student:
    def __init__(self, name, surname, mother_surname, father_surname, class_room):
        self.name = name
        self.surname = surname
        self.mother_surname = mother_surname
        self.father_surname = father_surname
        self.class_room = class_room

  



students = [Student("Александр", "Петров", "Петрова", "Петров", "5А"),
            Student("Петр", "Сидоров","Сидорова", "Сидоров", "8Б"),
            Student("Иван", "Иванов","Иванова", "Иванов", "5А"),
            ]


def roditeli():
    name_s=str(input('введите фамилию студента, по которому надо узнать родителей:'))
    for i in students:
        a=str(i.surname)
        if a==name_s:
            print("Фамилия Мамы -{} Фамилия Папы -{} ".format(i.mother_surname,i.father_surname))
           
    #student.next_class()
roditeli()
    
def spisok_vklasse():
    b=input('введите класс, по которому нужен список учеников:') 
    list_uch=[] 
    for i in students:
        a=str(i.class_room)
        if a==b:
            full_name=i.name+' '+i.surname
            list_uch.append(full_name)
            #list_uch.append(i.surname)
            #print("Ученик {} класса , Имя {}, Фамилия {}".format(b,i.name,i.surname))
    print("в {} классе учаться:{} ".format(b,list_uch))
spisok_vklasse() 
           
def spisok_vsehklassov():
    list_new=[]   
    for i in students:
        #a=str(i.class_room)
        list_new.append(i.class_room)
    l=[list_new[i] for i in range(len(list_new)) if i==list_new.index(list_new[i])]
    print('список всех классов',l)
    
spisok_vsehklassov()            

