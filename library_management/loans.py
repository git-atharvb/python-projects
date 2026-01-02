import library_management.utils as utils

def menu():
    while True:
        print("\n----- Loans -----")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. List All Loans")
        print("4. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            borrow_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            list_loans()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def borrow_book():
    # Implement the logic to borrow a book
    pass

def return_book():
    # Implement the logic to return a book
    pass

def list_loans():
    # Implement the logic to list all loans
    pass
