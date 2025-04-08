from file_manager import write, read
from utils import generate_id, hash_password

def register():
    username = input("Enter your username: ")
    phone = input("Enter your phone number: ")
    password1 = input("Enter your password: ")
    password2 = input("Enter your password again: ")

    while password1 != password2:
        print("Passwords do not match")
        password1 = input("Enter your password: ")
        password2 = input("Enter your password again: ")

    new_id = generate_id(filename="users.csv")
    hashed_pw = hash_password(password1)
    user = [str(new_id), username, phone, hashed_pw, 0]
    write(filename="users.csv", data=user, mode="a")
    print("You have successfully registered!")

def login():
    admin_phone = "948529805"
    admin_password = "x_2105"

    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")

    if phone_number == admin_phone and password == admin_password:
        print("Welcome boss!")
        return "admin"

    hashed_password = hash_password(password)
    users = read(filename="users.csv")

    for index, user in enumerate(users):
        if len(user) >= 4 and user[2] == phone_number and user[3] == hashed_password:
            users[index][-1] = 1
            write(filename="users.csv", data=users)
            print("Welcome, user!")
            return "user"

    print("Wrong phone number or password")
    return False

