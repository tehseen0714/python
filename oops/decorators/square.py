def my_decorator(funct):
    def wrapper(x):
        result=("value is:",x)
        funct(x)
    return wrapper
@my_decorator
def square(x):
  print("square:",x*x)
square(4)