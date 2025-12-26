list=['abc','xyz','aba','1221']
count=0
for word in list:
    if len(word)>=2 and word[0]==word[-1]: 
     count+=1
print(count)        
