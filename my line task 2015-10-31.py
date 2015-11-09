Lines=input("Введите строку: ").split()
line=""
symvols=[',',".",'!','?','"',':',';']
for i in range(len(Lines)):
    k=-1;ind=0;s=-1
    for j in range(len(symvols)):
        if(k<0):
            k=Lines[i].find(symvols[j],1)
        if(s<0):
            s=Lines[i].find(symvols[j],0,2)
    if(k>-1)or(s>-1):
      
          print(k)
          if(s<0): s=0
          line+=Lines[i][0:s:1]+Lines[i][k-1:s:-1]+Lines[i][len(Lines[i]):k-1:-1]+" "
          break;
      
    else:
         line+=Lines[i][::-1]+" "
        
    
    
print(line)
print()

flag=1
for i in range(len(Lines)):
    for j in range(len(Lines[i])):        
        if(Lines[i][j]>"А")and(Lines[i][j]<"Я"):
           flag=0 
           
    if(flag==0):
        print(Lines[i],i+1,sep="\t")
    flag=1





    



