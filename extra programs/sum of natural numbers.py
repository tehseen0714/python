number=int(input("enter natural number to find sum:"))
if number<0:
    print("enter a natural number")
else:
    sum=0
    while(number>0):
     sum+=number
print("sum is:",sum)