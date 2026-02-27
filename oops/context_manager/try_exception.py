try:
    with open("sample.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")

        
        