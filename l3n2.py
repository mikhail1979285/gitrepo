# Задача-2 NORMAL:
#author=Щилов Михаил



def sort_to_max(origin_list):
    len_o=len(origin_list)
    new_list=[]
    i=0
    while i<len_o:
        number=min(origin_list)
        for key in origin_list:     
           if number<key:
               number=key
        origin_list.remove(number)
        new_list.append(number)   
        i=i+1      
    new_list.reverse()
    print(new_list)
                           
def sort_to_max1(origin_list):
    len_o=len(origin_list)
    for j in range(0,len_o-1):
        for i in range(0,len_o-j-1):     
           if origin_list[i]>origin_list[i+1]:
               origin_list[i],origin_list[i+1]=origin_list[i+1],origin_list[i]
    print(origin_list)                 


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
sort_to_max1([2, 10, -12, 2.5, 20, -11, 4, 4, 0])