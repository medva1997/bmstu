"""
Задача 2.28
Дан одномерный массив P(L) L<=12. Расположить в начале массива
положительные элементы, затем нулевые, в конце отрицательные.
Дополнительный массив не вводить. Для ввода-вывода данных организовать
дополнительные циклы.

"""

#arr=list(map(float,input("Введите элементы через пробел: ").split()))
n=int(input("Введите количество элементов массива: "))
arr=[]
for i in range(0,n):
	arr.append(int(input("Элемент равен: ")))	

k = int(input("Введите количество элементов для печати на одной строке: "))

arr = [x for x in arr if x > 0] + [x for x in arr if x == 0]+\
        [x for x in arr if x <0]
        
for i in range(len(arr)):
    if (i+1) % k == 0:
        print(arr[i])
    else:
        print(arr[i],end=' ')


