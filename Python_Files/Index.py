import sys
import functions


while( True ):

    s=functions.display_Type_of_Users()

    print("**The value chosen is: ",s)
    if(s == "1"):
        while (True):
            admin_op=functions.admin_User()
            if (admin_op=="1"):
                print("You Selected User Access management")
                functions.user_access_mgmt()
            elif(admin_op=="2"):
                print("Execute a SQL Command")
            elif (admin_op == "3"):
                print("Eexute a SQL Script")
            elif (admin_op == "4"):
                print("Quitting Program....")
                sys.exit(0)
            else:
                print("Please enter a valid key...")
            print("\n")
    elif(s == "2"):
        print("You Selected Data Entry User Role")
    elif(s == "3"):
        print("You Selected End User or Browse-Only User Role")
    elif(s == "4"):
        print("Quitting Program....")
        functions.determineState()
        sys.exit(0)
    else:
        print("Please enter a valid key...")
    print("\n")


