import math
x = float(input("Введите x: "))
eps = float(input("Введите Eps: "))
s = 1
factorial = 1
pocazatel = 0
block = 1;

while(((block)>eps)or((-block)>eps)):
    pocazatel = pocazatel+1
    factorial =  factorial*pocazatel
    pocazatel = pocazatel+1
    factorial =  factorial*pocazatel
    block = (x**pocazatel)/factorial
    s = s+block
    #print(block,s,pocazatel,sep = "\t")
print("Сумма последовательности  = ","{:0.4f}".format(s))
    
