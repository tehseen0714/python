def my_decorator(funct):
    def wrapper(name):
        print("welcome!!!")
        funct(name)
        print("thank you!!!")
    return wrapper
@my_decorator
def greet(name):
    print("hello",name)
greet("tehseen")