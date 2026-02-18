import json 
import os

class address_book:
    def __init__(self):
        self.file = "address_book.json"
        self.address_book = {} 
        self.read_from_json()

    def read_from_json(self): 
        if os.path.exists(self.file): 
            with open(self.file, "r") as f: 
                self.address_book = json.load(f)
        else: 
            self.address_book = {}

    def write_to_json(self): 
        with open(self.file, "w") as f: 
            json.dump(self.address_book, f, indent=4)

    def create_address_book(self):
        while True:
            try:
                num_of_address_book = int(input("Enter the number of address books: "))
                break
            except ValueError:
                print("Invalid input. Please enter only digits.")
        
        count = 0
        while count < num_of_address_book:
            address_book_name = input("Enter your address book name: ")
            if address_book_name in self.address_book:
                print("Already name exists, give another name.")
                continue
            else:
                self.address_book[address_book_name] = {}

            while True:
                full_name = input("Enter your full name: ")
                if all(x.isalpha() for x in full_name) :
                    self.address_book[address_book_name]['full_name'] = full_name
                    break
                else:
                    print("Invalid input. Please enter only characters.")

            while True:
                try:
                    phone = (input("Enter your number: "))
                    if phone.isdigit() and len(phone)==10:
                      self.address_book[address_book_name]['phone'] = phone
                      break
                    else:
                        print ("invalid input .Please entr 10 digit mobile number.")
                except ValueError:
                    print("Invalid input. Please enter only digits.")

            while True:
                address = input("Enter your address: ")
                if all(x.isalpha() or x.isdigit() for x in address) :
                    self.address_book[address_book_name]['address'] = address
                    break
                else:
                    print("Invalid input. Please enter valid address characters or digits.")

            while True:
                try:
                    pincode = (input("Enter pincode: "))
                    if pincode.isdigit() and len(pincode)==6:
                     self.address_book[address_book_name]['pincode'] = pincode
                     break
                    else:
                        print("invalid input.please enter 6 digit pincode.")
                except ValueError:
                    print("Invalid input. Please enter only digits.")

            while True:
                state = input("Enter state: ")
                if all(x.isalpha()  for x in state) :
                    self.address_book[address_book_name]['state'] = state
                    break
                else:
                    print("Invalid input. Please enter only characters.")

            count += 1 
            self.write_to_json() 
            print("Address book created")

    def edit_address_book(self):
      address_book_name = input("Enter address book name to edit: ")
      if address_book_name not in self.address_book:
        print("Invalid information")
        return

      print("1. full name")
      print("2. phone")
      print("3. address")
      print("4. pincode")
      print("5. state")

      while True:
        try:
            choice = int(input("Enter your choice to edit: "))

            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Enter 1 to 5.")
                continue

            if choice == 1:
                full_name = input("Enter your full name: ")
                if all(x.isalpha() for x in full_name):
                    self.address_book[address_book_name]['full_name'] = full_name
                else:
                    print("Invalid input. Only characters allowed.")
                    continue

            elif choice == 2:
                phone = input("Enter your number: ")
                if phone.isdigit() and len(phone) == 10:
                    self.address_book[address_book_name]['phone'] = phone
                else:
                    print("Invalid input. Enter 10 digit mobile number.")
                    continue

            elif choice == 3:
                address = input("Enter your address: ")
                if all(x.isalpha() for x in full_name):
                    self.address_book[address_book_name]['address'] = address
                else:
                    print("Invalid address.")
                    continue

            elif choice == 4:
                pincode = input("Enter pincode: ")
                if pincode.isdigit() and len(pincode) == 6:
                    self.address_book[address_book_name]['pincode'] = pincode
                else:
                    print("Invalid input. Enter 6 digit pincode.")
                    continue

            elif choice == 5:
                state = input("Enter state: ")
                if all(x.isalpha() for x in state):
                    self.address_book[address_book_name]['state'] = state
                else:
                    print("Invalid input. Only characters allowed.")
                    continue
                break   
            
        except ValueError:
            print("Invalid input. please enter a number between 1 and 5.")

        self.write_to_json()
        print("Address book edited successfully.")

    def delete_address_book(self):
        address_book_name = input("Enter address book name to delete: ")
        if address_book_name in self.address_book:
            del self.address_book[address_book_name]
            self.write_to_json() 
            print("Address book deleted")
        else: 
            print("Address book not found")

    def display(self):
        if not self.address_book:
            print("No records found")
        else:
            print(json.dumps(self.address_book, indent=4))

if __name__ == "__main__":
    obj = address_book()
    while True:
        print("1.create address book")
        print("2. Edit address book")
        print("3.delete address book")
        print("4.read json file")
        print("5.display address book")
        print("6.exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                obj.create_address_book()
            elif choice == 2:
                obj.edit_address_book()
            elif choice == 3:
                obj.delete_address_book()
            elif choice == 4:
                obj.read_from_json()
                print("JSON file read successfully")
            elif choice == 5:
                obj.display()
            elif choice == 6:
                print("Exiting program")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter a digit from 1 to 6.")
