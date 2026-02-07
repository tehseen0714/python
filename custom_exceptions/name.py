class MyError(Exception):
    pass
try:
    name=input("enter your name:")
    if not name.isalpha():
        raise MyError("name should only contain alphabets")
    print("name:",name)
except MyError as e:
    print("custom error,e")





