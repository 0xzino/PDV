import flask
import cryptography
import password_manager
import files
import reverse_proxy

def intro():
    print("PDV V.0.1 - Prototype\n----------------------------------")
    print("1. Password Manager (Not yet implemented)\n2. Files\n3. Reverse Proxy")
    select = input()

    if select == "1":
        print("Not yet implemented")
        intro()
    elif select == "2":
        files()
    elif select == "3":
        reverse_proxy()
    else:
        print("Invalid selection. Please try again.")
        intro()
        
intro()