list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i][1]>list[j][1]:
            list[i],list[j]=list[j],list[i]
print(list)            