"Поиск корней квадратного уравнения"

import math
print("Решения уравнения вида ax^2+bx+c=0")
a = int(input("Введите, пожалуйста, коэффицент a="))    
b = int(input("Введите, пожалуйста, коэффицент b="))
c = int(input("Введите, пожалуйста, коэффицент c="))
if(a!=0):
    D=b*b-4*a*c
    if (D<0) :
          print("Нам очень жаль,но корней среди действительных чисел нету.")
    elif D==0 :
          X=(-b)/(2*a)
          print("Корень всего один:\n X =",'{:.4f}'.format(X))
    elif (D>0) :
          X1=((-b)+math.sqrt(D))/(2*a)
          X2=((-b)-math.sqrt(D))/(2*a)
          print("У уравнения два корня:\n")
          print("X1 =",'{:.4f}'.format(X1))
          print("X2 =",'{:.4f}'.format(X2))
else:
    if (b!=0):
            print("Внимание, коэффицент a=0, это не квадратное уравнение, но его ответ:")
            print("X=",'{:.4f}'.format(-c/b))
    else:
        if(c==0):
             print("X может быль любым.")
        else:
            print("Введенные данные неверны.")