lines=[]
bigline=""
n=0
flag=0
if (flag==1):
	print("Для завершения ввода,оставьте стрку пустой и нажите Enter")
	while(n!=-1):
		line=input("Введите строку: ")
		if(line!=""):
			lines.append(line)
		else:
			n=-1
	print(lines)
else:
	lines.append("Усадьба Кусково - родовая усадьба, построенная")
	lines.append("в семнадцатом веке, привлекает к себе внимание ценителей и")
	lines.append("посетителей. Уникальный архитектурный ансамбль, парковые")
	lines.append("интерьеры и здания, авторами которых были выдающиеся")
	lines.append("архитекторы своего времени. Абракадабра абракадабра Абракадабра Абракадабра абракадабра Абракадабра абракадабра Абракадабра абракадабра Абракадабра абракадабра Абракадабра абракадабра абракадабра Абракадабра абракадабра Абракадабра абракадабра Абракадабра абракадабра Абракадабра абракадабра Абракадабра абракадабра Абракадабра абракадабра. Они сделали ее любимым местом")
	lines.append("отдыха, обязательным пунктом экскурсионных поездок")
	lines.append("и уникальным местом съемок любых исторических фильмов.")


for i in range(len(lines)):
	bigline+=lines[i]+" "
#bigline=bigline.lower()
biglines=bigline.split(".")
#print(bigline)
maxwords=0
forprint=""
for i in range(len(biglines)):
	flag=True
	for j in range(len(biglines[i])):
		if(biglines[i][j]!=",")and (biglines[i][j]!=".")and \
		 (biglines[i][j]!=",") and((biglines[i][j]!="-")):
			if((biglines[i].count(biglines[i][j].lower())+
				biglines[i].count(biglines[i][j].upper()))<2):
				flag=False
				#print("False",biglines[i][j])
				break
		
		if(flag==False):
			break	
	biglines[i]+="."
	biglines[i]=biglines[i].split()

	if(flag==True):
		if(maxwords<len(biglines[i])):
			maxwords=len(biglines[i])
			forprint=""
			for j in range(maxwords):
				forprint+=biglines[i][j]+' '
		
if(forprint==". "):
        print("Предложение удовлетворяющее условию не найдено.")
else:
        print(forprint)
