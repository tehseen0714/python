class MyError(Exception):
    pass
try:
    password=input("enter your password:")
    if len(password)<10:
        raise MyError("password should contains atleast 10 characters")
    print("password accepted")
except MyError as e:
    print("custom error",e)

