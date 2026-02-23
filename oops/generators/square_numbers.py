def squares(n):
    for i in range (1,n+1):
        yield i*i

for i in squares(7):
    print(i)