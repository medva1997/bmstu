""" Вариант 8"""
k=int(input("Введите к: "))
F=[]*5
temp=[]
for i in range(k):
    temp=list(map(int,input("введите строку матрицы: ").split()))
    F.append(temp)
    
temp=[]
j=k-1

#ниже диагонали
while(j>=0):
    summ=0
    step=0
   
    while((j+step)<k):
        summ+=F[j+step][step]
        step=step+1        
    j-=1
    temp.append(summ)
    
#Выше диагонали
j=1
while(j<k):    
    step=0
    summ=0    
    while((j+step)<k):
        summ+=F[step][j+step]
        step=step+1   
    j+=1
    temp.append(summ)

print("Исходная матрица")
for i in range(k):
    for j in range(k):
       print(F[i][j],end=" ")
    print()
print()

print("Результирующий вектор")
for i in range(len(temp)):
     print(temp[i],end=" ")
print()
print()
ind=temp.index(max(temp))
temp[ind],temp[len(temp)-1]=temp[len(temp)-1],temp[ind]
print("Перобразованный вектор")
for i in range(len(temp)):
     print(temp[i],end=" ")
print()

