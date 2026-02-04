class address_book:
    contacts={}
    def create_address_book(self):
        full_name=input("Enter your full name:")
        phone=input("enter your number:")
        address=input("enter your address:")
        pincode=int(input("Enter pincode:"))
        state=input("Enter state:")
        address_book.contacts[full_name]=[phone,address,pincode,state]
        print("information added")

    def edit(self):
        full_name=input("enter yor full name:")
        if full_name in address_book.contacts:
         phone=input("enter your number:")
         address=input("enter your address:")
         pincode=int(input("Enter pincode:"))
         state=input("Enter state:")
         address_book.contacts[full_name]=[phone,address,pincode,state]
         print("contact edited")
        else:
         print("contact not found")

    def delete(self):
        full_name=input("enter yor full name:")
        if full_name in address_book.contacts:
           del address_book.contacts[full_name]
           print("contact deleted")
        else:
           print("contact not found")

obj= address_book()

while True:
 print("1.create 2.edit 3.delete 4.exit")
 choice=int(input("Enter your choice:"))
 if choice==1:
  obj.create_address_book()
 elif choice==2:
   obj.edit()
 elif choice==3:
   obj.delete
 elif choice==4:
    break
 else:
  print("invalid choice")
         

