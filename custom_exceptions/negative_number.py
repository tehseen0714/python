
   num=int(input("enter a number:"))
   if num<0:
       raise MyError("negative numebrs are not taken")
   print("valid number:",num)
except MyError as e:
    print("custom error:",e)