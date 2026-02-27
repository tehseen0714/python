def my_decorator(funct):
    def wrapper(a,b):
        result=funct(a,b)
        return result*2
    return wrapper
@my_decorator
def add(a,b):
    return a+b
print(add(3,4))