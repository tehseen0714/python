n=int(input("enter a number:"))
if n<=1:
    print("enter a number greater than 1.")
else:
    print("prime factors are:")
    i=2
    while i*i<=n:
        while n%i==0:
            print(i)
            n//=i
    if n>1:
        print(n)i
