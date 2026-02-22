def infinite_numbers():
    num=1
    while True:
        yield num
        num+=1

it=infinite_numbers()
print(next(it))
print(next(it))
print(next(it))