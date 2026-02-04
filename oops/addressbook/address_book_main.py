
from addressbook import address_book3
address_book={}
addressbook=address_book3(address_book3)
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