#l=int(input("Ведите длинну массива S: "))
b=list(map(int,input("Введите массив b через пробел: ").split()))
s=[]
t=[]
t=list(map(int,input("Введите массив t через пробел: ").split()))

out='{:.4g}'

summa=1;
indexofmax=0;
s.append(1);
proiz=1
for i in range(0,len(t)):
	proiz=proiz*(t[i]+1)	
for k in range(1,len(b)):
	#print(b[k],proiz)

	if(b[k]>0):
		s.append(s[k-1]+proiz*b[k])
		#print("доб1 ",s[k])
	else:
		s.append(s[k-1])
		#print("доб2 ",s[k])
	if(k%2==0):
		summa=summa+s[k]
	if(s[indexofmax]<s[k]):
		indexofmax=k

print("Порядковый номер максимального: ",out.format(indexofmax+1))
print("Значение максимального: ",out.format(s[indexofmax]))
#print(s[indexofmax])
s[indexofmax]=summa-s[indexofmax]


#for k in range(0,len(b)):
print("Массив С")
print(s)


#1 2 -1 0 3 -3
#5 4 3 2 1 -2
