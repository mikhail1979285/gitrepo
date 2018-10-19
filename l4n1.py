# Задание-1:
#author=Щилов Михаил
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более высокий характер в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить свой двух способов: с помощью re и без.
import re
line =  'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO ' \
       ' GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK ' \
       ' TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn ' \
       ' LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqGAWdJsOvqppOfyIVjXa ' \
       ' pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete ' \
       ' kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ ' \
       ' WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb ' \
       ' JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC ' \
       ' EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB ' \
       ' tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT ' \
       ' SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu ' \
       ' UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB ' \
       ' qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa ' \
       ' XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ ' \
       ' zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc '
found = re.findall(r'[a-z]+', line)
print(found)



numbers_under_4 = []
nachalo=0
schet=-1
schet_z=0
for number in line:
    schet+=1 
    if 'a'<=number<='z':
        schet_z=0
    else: 
        if schet_z==0: 
            schet_z+=1
            str=line[nachalo:schet]
            nachalo=schet+1
            numbers_under_4.append(str)
        else:
            nachalo=schet+1  			
print(numbers_under_4) 



