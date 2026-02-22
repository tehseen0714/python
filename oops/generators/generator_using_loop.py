def print_numbers(n):
    for i in range(1,n+1):
        yield i

for num in print_numbers(5):
    print(num)