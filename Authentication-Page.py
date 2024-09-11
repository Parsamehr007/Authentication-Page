import os
import time 
import re
import json
import bcrypt

data_file = "data.json"
if not os.path.exists(data_file):
    with open(data_file , 'w') as f:
        json.dump({} , f)

def load_file():
    with open(data_file , 'r') as f:
        return json.load(f)

def update_file(new_data):
    with open(data_file , 'w') as f:
        json.dump(new_data , f)


def hash_password(password):

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password

def check_password(password , hashed):
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

def login():
    data = load_file()
    username = input("username : ")
    password = input("password : ")
    if username in data and check_password(password, data[username].encode("utf-8")) :
        print("loging in")
    else:
        print("username or password are incorrect")

def user_menu(username):
    data = load_file()
    while True:
        print("\nUser Menu:")
        print("1: Show Profile")
        print("2: Edit Profile")
        print("3: Log Out")
        choice = input("Choose an option: ")

        if choice == "1":
            # Show Profile
            print(f"Username: {username}")
            print(f"Password (hashed): {data[username]}")  # نمایش هش پسورد
        elif choice == "2":
            # Edit Profile
            new_password = input("Enter new password: ")
            password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
            if re.match(password_regex, new_password):
                data[username] = hash_password(new_password).decode("utf-8")
                update_file(data)
                print("Profile updated successfully.")
            else:
                print("Invalid password format. Must include uppercase, lowercase, number, and special character.")
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def signup():
    data = load_file()
    username_regex = r"^(?=[a-zA-Z0-9._]{4,20}$)"
    # Minimum eight characters
    # at least one uppercase letter, one lowercase letter, one number and one special character
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    username = input("username : ")

    if not re.match(username_regex,username):
        print("invalid username format")
        return
    
    password = input("password : ")

    if not re.match(password_regex,password):
        print("invalid password format")
        return
    
    repeat = input("repeat password : ")
    if password == repeat :
        if username in data :
            print(" username is Duplicate")
            return
        hsd_password = hash_password(password)
        data[username] = hsd_password.decode("utf-8")
        print("sign up successfully")
        update_file(data)
    else :
        print("entered passwords are not the same ")

def main():
    while True :
        # os.system("cls")          #for windows terminal
        choose = input(" 1 : login \n 2 : sign up \n 3 : exit \n choose :")
        if choose ==  "1" :
            login()
        elif choose ==  "2" :
            signup()
        elif choose == "3" :
            break
        else :
            print("wrong input")
        time.sleep(3)
main()

