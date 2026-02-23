def count_down(start):
    while start>0:
        yield start
        start-=1
for i in count_down(10):
    print(i)