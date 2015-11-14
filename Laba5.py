"""
Вычислить таблицу значений функций, результаты вычислений оформить в 
виде заголовка с таблицей
№53
z(x) =x*sin(ln(x) -pi/4)
y(x)=x/2 *sqrt(x*x+1)-ln(x+sqrt(x*x+1))
    x=1(0.05)2

    оператор for
Определить также сумму максимальных значений этих функций
№3
печатать в виде графика 2-ое, 4-ое, 6-ое и тд значение х
Нулевую линию печатать если она есть
"""

import math
arrZ=[]
arrY=[]

Flag_input_validation=False
while Flag_input_validation==False:
    start=float(input("Начальное значение: "));
    if((start>0)):
        Flag_input_validation=True
    else:
        print("Ошибка ввода! Повторите ввод.")

step=float(input("Значение шаг: "));

Flag_input_validation=False
while Flag_input_validation==False:
    end=float(input("Конечное значение: "));
    if((start<end)):
        Flag_input_validation=True
    else:
        print("Ошибка ввода! Повторите ввод.")

#start=100
#step=10
#end=1500

print('{:^18}|{:^18}|{:^18}'.format("x","Z(x)","Y(x)"))  
x=start
numofsteps=math.trunc((end-start)/step)+1

x=start
for i in range(0,numofsteps):
    
    # Вычисление значений при текущем х
    tempz=x*math.sin(math.log(x)-math.pi/4)
    tempy=x/2*math.sqrt(x*x+1)-math.log(x+math.sqrt(x*x+1))
    #Сохранение значений в массивы
    arrZ.append(tempz)
    arrY.append(tempy)
    if(tempz<0)and(tempy<0):
        print('{:<18}|  {:<18}|  {:<18}'.format('{:.3g}'.format(x),
                                        '{:.3g}'.format(tempz),
                                        '{:.3g}'.format(tempy))) 
    elif(tempz<0)and(tempy>0):
        print('{:<18}|  {:<18}|   {:<18}'.format('{:.3g}'.format(x),
                                        '{:.3g}'.format(tempz),
                                        '{:.3g}'.format(tempy))) 
    elif(tempz>0)and(tempy<0):
        print('{:<18}|   {:<18}|  {:<18}'.format('{:.3g}'.format(x),
                                        '{:.3g}'.format(tempz),
                                        '{:.3g}'.format(tempy))) 
    elif(tempz>0)and(tempy>0):
        print('{:<18}|   {:<18}|   {:<18}'.format('{:.3g}'.format(x),
                                        '{:.3g}'.format(tempz),
                                        '{:.3g}'.format(tempy))) 
    
    
    
    x=x+step



print()
maxsumm=max(arrY)+max(arrZ)

print("Сумма максимальных значений функций: ",'{:.3g}'.format(maxsumm))
print()

if((max(arrZ)>0)and(min(arrZ)<0)):
    arrY,arrZ=arrZ,arrY
    print('{:^60}'.format("График функции Z(x)"))
else:
    if((max(arrY)>0)and(min(arrY)<0)):
        print('{:^60}'.format("График функции Y(x)"))
    else:
        print('{:^60}'.format("Ни один из графиков не пересекает ось X"))
        print('{:^60}'.format("График функции Y(x)"))


# Вычесление положения основых точек

stepforprint=(max(arrY)-min(arrY))/70

steplen=max(arrY)-min(arrY)
mmax=round((max(arrY)-min(arrY))*stepforprint)
mmin=round((min(arrY)-min(arrY))/(steplen)*50+5)
m0=round((0-min(arrY))/steplen*50+5)
#print(m0)

print('{:^6}'.format("X"))

x=start

# Посторение графика
for i in range(0,numofsteps):
    m=round((arrY[i]-min(arrY))/(steplen)*50+5)
    if(i%2==0):
        
        #print(m,m0,mmax)
               
        if(m0>0):
                if(m<m0):
                    print('{:^10}'.format('{:.4g}'.format(x))," "*m,
                        "*"," "*(m0-m-1),"|",sep='')
                if(m==m0):
                    print('{:^10}'.format('{:.4g}'.format(x))," "*m,
                        "*"," "*(70-m),sep='')
                if(m>m0):
                    print('{:^10}'.format('{:.4g}'.format(x))," "*(m0),
                                         "|"," "*(m-m0-1),"*",sep='')
            
            #print(" "*m,"*",sep='')
        else:
            if(m<m0):
                    print('{:^10}'.format('{:.4g}'.format(x))," "*m,
                        "*",sep='')
            if(m==m0):
                    print('{:^10}'.format('{:.4g}'.format(x))," "*m,
                        "*",sep='')
            if(m>m0):
                    print('{:^10}'.format('{:.4g}'.format(x))," "*(m),
                        "*",sep='')
            

       

    if(i%2==1):
            # Положение каретки для текущего значения            
            
            if(m0>0):
                if(m<m0):
                    print('{:^10}'.format(" ")," "*m,"*",
                    " "*(m0-m-1),"|",sep='')
                if(m==m0):
                    print('{:^10}'.format(" ")," "*m,"*",
                                         " "*(70-m),sep='')
                if(m>m0):
                    print('{:^10}'.format(" ")," "*(m0),
                                         "|"," "*(m-m0-1),"*",sep='')
            
            else:
                if(m<m0):
                    print(' '*10," "*(m),"*",sep='')
                if(m==m0):
                    print(' '*10," "*(m),"*",sep='')
                if(m>m0):
                    print(' '*10," "*(m),"*",sep='')           

    x=x+step
            

print(" "*3,"↓")
print(" "*3,"X")
