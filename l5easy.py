import os
import sys
import shutil

#print(sys.argv)

# создание копии текущего файла
shutil.copyfile(__file__,'new_file.py')

#print(os.getcwd())
#print(os.path)
#print(os.path.dirname(os.path.abspath(__file__)))
#print(os.listdir(os.path.dirname(os.path.abspath(__file__))))


# вывод директорий из текущей директории
def spisok_dir_vtekdir():
    with os.scandir(os.path.dirname(os.path.abspath(__file__))) as i:
        for entry in i:
            if entry.is_dir():
                print(entry.name)
            
            
#spisok_dir_vtekdir()            

# создании директорий dir_1...9
def dir_sozdanie():
    for i in range(1,9):
        d='dir_'
        s=str(i)
        dir_new=d+s
        dir_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),dir_new)
        try:
            os.mkdir(dir_path)
            print("директория {}создана".format(dir_new))    
        except FileExistsError:
            print("Такая директория {} существует".format(dir_new))
# удаление  директорий dir_1...9    
#dir_sozdanie()


    
def dir_udalenie():
    for i in range(1,9):
        d='dir_'
        s=str(i)
        dir_new=d+s
        dir_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),dir_new)
        try:
            os.rmdir(dir_path)
            print("директория {}удалена".format(dir_new))    
        except FileExistsError:
            print("Такая директория{} не существует".format(dir_new))

        
#dir_udalenie()

def make_dir():
    dir_name=input("введите имя директории, которую Вы хотите создать")
    if not dir_name:
        print("необходимо ввести имя директории")
        return
    dir_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),dir_name)
    try:
        os.mkdir(dir_path)
        print("директория {} успешно создана".format(dir_name))
    except FileExistsError:
        print("директорию  {} невозможно создать, так как она уже существует".format(dir_name))

def remove_dir():
    dir_name=input("введите имя директории, которую Вы хотите удалить")
    if not dir_name:
        print("необходимо ввести имя директории")
        return
    dir_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),dir_name)
    try:
        os.rmdir(dir_path)
        print("директория {} успешно удалена".format(dir_name))
    except FileExistsError:
        print("директорию  {} невозможно создать, так как не существует".format(dir_name))
        
def change_dir():
    print("текущая папка",os.getcwd()) 
    dir_name=input("введите имя папки ,в которую Вы хотите перейти")
    if not dir_name:
        print("необходимо ввести имя папки, в которую Вы хотите перейти")
        return
    dir_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),dir_name)
    try:
        os.chdir(dir_path)
        print("переход в папку {} успешно завершен".format(dir_name))
        print("текущая папка",os.getcwd())
    except FileExistsError:
        print("переход в папку {} невозможно, так как папка не существует ".format(dir_name))
        
def print_help():
    print("1 - перейти в папку")
    print("2 - посмотреть  директории в текущей папке")
    print("3 - удалить папку")
    print("4- создать папку")  
    print("5- создать папки с наименованиями dir_1...9")
    print("6- удалить папки с наименованиями dir_1...9")
    key=int(input('введите цифру: '))   
    print(key)
    if key==4:
        make_dir()
    elif key==3:
        remove_dir()
    elif key==1:
        change_dir()
    elif key==2:
        spisok_dir_vtekdir()
    elif key==5:
        dir_sozdanie()
    elif key==6:
        dir_udalenie()        
    else:
        print("задана неправильная цифра")

    

