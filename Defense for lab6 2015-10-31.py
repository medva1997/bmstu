m=int(input("Введите M: "))
n=int(input("Введите N: "))
arr=[[0]*m for i in range(n)]
count=2
i=0
j=0
summline=0
maxsumm=0
for i in range(n):
    for j in range(m):
        if(i==j):
            arr[i][j]=0            
        if(i>j):
            arr[i][j]=1            
        if(i<j):
            arr[i][j]=count
            count=count+1        
        summline=summline+arr[i][j]
    summline=summline/m
    if(maxsumm<summline):
        maxsumm=summline
    summline=0   
    


for i in range(n):
    for j in range(m):
            print(' {:^5}|'.format('{:.4g}'.format(arr[i][j])),sep="",end="")
    print(" ")
print('Максимальное среднее арифметическое: {:^5}'.format('{:.4g}'.format(maxsumm)))
    
