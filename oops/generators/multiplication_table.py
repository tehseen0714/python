def table(num):
    for i in range(1,11):
     yield num*i

for i in table(7):
   print(i) 