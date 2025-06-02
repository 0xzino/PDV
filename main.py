import flask
import cryptography

def intro():
    print("PDV V.0.1 - Prototype\n----------------------------------")
    print("1. Password Manager\n2. Files")
    select = input()
    print(select)

    if select == "1":
        password_manager()

    if select == "2":
        files()
        
def password_manager():
    print("\n\n\n\n\n\n\n\n\n\nPassword Manager\n----------------------------------")
    print("1. Add Password\n2. View Passwords\n3. Delete Password")
    select = input()
    if select == "1":
        add_password()
    elif select == "2":
        view_passwords()
    elif select == "3":
        delete_password()
    else:
        print("Invalid selection. Please try again.")
        password_manager()

def files():
    print("\n\n\n\n\n\n\n\n\nFiles\n----------------------------------")
    print("Usually files will just pop up here")

intro()