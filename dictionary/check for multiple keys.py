dict={'1':10,'2':20,'3':30,'4':40}
keys=['1','2']
found=True
for k in keys:
    if k not in dict:
        found=False
else:
    print("keys exist")