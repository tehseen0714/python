def my_decorator(funct):
    def wrapper():
        print("after function execution")
        funct()
        print("after function execution")
    return wrapper
@my_decorator
def say_hello():
    print("hello!!!")
say_hello()
