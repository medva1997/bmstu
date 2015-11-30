def tree(n):
    step=(b-a)/n
    summ=0
    pos=a
    while(pos<b):
        summ+=3*step/8*(func(pos)+func(pos+3*step)+3*func(pos+step)+3*func(pos+2*step))
        pos+=step*3
    #print(n, summ)
    return summ


def counttree1(x,step):
    summ=0
    while (x<b-step):
        summ+=func(x)+ func(x+step*2)
        x=x+step*3
    return summ
    
def counttree2(x,step):
    summ=0
    x=x+step
    while (x<b-step):
        summ+=func(x)
        x=x+step*3
    return summ

def func(x):
    return x**2

a=float(input("Ведите левую гранцу вычесления интеграла: "))
b=float(input("Ведите правую гранцу вычесления интеграла: "))
eps=float(input("Ведите точность: "))
n=3
while(abs(tree(n)-tree(n*2))>eps):
    n=n*2
print("При",n,"разбиениях значение интеграла составляет:",
      "{:7f}".format(tree(n)),",что удовлетворяет погрешности",eps)

