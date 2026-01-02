import library_management.utils as utils

def menu():
    while True:
        print("\n----- Members -----")
        print("1. Add Member")
        print("2. Search Member")
        print("3. List All Members")
        print("4. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            search_member()
        elif choice == "3":
            list_members()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def add_member():
    # Implement the logic to add a member
    pass

def search_member():
    # Implement the logic to search for a member
    pass

def list_members():
    # Implement the logic to list all members
    pass
