"""Составить программу вычисления суммы ряда с точностью до члена ряда меньшего Е
Производить печать текущих значений суммы и количества членов ряда. Окончательное
значение суммы и количества также должны быть напечатаны. Исходные данные вводить.
Также вводится начальное значение N и шаг для печати. Текущие значения печатаются
в таблице. Окончательное значение вывести вне таблицы. Если ряд не сошелся за N
циклов, то выдать сообщение.
Карточка №93

Z=1-1/2*x+(1*3)/(2*4)*x^2-(1*3*5)/(2*4*6)*x^3+.....
-1<x<=1
"""


import math, sys

Flag_input_validation=False
while Flag_input_validation==False:
    x=float(input("Введите значение параметра x (-1<x<=1): "))
    if((x<=1)&(x>-1)):
        Flag_input_validation=True
    else:
        print("Ошибка ввода! Повторите ввод.")

Flag_input_validation=False
while Flag_input_validation==False:
    N=int(input("Введите макс. длинну ряда: "))
    if((N>=1)):
        Flag_input_validation=True
    else:
        print("Ошибка ввода! Повторите ввод.")

Flag_input_validation=False
while (Flag_input_validation==False):
    Startpos =int(input("Введите номер эл. с которого нужно начать вывод: "))
    if((Startpos>=1)):
        Flag_input_validation=True
    else:
        print("Ошибка ввода! Повторите ввод.")

Flag_input_validation=False
while Flag_input_validation==False:
    Printstep=int(input("Введите шаг печати: "))
    if((Printstep>=1)):
        Flag_input_validation=True
    else:
        print("Ошибка ввода! Повторите ввод.")

Flag_input_validation=False
while Flag_input_validation==False:
    Eps=float(input("Введите значение погрешности E: "))
    if((Eps>=0)):
        Flag_input_validation=True
    else:
        print("Ошибка ввода! Повторите ввод.")

Z=0             #сумма
proisup=1       #Числитель
proisdown=1     #Знаменатель
lastcurrent=0;      #Значение блока произведения 
lasti=-1        #Количество пройденных итераций при выходе из цикла

print("Порядковый №","Cумма      ","Тек. Значение",sep='\t')
if(N>0):
    Z=proisup/proisdown*math.pow(x,0)
    if(Startpos-1==0):
        print(1,'{:.4f}'.format(Z),Z,sep='\t\t')
    lasti=1

# цикл
for i in range (1,N):
    #обновляем числитель и знатенатель дроби
    proisup=proisup*(2*i-1)
    proisdown=proisdown*(2*i)

    #опредяляем нужен ли минус перед блоком
    if(i%2==0):
        current=proisup/proisdown*math.pow(x,i)
    else:
        current=(-1)*proisup/proisdown*math.pow(x,i)

    Z=Z+current     #обновление суммы

    if(((i+1-Startpos)%Printstep==0)&(i>=Startpos-1)):    # печать с нужным шагом
        print(i+1,'{:.4f}'.format(Z),'{:2.3e}'.format(current),sep='\t\t')

    #Выход если наш блок меньше E
    if (abs(current)<Eps):
        lasti=i+1
        #print(i+1,'{:.4f}'.format(Z),'{:2.3e}'.format(current),sep='\t\t')
        break

    
else:
    print()
    print("Значение не найдено.")

if(lasti>1):
    print(" ")
    print("Итоговое значение выражения=",'{:.4g}'.format(Z))
    print("Элемент последовательности под номером",lasti," равен ",'{:.4g}'.format(current),"что меньше Eps")
