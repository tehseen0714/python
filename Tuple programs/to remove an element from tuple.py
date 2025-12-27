tuple=(1,2,3,4,5)
number=3
new_tuple=()
for i in tuple:
    if i!=number:
        new_tuple=new_tuple+(i,)
print(new_tuple)