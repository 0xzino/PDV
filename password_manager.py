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