class address_book:
    def __init__(self):
        self.address_book={}
    
    def create_address_book(self):
        num_of_address_book=int(input("Enter the number of address books:"))
        count=0
        while count<num_of_address_book:
         address_book_name=input("Enter your address book name:")
         if address_book_name in self.address_book:
              print("Already name exist give another name.")   
         else:                                                                   
              self.address_book[address_book_name]={}
              full_name=input("Enter your full name:")
              self.address_book[address_book_name]['full_name']=full_name

              phone=int(input("enter your number:"))
              self.address_book[address_book_name]['phone']=phone
              
              address=input("enter your address:")
              self.address_book[address_book_name]['address']=address
              
              pincode=int(input("Enter pincode:"))
              self.address_book[address_book_name]['pincode']=pincode
              
              state=input("Enter state:")
              self.address_book[address_book_name]['state']=state
              count+=1
              print("address book created")
              

    def edit_address_book(self):
        address_book_name=input("Enter address book name to edit:")
        if address_book_name in self.address_book:
            print("edit address book:")
            self.address_book[address_book_name]['full_name']=input("Enter your full name:")
            self.address_book[address_book_name]['phone']=int(input("enter your number:"))
            self.address_book[address_book_name]['address']=input("enter your address:")
            self.address_book[address_book_name]['pincode']=int(input("Enter pincode:"))
            self.address_book[address_book_name]['state']=input("Enter state:")
            print("address book edited")
        else:
            print("address book name not found")

    def delete_address_book(self):
        address_book_name=input("enter address book name to delete:")
        if address_book_name in self.address_book:
         del self.address_book[address_book_name]
         print("address book deleted")
        else:
         print("address book not found")

    def display(self):
       print("address book")
       print(self.address_book)


if __name__=="__main__":

     obj=address_book()
     while True:
       print("1.create  2. edit  3.delete  4.display  5.exit")
       choice=int(input("Enter your choice:"))
       if choice==1:
         obj.create_address_book()
       elif choice==2:
         obj.edit_address_book()
       elif choice==3:
        obj.delete_address_book()
       elif choice==4:
        obj.display()
       elif choice==5:
        print("exiting program")
        break
       else:
        print("invalid choice")
         

            
            
        