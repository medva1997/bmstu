""" Вариант 2"""
D=input("Введите строку D: ")
L=[]
F=""
print("<<<Для выхода из ввода подстрок программы введите: -1>>>")
while(F!="-1"):
    F=input("Введите подстроку F: ")
    flag=True
    for i in range(len(F)):
        kolF=F.count(F[i])
        kolD=D.count(F[i])
        if(kolF>kolD):
            flag=False
            break
    temp=[F,flag]
    
    if(F!="-1"):
        L.append(temp);
    flag=True
print(D)

for i in range(len(L)):       
    if(L[i][1]==False):
        s=print("\tF - '",L[i][0],"' (нельзя составить)",sep='')
    else:
        print("\tF - '",L[i][0],"' (можно составить)",sep='')    
      

