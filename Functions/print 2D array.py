def print_array():
    row=int(input("Enter number of rows:"))
    cols=int(input("Enter number of colums:"))
    arr=[]
    print("Enter elements:")
    for i in range(row):
        row=[]
        for j in range(cols):
            row.append(int(input()))
        arr.append(row)
    print("2D array:")
    for row in arr:
        for value in row:
            print(value,end="")
        print()    
print_array() 