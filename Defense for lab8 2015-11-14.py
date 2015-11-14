value=[["M",1000],["D",500],["C",100],["L",50],["X",10],["V",5],["I",1]]
line=" "+input("Введите римское число: ")
res=0
last=8
for i in range(len(line)-1,0,-1):
    for j in range(len(value)-1,-1,-1):
        if(value[j][0]==line[i]):
            if(j<=last):
                res+=value[j][1]
                #print("pl",res,value[j][1])
            if(j>last):
                res-=value[j][1]
                #print("mn",res,value[j][1])
            last=j
print(res)
        
    
    

