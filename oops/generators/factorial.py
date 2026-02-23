def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        yield fact

for i in factorial(5):
    print(i)