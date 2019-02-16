#1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, 
#состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.


def hesh_opr(s,subs):
    sum_=0
    spisok_podstr = podstr.split(",")
    for j in range(len(spisok_podstr)):
        h_subs=hash(spisok_podstr[j])
        len_subs = len(spisok_podstr[j])
        for i in range(len(s) - len_subs + 1):
            if h_subs == hash(s[i:i + len_subs]):
                sum_+=1
    return sum_       

str = input('Введите строку:')
podstr = input('Введите подстроку:')

print(hesh_opr(str,podstr))