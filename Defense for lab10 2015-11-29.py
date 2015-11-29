lines=[]
lines.append("Семен пишет защиту строк. Сергей сдает строки. Давид")
lines.append("катается на стуле. Ира cмотрит к Кате. Я пишу защиту по")
lines.append("строкам вот так проходит наша лаба по проге.")
line=""
for i in range(len(lines)):
    line+=lines[i]+" "
sentenses=line.split(".")

for i in range(0,len(sentenses),2):
    maxlit=""
    maximum=0
    #print(sentenses[i])
    for j in range(len(sentenses[i])):
        if(sentenses[i][j]!=" "):
            if(sentenses[i].count(sentenses[i][j])>maximum):
                maximum=sentenses[i].count(sentenses[i][j])
                maxlit=sentenses[i][j]
    print(maxlit)


