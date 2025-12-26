list=['red','green','white','black','pink','yellow']
new_list=[]
for i in range(len(list)):
 if i!=0 and i!=4 and i!=5:
  new_list.append(list[i])
print(new_list)
