""" Вариант 7"""
n=input("Введите строку с символами без пробелов: ")  
for i in range(122,96,-1):
    kol=n.count(chr(i))+n.count(chr(i-32))
    if(i%2==0):
        print('Буква "',chr(i),",",chr(i-32),'" = ',kol,sep="",end="\t\t")
    else:
        print('Буква "',chr(i),",",chr(i-32),'" = ',kol,sep="")
        
    
    

