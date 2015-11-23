""" Вариант 3"""
#массив символов, для добавления в множество
literal=["q","z","w","s","x","d","c","r","f","v","t","g","b","h","n","j","m","k","l","p"]
dic=set()
for i in range(20):
    dic.add(literal[i])
    
line=input("Введите строку: ")
line=line.lower()
lines=line.split()
b=len(lines)
words=[]


for i in range(b):
    words.append(set())
    for j in range(len(lines[i])):
        words[i].add(lines[i][j])
#print(words)

for i in range(len(words)):
    dic=set.intersection(words[i],dic)
    #print(dic)
print("Найденные повторяющиеся буквы: ",dic)



