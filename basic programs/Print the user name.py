username=input("enter your name (minimum 3 characters):")
if len(username)>=3:
    template= "Hello  <<username>>, How are you?"
    final_string=template.replace( " <<username>>",username)
    print(final_string)
else:
    print( " user name should have atleast 3 characters.")