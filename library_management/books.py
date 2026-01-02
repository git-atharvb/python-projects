import library_management.utils as utils

def menu():
    while True:
        print("\n----- Books -----")
        print("1. Add Book")
        print("2. Search Book")
        print("3. List All Books")
        print("4. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            list_books()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    # Implement the logic to add a book
    pass

def search_book():
    # Implement the logic to search for a book
    pass

def list_books():
    # Implement the logic to list all books
    pass
