
user_database = {"Richard01": ["01", "Richard", "Dalziel", "Blue"],
                 "Murray02": ["02", "Murrya", "McNicol", "Brown"],
                 "Marc03": ["03", "Marc", "Sherwood", "Brown"],
                 "Joe04": ["04", "Joe", "Anderson", "Green"]}


def login_register():
    selection = ""
    account_blocked = False
    user_name = ""
    password = ""
    first_name = ""
    last_name = ""
    eye_colour = ""
    while selection != ("A" or "B") and not account_blocked:
        selection = input("Hi There. Please sign into your account, or sign up with us.\nSelect A or B\n\nA - Sign in\nB - Register\n\n").upper()
        if selection == "A":
            user_name, password, first_name, last_name, eye_colour = sign_in()
            if user_name == None:
                account_blocked = True
                break
            access_account(user_name, password)
        elif selection == "B":
            user_name, password, first_name, last_name, eye_colour = register()
            user_database[user_name] = [password, first_name, last_name, eye_colour]
            print(user_database.items())
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
    print("access account", user_name, password, "access account")


def register():
    user_name = input("please register a username of your choice: ")
    password = input("Please create a password: ")
    first_name = input("please enter your first name: ")
    last_name = input("please enter your last name: ")
    eye_colour = input("please enter your eye colour: ")
    return user_name, password, first_name, last_name, eye_colour


login_register()
