Lines=input("Введите строку: ").split()
line=""
for i in range(len(Lines)):
    line+=Lines[i][::-1]+" "
print(line)

flag=1
for i in range(len(Lines)):
    for j in range(len(Lines[i])):        
        if(Lines[i][j]>"А")and(Lines[i][j]<"Я"):
           flag=0 
           
    if(flag==0):
        print(Lines[i],i)
    flag=1
                



