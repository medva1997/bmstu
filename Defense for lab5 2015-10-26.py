a=float(input("Начальное значение: "))
d=float(input("Конечное значение: "))
step=float(input("Шаг: "))
countsteps=round((d-a)/step)
pos=a
arr=[]
for i in range(countsteps+1):
    y=pos*pos-25
    arr.append(y)    
    pos=pos+step
mmin=round((min(arr)-min(arr))/(max(arr)-min(arr))*50+5)
mmax=round((max(arr)-min(arr))/(max(arr)-min(arr))*50+5) 
m0=round((0-min(arr))/(max(arr)-min(arr))*50+5)

x=a

for i in range(countsteps+1):
    m=round((arr[i]-min(arr))/(max(arr)-min(arr))*50+5)
    if(m0>0)and (m0<=mmax):            
            if(m<m0):
                print(" "*m,"*"," "*(m0-m-1),"|",sep='')
            if(m==m0):
                print(" "*m,"*"," "*(70-m),sep='')
            if(m>m0):
                print(" "*(m0),"|"," "*(m-m0-1),"*",sep='')
    else:
                       
            if(m<m0):
                print( " "*m,"*",sep='')
            if(m==m0):
                print(" "*m,"*",sep='')
            if(m>m0):
                print(" "*(m),"*",sep='')
    
            
    x=x+step
        

    

 
        

