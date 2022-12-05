import random
import sys


def determineState():
    save = input("\nWould you like to commit changes before closing? [Y/N]\n")

    if (save.lower() == "y"):
        print("\nCommit database changes and exiting....\n")
    else:
        print("\nQutting program without saving....\n")

    return 1


def display_Type_of_Users():
    print("\n********** Welcome to  Museum Management System ************")
    s = input("""Select User Type By Entering Your Choice (1/2/3 __
          1 - Admin User
          2 - Data Entry User
          3 - End User Or Guest User
          4 - Quit\n""")

    return s


def admin_User():
    print("\n********** Admin User Menu ************")
    s = input("""Select Admin User Operation By Entering Your Choice (1/2/3 __
          1 - User Access Management
          2 - Execute a SQL Query
          3 - Execute a SQL script
          4 - Quit Application\n""")
    return s


def user_access_mgmt():
    print("\n********** User Access Management Menu ************")
    while (True):
        s = input("""Select Operation By Entering Your Choice (1/2/3 __
              1 - Add User
              2 - Remove User
              3 - Quit Application\n""")
        if (s == "1"):
            print("You Selected Add User Operation")
        elif (s == "2"):
            print("You Selected Remove User Operation")
        elif (s == "3"):
            print("Quitting Application")
            sys.exit(0)
        else:
            print("Please enter a valid key...")
        print("\n")