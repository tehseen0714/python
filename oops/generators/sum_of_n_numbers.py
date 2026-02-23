def sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
        yield total

for i in sum(5):
    print(i)