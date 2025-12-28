tuple=(1,1,2,2,3,3,4,4,5,5)
repeated=[]
for i in range(len(tuple)):
    for j in range(i+1,len(tuple)):
        if tuple[i]==tuple[j] and tuple[i] not in repeated:
          repeated.append(tuple[i])
print(repeated)
