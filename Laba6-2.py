m=int(input("Введите M: "))
n=int(input("Введите N: "))
flag=False
foundFirst=False;
Found_last=False;
D =[[0] * (m-1)] * n
G=[]

for i in range(n):
        while(len(D[i])!=m):
                if(flag==True):
                        print("Ошибка ввода. Введите строку еще раз")
                D[i]=list(map(int,input("Введите строку массива через пробел: ").split())) 
                flag=True
        flag=False
        G.append(min(D[i]))

indexfirst=-1
while((foundFirst==False)and(indexfirst<n)):
	indexfirst=indexfirst+1
	if(G[i]>0):
		foundFirst=True
		ind1=indexfirst	

indexlast=n
while((Found_last==False)and(indexlast>0)):
	indexlast=indexlast-1
	if(G[i]>0):
		Found_last=True	
		ind2=indexlast

if(Found_last==False)and(foundFirst==False):
	print("Положительных элементов в массиве G нету")
else:
	#print(ind1,ind1)
	G[ind1],G[ind2]=G[ind2],G[ind1]
	
print()
print("Масссив G: ")
print(G)

print()
print("Масссив D: ")

for i in range(n):
        for j in range(m):
                print(' {:^5}|'.format('{:.4g}'.format(D[i][j])),sep="",end="")
        print(" ")
        
        
