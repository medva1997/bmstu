Lines=" "+input("Введите строку: ")+" "
line=""
start=0
end=0

for k in range(0,len(Lines)):
    if(Lines[k]==" "):
        end=k
        break
i=0
temp=""
flag=1

while(end<len(Lines)):   

    for k in range(end-1,start-1,-1):
        temp+=Lines[k]
    
    if(start!=0):
        line+=temp+" "
        
    for j in range(len(temp)):        
        if(temp[j]>"А")and(temp[j]<"Я"):
           flag=0
        if(temp[j]>"A")and(temp[j]<"Z"):
           flag=0
           
    if(flag==0):
        print(temp[::-1],i,sep="\t")
        
    flag=1
    i=i+1    
    start=end+1
    
    if(end+1<len(Lines)):
        for k in range(start,len(Lines)):
            if(Lines[k]==" "):
                end=k
                break
    else:
        end=len(Lines)
        
    temp=""
        
print()

print(line)




