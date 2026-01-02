import library_management.books as books
import library_management.members as members
import library_management.loans as loans

def main():
    while True:
        print("\n----- Library Management System -----")
        print("1. Books")
        print("2. Members")
        print("3. Loans")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            books.menu()
        elif choice == "2":
            members.menu()
        elif choice == "3":
            loans.menu()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
