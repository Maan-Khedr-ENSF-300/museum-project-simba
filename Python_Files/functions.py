import sys
import mysql.connector
from IPython.display import display
import pandas as pd
from mysql.connector import errorcode



def determineState():

    save=input("\nWould you like to commit changes before closing? [Y/N]\n")

    if( save.lower() == "y" ):
        print("\nCommit database changes and exiting....\n")
    else:
        print("\nQutting program without saving....\n")
        
    return 1

def display_Type_of_Users():

    s = input("""Select User Operation Type By Entering Your Choice (1/2/3 __
          1 - Admin User
          2 - Data Entry User
          3 - End User Or Guest User
          4 - Quit\n""")

    return s

def admin_User():
    print("\n********** Admin User Menu ************")
    s = input("""Select Admin User Operation By Entering Your Choice (1/2/3 __
          1 - Execute a SQL Query
          2 - Execute a SQL script
          3 - User Access Management
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

def dataEntery_Option():
    print("\n********** Data Entry Menu ************")
    while (True):
        s = input("""Select Operation By Entering Your Choice (1/2/3 __
              1 - Lookup/Search a DB Table
              2 - Insert new Tuple Into a Table
              3 - Delete a Tuple
              4 - Update a Tuple
              5 - Quit Application\n""")
        if (s == "1"):
            print("You Selected Lookup Operation\n")
            DataEntryUser_Lookup()
        elif (s == "2"):
            print("You Selected Insert Operation")
        elif (s == "3"):
            print("You Selected Delete Operation")
        elif (s == "4"):
            print("You Selected Update Operation")
        elif (s == "5"):
            print("Quitting Application")
            sys.exit(0)
        else:
            print("Please enter a valid key...")
        print("\n")

def connect_database():

        try:
            user=input("Enter Your User Name:")
            password=input("Enter Your Password:")
            cnx = mysql.connector.connect(host ='127.0.0.1',user=user,
                                          password=password,database='museum')
            cnx.close()
            return 1
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                sys.exit(0)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                sys.exit(0)
            else:
                print(err)
                sys.exit(0)

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        if result==None:
            result=[]
        return result
    except mysql.connector.Error as err:
        print(err)

def admin_execute_query():
    try:
        user_query = input("Type your Sql Command/Query:")
        cnx = mysql.connector.connect(host='127.0.0.1', user='root',
                                      password='admin', database='museum')
        cursor=cnx.cursor()
        cursor.execute(user_query)
        print("SQL Command/Query Executed Successfully")
        cnx.commit()
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            sys.exit(0)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            sys.exit(0)
        else:
            print(err)
            sys.exit(0)

def Enduser_BrowseOnly():
    try:
        user_query = input("""Select the Information you want to Browse By Entering your choice (1/2/3..):
                        1- Artist
                        2- Painting
                        3- ArtObject
                        4- Collection
                        5- Sculpture
                        6- Statue
                        7- Exhibition  \n""")

        cnx = mysql.connector.connect(host='127.0.0.1', user='root',
                                      password='admin', database='museum')
        if (user_query=="1"):
            select_query="Select Name, Country, MainStyle,DateBorn,DateDied From Artist"
            query_result= read_query(cnx,select_query)
            query_data=[]
            for result in query_result:
                result = list(result)
                query_data.append(result)

            table_columns = ["Name", "Country", "MainStyle", "DateBorn", "DateDied"]
            df = pd.DataFrame(query_data, columns=table_columns)
            display(df)
        elif (user_query=="2"):
            select_query="Select IDNum,PaintType,DrawnON,Style From Painting"
            query_result= read_query(cnx,select_query)
            query_data=[]
            for result in query_result:
                result = list(result)
                query_data.append(result)

            table_columns = ["ID", "PaintType", "DrawnON", "Style"]
            df = pd.DataFrame(query_data, columns=table_columns)
            display(df)
        elif (user_query == "3"):
            select_query = "Select IDNum,Artist,Year,Title,Description,Category,Ownership From ArtObject"
            query_result = read_query(cnx, select_query)
            query_data = []
            for result in query_result:
                result = list(result)
                query_data.append(result)

            table_columns = ["ID", "Artist", "Year", "Title", "Description","Category", "Ownership"]
            df = pd.DataFrame(query_data, columns=table_columns)
            display(df)
            cnx.close()
        elif (user_query == "4"):
            select_query = "Select Name,Type,Description,Address,Phone,ContactPerson From Collection"
            query_result = read_query(cnx, select_query)
            query_data = []
            for result in query_result:
                result = list(result)
                query_data.append(result)

            table_columns = ["Name", "Type", "Description", "Address", "Phone", "ContactPerson"]
            df = pd.DataFrame(query_data, columns=table_columns)
            display(df)
        elif (user_query == "5"):
            select_query = "Select IDNum,Material,Height,Weight,Style From Sculpture"
            query_result = read_query(cnx, select_query)
            query_data = []
            for result in query_result:
                result = list(result)
                query_data.append(result)

            table_columns = ["ID", "Material", "Height", "Weight", "Style"]
            df = pd.DataFrame(query_data, columns=table_columns)
            display(df)
        elif (user_query == "6"):
            select_query = "Select IDNum,Material,Height,Weight,Style From Statue"
            query_result = read_query(cnx, select_query)
            query_data = []
            for result in query_result:
                result = list(result)
                query_data.append(result)

            table_columns = ["ID", "Material", "Height", "Weight", "Style"]
            df = pd.DataFrame(query_data, columns=table_columns)
            display(df)
        elif (user_query == "7"):
            select_query = "Select Name,StartDate,EndDate From Exhibition"
            query_result = read_query(cnx, select_query)
            query_data = []
            for result in query_result:
                result = list(result)
                query_data.append(result)
            table_columns = ["Name", "StartDate", "EndDate"]
            df = pd.DataFrame(query_data, columns=table_columns)
            display(df)
        else:
            print("Please enter a valid key...")
            print("\n")

        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.CR_NO_RESULT_SET:
            print("Something went wrong")
            sys.exit(0)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            sys.exit(0)
        else:
            print(err)
            sys.exit(0)

def DataEntryUser_Lookup():
    try:
        user_query = input("""Select the Database Table you Want to Search (1/2/3..):
                        1- Artist
                        2- Painting
                        3- ArtObject
                        4- Collection
                        5- Sculpture
                        6- Statue
                        7- Exhibition  \n""")
        #db connection
        cnx = mysql.connector.connect(host='127.0.0.1', user='root',
                                      password='admin', database='museum')
        if (user_query=="1"):
            search_condition = input("Type the DB Field name you want to search  (like Name,Country..):")
            search_value = input("Type the DB Field value you want to search :")

            select_query="Select Name, Country, MainStyle,DateBorn,DateDied From Artist Where "
            select_query=select_query + search_condition +"=" + str(search_value)

            #print(select_query)
            query_result= read_query(cnx,select_query)
            query_data=[]
            if query_result != None and len(query_result) != 0:
                for result in query_result:
                    result = list(result)
                    query_data.append(result)
                table_columns = ["Name", "Country", "MainStyle", "DateBorn", "DateDied"]
                df = pd.DataFrame(query_data, columns=table_columns)
                print("\n ****Result of Your Search****\n")
                display(df)
            else:
                print("\n ****No Result of Your Search****\n")
        elif (user_query=="2"):
            search_condition = input("Type the DB Field name you want to search  (like ID,Style..):")
            search_value = input("Type the DB Field value you want to search :")

            select_query="Select IDNum,PaintType,DrawnON,Style From Painting Where "
            select_query = select_query + search_condition + "=" + search_value
            query_result= read_query(cnx,select_query)
            #print(len(query_result))
            query_data=[]
            if query_result!=None and len(query_result)!=0:
                for result in query_result:
                    result = list(result)
                    query_data.append(result)
                table_columns = ["ID", "PaintType", "DrawnON", "Style"]
                df = pd.DataFrame(query_data, columns=table_columns)
                print("\n ****Result of Your Search****\n")
                display(df)
            else:
                print("\n ****No Result of Your Search****\n")
        elif (user_query == "3"):

            search_condition = input("Type the DB Field name you want to search  (like IDNum,Artist,Title..):")
            search_value = input("Type the DB Field value you want to search :")

            select_query = "Select IDNum,Artist,Year,Title,Description,Category,Ownership From ArtObject Where "
            select_query = select_query + search_condition + "=" + search_value

            query_result = read_query(cnx, select_query)
            query_data = []
            if query_result != None and len(query_result) != 0:
                for result in query_result:
                    result = list(result)
                    query_data.append(result)

                table_columns = ["ID", "Artist", "Year", "Title", "Description","Category", "Ownership"]
                df = pd.DataFrame(query_data, columns=table_columns)
                print("\n ****Result of Your Search****\n")
                display(df)
            else:
                print("\n ****No Result of Your Search****\n")
        elif (user_query == "4"):
            search_condition = input("Type the DB Field name you want to search  (like Name,Type..):")
            search_value = input("Type the DB Field value you want to search :")

            select_query = "Select Name,Type,Description,Address,Phone,ContactPerson From Collection Where "
            select_query = select_query + search_condition + "=" + search_value
            query_result = read_query(cnx, select_query)
            query_data = []
            if query_result != None and len(query_result) != 0:
                for result in query_result:
                    result = list(result)
                    query_data.append(result)

                table_columns = ["Name", "Type", "Description", "Address", "Phone", "ContactPerson"]
                df = pd.DataFrame(query_data, columns=table_columns)
                print("\n ****Result of Your Search****\n")
                display(df)
            else:
                print("\n ****No Result of Your Search****\n")
        elif (user_query == "5"):
            search_condition = input("Type the DB Field name you want to search  (like IDNum,Style..):")
            search_value = input("Type the DB Field value you want to search :")

            select_query = "Select IDNum,Material,Height,Weight,Style From Sculpture Where "
            select_query = select_query + search_condition + "=" + search_value
            query_result = read_query(cnx, select_query)
            query_data = []
            if query_result != None and len(query_result) != 0:
                for result in query_result:
                    result = list(result)
                    query_data.append(result)

                table_columns = ["ID", "Material", "Height", "Weight", "Style"]
                df = pd.DataFrame(query_data, columns=table_columns)
                print("\n ****Result of Your Search****\n")
                display(df)
            else:
                print("\n ****No Result of Your Search****\n")
        elif (user_query == "6"):
            search_condition = input("Type the DB Field name you want to search  (like IDNum,Style..):")
            search_value = input("Type the DB Field value you want to search :")

            select_query = "Select IDNum,Material,Height,Weight,Style From Statue Where "
            select_query = select_query + search_condition + "=" + search_value
            query_result = read_query(cnx, select_query)
            query_data = []
            if query_result != None and len(query_result) != 0:
                for result in query_result:
                    result = list(result)
                    query_data.append(result)

                table_columns = ["ID", "Material", "Height", "Weight", "Style"]
                df = pd.DataFrame(query_data, columns=table_columns)
                print("\n ****Result of Your Search****\n")
                display(df)
            else:
                print("\n ****No Result of Your Search****\n")
        elif (user_query == "7"):
            search_condition = input("Type the DB Field name you want to search  (like Name,StartDate..):")
            search_value = input("Type the DB Field value you want to search :")

            select_query = "Select Name,StartDate,EndDate From Exhibition Where "
            select_query = select_query + search_condition + "=" + search_value
            query_result = read_query(cnx, select_query)
            query_data = []
            if query_result != None and len(query_result) != 0:
                for result in query_result:
                    result = list(result)
                    query_data.append(result)
                table_columns = ["Name", "StartDate", "EndDate"]
                df = pd.DataFrame(query_data, columns=table_columns)
                print("\n ****Result of Your Search****\n")
                display(df)
            else:
                print("\n ****No Result of Your Search****\n")
        else:
            print("Please enter a valid key...")
            print("\n")

        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_FIELD_ERROR:
            print("Something went wrong")
            sys.exit(0)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            sys.exit(0)
        else:
            print(err)
            sys.exit(0)