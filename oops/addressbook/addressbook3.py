import json
import os

class address_book:
    def __init__(self):
        self.file = "address_book.json"
        self.address_book = {}
        self.read_from_json()

   
    def get_name_input(self, msg):
        while True:
            value = input(msg)
            if value.replace(" ", "").isalpha():
                return value
            else:
                print(" Only characters are allowed.")

    def get_digit_input(self, msg):
        while True:
            value = input(msg)
            if value.isdigit():
                return int(value)
            else:
                print(" Only digits are allowed.")


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
        n = self.get_digit_input("Enter number of address books: ")
        count = 0

        while count < n:
            name = self.get_name_input("Enter address book name: ")

            if name in self.address_book:
                print("Already exists, try another name.")
                continue

            self.address_book[name] = {}
            self.address_book[name]["full_name"] = self.get_name_input("Enter full name: ")
            self.address_book[name]["phone"] = self.get_digit_input("Enter phone number: ")
            self.address_book[name]["address"] = input("Enter address: ")
            self.address_book[name]["pincode"] = self.get_digit_input("Enter pincode: ")
            self.address_book[name]["state"] = self.get_name_input("Enter state: ")

            count += 1
            self.write_to_json()
            print("Address book created")

    
    def edit_address_book(self):
        name = self.get_name_input("Enter address book name to edit: ")

        if name not in self.address_book:
            print("Invalid information")
            return

        print("1. Enter your full name\n2. Enter your phone number \n3. Enter your address\n4. Enter your pincode\n5.Enter your state")
        choice = self.get_digit_input("Enter your choice: ")

        if choice == 1:
            self.address_book[name]["full_name"] = self.get_name_input("Enter full name: ")
        elif choice == 2:
            self.address_book[name]["phone"] = self.get_digit_input("Enter phone number: ")
        elif choice == 3:
            self.address_book[name]["address"] = input("Enter address: ")
        elif choice == 4:
            self.address_book[name]["pincode"] = self.get_digit_input("Enter pincode: ")
        elif choice == 5:
            self.address_book[name]["state"] = self.get_name_input("Enter state: ")
        else:
            print("Invalid choice")
            return

        self.write_to_json()
        print("Address book updated")

    
    def delete_address_book(self):
        name = self.get_name_input("Enter address book name to delete: ")

        if name in self.address_book:
            del self.address_book[name]
            self.write_to_json()
            print("✅ Address book deleted")
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
        print("\n1.Create address book \n2.Edit address book \n3.Delete address book  \n4.Read JSON \n5.Display address book \n6.Exit address book")
        choice = input("Enter your choice: ")

        if choice == "1":
            obj.create_address_book()
        elif choice == "2":
            obj.edit_address_book()
        elif choice == "3":
            obj.delete_address_book()
        elif choice == "4":
            obj.read_from_json()
            print("JSON file read successfully")
        elif choice == "5":
            obj.display()
        elif choice == "6":
            print("Exiting program")
            break
        else:
            print("Invalid choice")