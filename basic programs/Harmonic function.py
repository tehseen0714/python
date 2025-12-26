n=int(input("enter the value of n:"))
if n<=0:
    print("n must be greater than 0.")
else:
     harmonic=0.0
     for i in range (1,n+1):
          harmonic +=1/i
          print("nth harmonic values is:",harmonic)
          