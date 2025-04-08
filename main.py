from auth import register, login
from admin import admin_menu
from user import user_menu

def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            role = login()
            if role == "admin":
                admin_menu()
            elif role == "user":
                user_menu()
        elif choice == "3":
            print("Good bye :)")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    auth_menu()
