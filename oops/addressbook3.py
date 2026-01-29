import json
import os

class address_book:
    def __init__(self):
        self.file="address_book.json"
        self.address_book={}
        self.read_from_json()

    def read_from_json(self):
        if os.path.exists(self.file):
          with open(self.file,"r") as f:
           self.address_book=json.load(f)
        else:
          self.address_book={}

    def write_to_json(self):
      with open(self.file,"w") as f:
       json.dump(self.address_book,f,indent=4)

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
              self.write_to_json()
              print("address book created")
              

    def edit_address_book(self):
        address_book_name=input("Enter address book name to edit:")
        if address_book_name not in self.address_book:
            print("invalid infomartion")
            return
        print("1.full name")
        print("2.phone")
        print("3.address")
        print("4.pincode")
        print("5.state")
        choice=int(input("enter your choice to edit"))
        if choice==1:
         self.address_book[address_book_name]['full_name']=input("Enter your full name:")
        if choice==2:
         self.address_book[address_book_name]['phone']=int(input("enter your number:"))
        if choice==3:
         self.address_book[address_book_name]['address']=input("enter your address:")
        if choice==4:
         self.address_book[address_book_name]['pincode']=int(input("Enter pincode:"))
        if choice==5:
         self.address_book[address_book_name]['state']=input("Enter state:")
        else:
         print("invalid choice")
         return
        self.write_to_json()
        print("address book edited")

    def delete_address_book(self):
        address_book_name=input("enter address book name to delete:")
        if address_book_name in self.address_book:
         del self.address_book[address_book_name]
         self.write_to_json()
         print("address book deleted")
        else:
         print("address book not found")

    def display(self):
       if not self.address_book:
         print("no records found")
       else:
         print(json.dumps(self.address_book,indent=4))
    
if __name__=="__main__":

     obj=address_book()
     while True:
       print("1.create  2. edit  3.delete  4.read json file  5.display  6.exit")
       choice=int(input("Enter your choice:"))
       if choice==1:
         obj.create_address_book()
       elif choice==2:
         obj.edit_address_book()
       elif choice==3:
        obj.delete_address_book()
       elif choice==4:
         obj.read_from_json()
         print ("json file read successfully")
       elif choice==5:
        obj.display()
       elif choice==6:
        print("exiting program")
        break
       else:
        print("invalid choice")
         

            
            
        