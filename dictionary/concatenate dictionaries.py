d1={1:1,2:2,3:3}
d2={4:4,5:5,6:6}
d3={7:7,8:8,9:9}
dict={}
for d in(d1,d2,d3):
    for key in d:
        dict[key]=d[key]
print(dict)