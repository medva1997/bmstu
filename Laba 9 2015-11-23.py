
def trapeze(n):
	trapezeres=0
	step=(b-a)/n
	pos=a
	while(abs(pos-b)>eps):
		trapezeres+=trapezecount(pos,step)
		print(pos,trapezecount(pos,step))
		pos+=step
	return trapezeres

def trapezecount(pos,step):
	left=pos
	right=pos+step
	S=(func(left)+func(right))/2*step
	return S

def func(val):		
	value=val**(2)
	return value

def bulean(n):
	step=(b-a)/(4*n)
	pos=a;
	boleanrez=0
	for i in range(0,n):
		boleanrez+=2*step/45*smallbool(pos,step)
		pos+=step*4
	return boleanrez

def smallbool(pos,step):
	#print(pos,step)
	ln=7*func(pos)
	ln+=32*func(pos+step)
	ln+=12*func(pos+step*2)
	ln+=32*func(pos+step*3)
	ln+=7*func(pos+step*4)
	#print(ln)
	return ln

flag=0
if(flag==0):
	n1=int(input("Введите n1: "))
	n2=int(input("Введите n2: "))
	a=float(input("Введите a: "))
	b=float(input("Введите b: "))
	eps=float(input("Введите eps: "))
else:
	n1=10
	n2=100
	a=1
	b=100
	eps=0.025

#settings	
s="{:^18}|"
G='{:7g}'
S='{:5g}'
lenofline=18*3+3

print()

print((s+s+s).format("Метод  ",n1,n2)) 
print("-"*lenofline)
print((s+s+s).format("Трапеций",G.format(trapeze(n1)),G.format(trapeze(n2))))
print("-"*lenofline)
if((n1)%2==0)and(n2%2==0):
	print((s+s+s).format("Буля    ",G.format(bulean(n1)),G.format(bulean(n2))))
else:
	print("Метод Буля не работает, для нечетного колества интервалов. Вычесление невозможно.")
print()

n3=1
while(abs(trapeze(n3)-trapeze(n3*2))>eps):
	n3=n3*2	
print("Значение интеграла",S.format(trapeze(n3)), "состоящего из",n3, "интерволов удовлетворяет погрешности",eps)
