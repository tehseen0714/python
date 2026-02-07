class MyError(Exception):
    pass
try:
    age=int(input("Enter age:"))
    if age<18:
        raise MyError("age must be above 18 to vote")
    print("you are eligible to vote")
except MyError as e:
    print("custom erroe:",e)