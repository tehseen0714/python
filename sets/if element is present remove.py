set={1,2,3,4,5,6,7,8}
for i in set.copy():
    if i==8:
        set.remove(i)
        print(set)
        