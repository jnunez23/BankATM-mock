import random

account_info = {}


def init():
    print("Welcome to Julio's Bank")
    status = int(input("Do you have an account with us? (1) for Yes, (2) for No "))

    if status is 1:
        login()
    elif status is 2:
        register()
    else:
        print("Sorry, I can't understand what you are inputting. Please try again")
        init()


def register():
    print("Welcome to the registering process!!!!")
    f_name = input("What is your first name? ")
    l_name = input("What is your last name? ")
    email = input("What is your email address? ")
    passwd = input("What is your password? ")

    account_num = generating_account()
    account_info[account_num] = [f_name, l_name, email, passwd, current_balance()]

    print("You have finished creating your account\nYour account number is %d" % account_num)

    login()


def login():

    print("Please login!")

    login_success = False

    while not login_success:
        user_acc = int(input("What is your account number? "))
        user_pass = input("What is your password? ")

        for acc_num, acc_details in account_info.items():
            if user_acc == acc_num:
                if user_pass == acc_details[3]:
                    bank_ops(acc_details)
                    login_success = True
                else:
                    print("Try again, something went wrong")
            else:
                print("Something went wrong, try again")
                login()


def bank_ops(acc_details):
    print("Welcome %s %s to Bank of Julio" % (acc_details[0], acc_details[1]))

    option_select = int(input("Select one of the following: (1) Withdraw, (2) Deposit, (3) Logout, (4) Exit "))

    if option_select:

        if option_select == 1:
            withdraw()
        elif option_select == 2:
            deposit()
        elif option_select == 3:
            logout()
        elif option_select == 4:
            exit()
        else:
            print("Incorrect selection. Try again.")
            bank_ops(acc_details)


def current_balance():
    return 50000


def withdraw():
    print("Your current balance is %d" % current_balance())
    withdraw_ammount = int(input("How much would you like to withdraw? "))

    if current_balance() > withdraw_ammount:
        new_balance = current_balance() - withdraw_ammount
        print("Your new balance is {}".format(new_balance))
    else:
        print("Unsuccessful attempt, please try again.")
        withdraw()


def deposit():
    print("Your current balance is %d" % current_balance())
    deposit_ammount = int(input("How much would you like to deposit? "))
    new_balance = deposit_ammount + current_balance()
    print("Your new balance is {}".format(new_balance))


def logout():
    login()


def generating_account():
    return random.randrange(000000, 999999)


init()
