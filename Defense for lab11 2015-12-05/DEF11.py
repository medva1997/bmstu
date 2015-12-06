def read():
	readfile=open("compslist.txt","r")
	for line in readfile:
		sql.append(line.split(";"))
	readfile.close()

def printer():
	for i in range(len(sql)):
		print(sql[i][0],sql[i][1],sql[i][2],sep="\t")

def vendor(name):
	i=0
	name=name.lower()
	while(i<len(sql)):
		temp=sql[i][0].lower()
		if(temp!=name): 
			sql.remove(sql[i])
			i-=1
		i+=1
		
def cpu(tact):
	i=0
	tact=tact.lower()
	while(i<len(sql)):
		temp=sql[i][1].lower()
		if(temp!=tact): 
			sql.remove(sql[i])
			i-=1
		i+=1
		
def disk(volume):
	i=0
	while(i<len(sql)):
		if(int(sql[i][2])!=int(volume)): 
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
print("Поиск по категориям:")
print("		1. Марка")
print("		2. Тактовая частота")
print("		3. Объем винчестера")

task=int(input("Укажите номер категории: "))
if task == 1: vendor(input("Введите марку: "));    
elif task == 2: cpu(input("Введите тактовую частоту: "));  
elif task== 3: disk(int(input("Введите гобъем винчестера: ")));
      
printer()
writer()
