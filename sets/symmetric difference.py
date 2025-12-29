set1={1,2,3,4,5}
set2={1,2,6,7,8}
set3=set()
for i in set1:
    if i not in set2:
     set3.add(i)

for j in set2:
   if j not in set1:
      set3.add(j)
print(set3) 