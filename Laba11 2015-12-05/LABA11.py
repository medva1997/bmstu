def read():
	readfile=open("preztablewin.txt","r")
	for line in readfile:
		sql.append(line.split(";"))
	readfile.close()

def printer():
	for i in range(len(sql)):
		print(sql[i][0],sql[i][1],sql[i][2],sep="\t")

def country(area):
	i=0
	area=area.lower()
	while(i<len(sql)):
		temp=sql[i][0].lower()
		if(temp!=area): 
			sql.remove(sql[i])
			i-=1
		i+=1

def people(name):
	i=0
	name=name.lower()
	while(i<len(sql)):
		temp=sql[i][1].lower()
		if(temp.find(name)<0): 
			sql.remove(sql[i])
			i-=1
		i+=1

def year(date):
	i=0
	while(i<len(sql)):
		if(int(sql[i][2])!=date): 
			sql.remove(sql[i])
			i-=1
		i+=1

def writer():
	f = open('out.txt', 'w')
	for i in range(len(sql)):
		f.write(sql[i][0]+'\t'+sql[i][1]+'\t'+sql[i][2]+'\n')
	f.close()

sql=[]
read()
if(input("Для вывода на экран считанного файла нажмите 'Y' ")=="Y"): printer()
print("Поиск осуществляется по следущим категориям:")
print("		1. Страна")
print("		2. Президент")
print("		3. Год вступления в должность")

tasks=[]
tasks=list(map(int,input("Через пробел укажите категории для поиска: ").split()))
for i in range(len(tasks)):
	if tasks[i] == 1: country(input("Введите страну: "));    
	elif tasks[i] == 2: people(input("Введите имя президента: "));  
	elif tasks[i] == 3: year(int(input("Введите год вступления в должность: ")));
printer()
writer()
