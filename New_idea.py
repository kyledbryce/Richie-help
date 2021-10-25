user_database = dict(
    Richard01=["01", "Richard", "Dalziel", "Blue", False, 3],
    Murray02=["02", "Murrya", "McNicol", "Brown", True, 0],
    Marc03=["03", "Marc", "Sherwood", "Brown", False, 3],
    Joe04=["04", "Joe", "Anderson", "Green", False, 3]
)


def login_register():
    selection = str
    finished = False
    while (selection != "A" and selection != "B" and selection != "C") or not finished:
        selection = input("Hi There. Please sign into your account, or sign up with us.\nSelect A, B or C\n\nA - Sign in\nB - Register\nC - Exit\n\n").upper()
        if selection == "A":
            user_name = sign_in()
            if user_name == None:
                pass
            elif not user_database[user_name][4]:
                access_account(user_name)
            else:
                pass
        elif selection == "B":
            user_name = register()
            if user_name == None:
                pass
            else:
                access_account(user_name)
        elif selection == "C":
            finished = True
        else:
            print("Please enter only A, B or C")


def sign_in():
    go_back = False
    while not go_back:
        user_name = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if user_name in user_database:
            if user_database[user_name][0] == password and not user_database[user_name][4]:
                return user_name
            else:
                user_database[user_name][5] -= 1
                if user_database[user_name][5] <= 0:
                    user_database[user_name][4] = True
                    print("Your account has been blocked. Please contact our helpline on 0800 123 456. Open 24/7")
                    return user_name
                else:
                    print("You've entered an incorrect password. You have", user_database[user_name][5], "attempts left.")
        else:
            print("This username has not been recognised. Please try again or register with us.")
            Exit = input("Would you like to go back?").upper()
            if Exit == "Y":
                user_name = None
                return user_name
            else:
                pass


def access_account(user_name):
    edit = str
    logged_out = False
    while (edit != "A" and edit != "B") or not logged_out:
        edit = input("Would you like to edit your account?\nA - Yes\nB - Log Out\n").upper()
        if edit == "A":
            attribute = str
            while attribute != "A" and attribute != "B" and attribute != "C" and attribute != "D" and attribute != "E":
                attribute = input("What would you like to change?\nA - Username\nB - Password\nC - First Name\nD - Last Name\nE - Eye Colour\n").upper()
                if attribute == "A":
                    new_username = input("Please choose a new username: ")
                    user_database[new_username] = user_database[user_name]
                    del user_database[user_name]
                    user_name = new_username
                elif attribute == "B":
                    user_database[user_name][0] = input("Please choose a new password: ")
                elif attribute == "C":
                    user_database[user_name][1] = input("Please choose a new first name: ")
                elif attribute == "D":
                    user_database[user_name][2] = input("Please choose a new last name: ")
                elif attribute == "E":
                    user_database[user_name][3] = input("Please choose a new eye colour: ")
                else:
                    print("Please choose only from A - E")
                print(user_database[user_name])
        elif edit == "B":
            print("You are not making any changes at the moment.")
            logged_out = True
        else:
            print("Please choose only A or B")


def register():
    user_name = str
    exit_registration = False
    while user_name not in user_database and not exit_registration:
        user_name = input("please register a username of your choice: ")
        if user_name in user_database:
            print("This username has already been taken. Try again.")
            user_name = str
            Exit = input("Would you like to exit registration?\nY - Yes\nN - No\n\n").upper()
            if Exit == "Y":
                exit_registration = True
                user_name = None
            else:
                pass
        else:
            password = input("Please create a password: ")
            first_name = input("please enter your first name: ")
            last_name = input("please enter your last name: ")
            eye_colour = input("please enter your eye colour: ")
            user_database[user_name] = [password, first_name, last_name, eye_colour, False, 3]
            return user_name


login_register()
