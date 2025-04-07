from file_manager import write, read
from utils import generate_id

def register():
    username = input("Enter your username: ")
    password1 = input("Enter your password: ")
    password2 = input("Enter your password: ")
    
    while password1 != password2:
        print("Password does not match")
        password1 = input("Enter your password: ")
        password2 = input("Enter your password: ")
        
    new_id = generate_id(filename="user.csv")
    user = [new_id, username, password1, 0]
    write(filename="user.csv", data=user, mode="a")
    print("You have successfully registered!!!")
    

def login():
    username = input("Enter you username: ")
    password = input("Enter your password: ")
    
    users = read("users.csv")
    for user in users:
        if user[1] == username and user[2] == password:
            print(f"Welcome {user[1]}")
            return True
    return False