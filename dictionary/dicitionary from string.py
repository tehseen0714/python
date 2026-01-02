string="w3resource"
d={}
for ch in string:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)