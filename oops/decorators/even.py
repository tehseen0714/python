def check_even(funct):
    def wrapper(n):
        if n%2==0:
            funct(n)
        else:
            print("not even")
    return wrapper
@check_even
def show(n):
    print("even number:",n)
show(7)