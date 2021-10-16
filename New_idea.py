#from Database import user_database (I just copy and pasted Database file below.

user_database = {"Richard01": "01",
                 "Murray02": "02",
                 "Marc03": "03",
                 "Joe04": "04"}


def login_register():
    selection = ""
    account_blocked = False
    user_name = ""
    password = ""
    while selection != ("A" or "B") and not account_blocked:
        selection = input("Hi There. Please sign into your account, or sign up with us.\nSelect A or B\n\nA - Sign in\nB - Register\n\n").upper()
        if selection == "A":
            user_name, password = sign_in()
            print("login register", user_name, password, "login register")
            if user_name == None:
                account_blocked = True
                break
            access_account(user_name, password)
        elif selection == "B":
            user_name, password = register()
            user_database[user_name] = password
            access_account(user_name, password)
        else:
            print("Please enter only A or B")


def sign_in():
    attempts = 3
    while attempts > 0:
        user_name = input("Please enter your username: ")
        password = input("Please enter your password: ")
        attempts -= 1
        if user_name in user_database:
            if user_database[user_name] == password:
                return user_name, password
            else:
                print("You've entered your username and/or password incorrect. You have", attempts, "attempts left.")
        else:
            print("You've entered your username and/or password incorrect. You have", attempts, "attempts left.")
    print("\nYour account has been blocked. Please contact our helpline on 0800 123 456. Open 24/7")
    user_name = None
    password = None
    return user_name, password


def access_account(user_name, password):
    #write code that displays info about about user's account, and options to change: password, names, date of birth etc.
    print("access account", user_name, password, "access account")


def register():
    user_name = input("please register a username of your choice: ")
    password = input("Please create a password: ")
    print("register", user_name, password, "register")
    return user_name, password


login_register()
