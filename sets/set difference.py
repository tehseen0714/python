set1={1,2,3,4,5,6}
set2={2,3,4,5,6}
set3=set()
for i in set1:
  if i not in set2:
    set3.add(i)
print(set3)    