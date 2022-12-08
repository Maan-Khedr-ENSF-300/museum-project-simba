import sys
import functions

if __name__ == '__main__':


    print("\n********** Welcome to  Museum Management System ************\n")
    valid_user=functions.connect_database()
    #print(valid_user)

while (True):
    #Display Menu options
    if valid_user==3:
        s="3"
    else:
        s=functions.display_Type_of_Users()

    if(s == "1"):
        print("***Admin User Menu***\n")
        while (True):
            admin_op=functions.admin_User()
            if (admin_op=="1"):
                print("Execute a SQL Commands & Queries")
                functions.admin_execute_query()
            elif(admin_op=="2"):
                print("Execute a SQL Script File")
                functions.admin_execute_SqlFile()
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
        print("***Data Entry User Menu***\n")
        functions.dataEntery_Option()
    elif(s == "3"):
        print("***Browse/Guest User Menu***\n")
        functions.Enduser_BrowseOnly()
    elif(s == "4"):
        print("Quitting Program....")
        functions.determineState()
        sys.exit(0)
    else:
        print("Please enter a valid key...")
    print("\n")



