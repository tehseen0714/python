def primes(limit):
    for num in range(2,limit+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            yield num

for p in primes(20):
    print(p)