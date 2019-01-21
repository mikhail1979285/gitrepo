#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и 
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple
from collections import defaultdict

size = int(input('Введите количество предприятий'))
baza_class = namedtuple('baza_class',['name', 'kv1' ,'kv2', 'kv3', 'kv4'])
vivod_class = namedtuple('vivod_class',['x', 'y'])
baza = []
vivod = []
vse_pr =0
sr = 0
for i in range(size):
   name = str(input('Введите наименование '))
   kv1 = int(input('Введите прибыль за 1 квартал '))
   kv2 = int(input('Введите прибыль за 2 квартал '))
   kv3 = int(input('Введите прибыль за 3 квартал '))
   kv4 = int(input('Введите прибыль за 4 квартал '))
   vse_pr = vse_pr + kv1 + kv2 + kv3 + kv4
   new_company = baza_class(name,kv1,kv2,kv3,kv4)
   baza.append(new_company)

sr_pr = vse_pr / size

for i in range(size):
   if (baza[i].kv1 + baza[i].kv2 + baza[i].kv3 + baza[i].kv4) < sr_pr:
       new_company = vivod_class('у этих фирм прибыль ниже среднего',baza[i].name)
   elif (baza[i].kv1 + baza[i].kv2 + baza[i].kv3 + baza[i].kv4) == sr_pr:   
       new_company = vivod_class('у этих фирм прибыль равна средней',baza[i].name)
       sr = 1
   else:    
        new_company = vivod_class('у этих фирм прибыль больше  средней',baza[i].name)
   vivod.append(new_company)

q = defaultdict(list)
for key,value in vivod:
    q[key].append(value)
print('у этих фирм прибыль ниже среднего',q['у этих фирм прибыль ниже среднего'])
print('у этих фирм прибыль больше средней',q['у этих фирм прибыль больше  средней'])
if sr > 0:
    print('у этих фирм прибыль равна средней',q['у этих фирм прибыль равна средней'])






