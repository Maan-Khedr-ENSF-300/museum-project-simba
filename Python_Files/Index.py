import sys
import functions

if __name__ == '__main__':


    print("\n********** Welcome to  Museum Management System ************\n")
    valid_user=functions.connect_database()

while (True):
    #Display Menu options
    s=functions.display_Type_of_Users()

    print("**The value chosen is: ",s)
    if(s == "1"):
        while (True):
            admin_op=functions.admin_User()
            if (admin_op=="1"):
                print("Execute a SQL Script")
                functions.admin_execute_query()
            elif(admin_op=="2"):
                print("Execute a SQL Command")
            elif (admin_op == "3"):
                print("User Access Management")
                functions.user_access_mgmt()
            elif (admin_op == "4"):
                print("Quitting Program....")
                sys.exit(0)
            else:
                print("Please enter a valid key...")
            print("\n")
    elif(s == "2"):
        print("You Selected Data Entry User Role")
        functions.dataEntery_Option()
    elif(s == "3"):
        print("You Selected End User or Browse-Only User Role\n")
        functions.Enduser_BrowseOnly()
    elif(s == "4"):
        print("Quitting Program....")
        functions.determineState()
        sys.exit(0)
    else:
        print("Please enter a valid key...")
    print("\n")


