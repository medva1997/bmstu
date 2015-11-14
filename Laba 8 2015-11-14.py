lines=input("Введите строку: ").split()
#lines='Сережа сказал Семе: "Дай, пожалуста,
#предметы: ручку, ластик или тетрадь. Ура!".'.split()

line=""
b=['"','.',',','!',':',';',';','?']
#print(lines)
for i in range(0,len(lines)):
    st=-1
    en=0    

    if(lines[i][0]==b[0]):
        st=0;
    for j in range(1,len(lines[i])):
        for k in range(0,len(b)):
            #print(lines[i],i,j,k)
            if(lines[i][j]==b[k]):
                en=j-1
                break
        if(en!=0):
            break
    
    if(st==0):
        line+=lines[i][0]+lines[i][j-1:0:-1]+lines[i][j:len(lines[i]):1]+" "
    else:
        if(en==0):
            line+=lines[i][::-1]+" "
        else:
            line+=lines[i][en::-1]+lines[i][en+1:len(lines[i]):1]+" "
    st=-1
    en=0
print(line)


print()

flag=1
for i in range(len(lines)):
    for j in range(len(lines[i])):        
        if(lines[i][j]>"А")and(lines[i][j]<"Я"):
           flag=0 
           
    if(flag==0):
        print(lines[i],i+1,sep="\t")
    flag=1

