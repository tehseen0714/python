N=int(input("Enter value of N (0<=N<31):"))
if N<0 or N>=31:
    print("N must be between 0 and 30.")
else:
    for i in range (N+1):
        print(f"2^{i}={2**i}") 