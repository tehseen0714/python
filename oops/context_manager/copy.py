with open("sample.txt","r") as f1:
    with open("copy.txt","w") as f2:
        f2.write(f1.read())