def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)

    while True:
        
        choice = input("Enter your choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            print("Good bye :)")
        else:
            print("Invalid choice")



def admin_menu():
    print("""
    1. New orders (10)
    2. Accepted orders (100)
    3. Canceled orders (34)
    4. Add new product
    5. Delete product
    6. Logout
    """)


    choice = input("Enter your choice: ")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        print("Good bye :)")
    else:
        print("Invalid choice")


def user_menu():
    print("""
    1. Show all products
    2. Order
    3. My orders
    4. Logout
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        print("Good bye")
    else:
        print("Invalid choice")


