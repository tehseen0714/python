def fibonacci(limit):
    a,b=0,1
    while a<=limit:
     yield a
     a,b=b,a+b

for i in fibonacci(10):
   print(i)