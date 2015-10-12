import random
n=int(input("Введите длину массива "))
arr=[]
index=0;
while(index<n):    
    temp=random.randint(1,100)
    for i in range(0,index):
        if(temp==arr[i]):
           break;
    else:
        arr.append(temp)
        index=index+1
        
print(arr);
    
