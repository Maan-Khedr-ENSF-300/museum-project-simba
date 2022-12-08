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
          1 - Execute a SQL Command/Query
          2 - Execute a SQL Script File
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
            print("You Selected Add User Operation\n")
            admin_addUser()
        elif (s == "2"):
            print("You Selected Remove User Operation\n")
            admin_RemoveUser()
        elif (s == "3"):
            print("Quitting Application")
            sys.exit(0)
        else:
            print("Please enter a valid key...")
        print("\n")

def admin_addUser():
    try:
        user = input("Enter New User Name To Add:")
        password = input("Enter Your Password for the New User:")
        cnx = mysql.connector.connect(host='127.0.0.1', user='root',
                                      password='admin', database='museum')
        add_user_query="CREATE USER IF NOT EXISTS "+"'" + user + "'" + "@'localhost'" + " IDENTIFIED BY " + "'"+ password+"'"
        #print(add_user_query)
        cursor=cnx.cursor()
        cursor.execute(add_user_query)
        print("User "+user+ " added Successfully")
        cnx.commit()
        cursor.close()
        cnx.close()
        return 1
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("***Not a registered user,You logged in as a Guest***\n")
            return 3
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def admin_RemoveUser():
    try:
        user = input("Enter User Name To Delete:")
        cnx = mysql.connector.connect(host='127.0.0.1', user='root',
                                      password='admin', database='museum')
        delete_user_query="DROP USER "+ user + "@localhost"
        #print(delete_user_query)
        cursor=cnx.cursor()
        cursor.execute(delete_user_query)
        print("User "+user+ " Deleted Successfully")
        cnx.commit()
        cursor.close()
        cnx.close()
        return 1
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("***Not a registered user,You logged in as a Guest***\n")
            return 3
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


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
            print("You Selected Insert Operation\n")
            DataEntryUser_Insert()
        elif (s == "3"):
            print("You Selected Delete Operation\n")
            DataEntryUser_Delete()
        elif (s == "4"):
            print("You Selected Update Operation\n")
            DataEntryUser_Update()
        elif (s == "5"):
            print("Quitting Application")
            sys.exit(0)
        else:
            print("Please enter a valid key...")
        print("\n")

def connect_database():

        try:
            user=input("Enter Your User Name Or type 'Guest' if Don't have a login:")
            password=input("Enter Your Password or Type 'Guest' as password:")
            cnx = mysql.connector.connect(host ='127.0.0.1',user=user,
                                          password=password,database='museum')
            cnx.close()
            return 1
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\n***Not a registered user,You logged in as a Guest***\n")
                return 3
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                #print(err)
                print("\n***Not a registered user,You logged in as a Guest***\n")
                return 3

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
            print("Something went Wrong")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def admin_execute_SqlFile():
    try:
        cnx = mysql.connector.connect(host='127.0.0.1', user='root',
                                      password='admin', database='museum')
        with open('python.sql', 'r') as f:
            with cnx.cursor() as cursor:
                cursor.execute(f.read(), multi=True)
            cnx.commit()
        print("SQL Script Executed Successfully")
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something went wrong")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def Enduser_BrowseOnly():
    try:
        user_query = input("""Select the Information you want to Browse By Entering your choice (1/2/3..):
                        1 - Artist
                        2 - Painting
                        3 - ArtObject
                        4 - Collection
                        5 - Sculpture
                        6 - Statue
                        7 - Exhibition
                        8 - Quit Application
                          \n""")

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
        elif (user_query=="8"):
            print("Quitting Application")
            sys.exit(0)
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
            search_value = input("Type the DB Field value you want to search (Use '' Quotes for String/date Values) :")

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
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def DataEntryUser_Insert():
    try:
        user_query = input("""Select the Database Table you Want to do an Insert (1/2/3..):
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
            print("\n ***You selected Artist DB table for an Insert Operation***\n ")
            insert_values = input("""Please type the values for this Tuple separated by commas in the listed sequence :
                                        Name                varchar(30),
                                        DateBorn			integer,
                                        DateDied			integer,
                                        Country				varchar(30),
                                        MainStyle			varchar(30),
                                        Description			varchar(30),
                                        primary key (Name)
                                     \n""")

            insert_query="Insert Into Artist (Name,DateBorn,DateDied,Country, MainStyle,Description) Values "
            insert_query=insert_query + " (" + insert_values +" )"
            #print (insert_query)
            cursor=cnx.cursor()
            cursor.execute(insert_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Insert Operation Completed Successfully \n")
        elif (user_query=="2"):
            print("\n ***You selected Painting DB table for an Insert Operation***\n ")
            insert_values = input("""Please type the values for this Tuple separated by commas in the listed sequence :
                                        IDNum			integer,
                                        PaintType		varchar(30),
                                        DrawnON			varchar(30),
                                        Style			varchar(30)
                                     \n""")

            insert_query="Insert Into Painting (Name,DateBorn,DateDied,Country, MainStyle,Description) Values "
            insert_query=insert_query + " (" + insert_values +" )"
            #print (insert_query)
            cursor=cnx.cursor()
            cursor.execute(insert_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Insert Operation Completed Successfully \n")
        elif (user_query == "3"):
            print("\n ***You selected Artobject DB table for an Insert Operation***\n ")
            insert_values = input("""Please type the values for this Tuple separated by commas in the listed sequence :
                                            IDNum					integer,
                                            Artist					varchar(30),
                                            Year					integer,
                                            Title					varchar(30),
                                            Description				varchar(30),
                                            Epoch					varchar(30),
                                            Category				varchar(30),
                                            Ownership				varchar(30),
                                            primary key (IDNum)
                                     \n""")

            insert_query="Insert Into ArtObject (IDNum,Artist,Year,Title,Description,Epoch,Category,Ownership) Values "
            insert_query=insert_query + " (" + insert_values +" )"
            #print (insert_query)
            cursor=cnx.cursor()
            cursor.execute(insert_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Insert Operation Completed Successfully \n")
        elif (user_query == "4"):
            print("\n ***You selected Collection DB table for an Insert Operation***\n ")
            insert_values = input("""Please type the values for this Tuple separated by commas in the listed sequence :
                                        Name					varchar(30),
                                        Type					varchar(30),
                                        Description				varchar(30),
                                        Address					varchar(50),
                                        Phone					integer,
                                        ContactPerson			varchar(30),
                                        primary key (Name)
                                     \n""")

            insert_query="Insert Into Collection (Name,Type,Description,Address,Phone,ContactPerson ) Values "
            insert_query=insert_query + " (" + insert_values +" )"
            #print (insert_query)
            cursor=cnx.cursor()
            cursor.execute(insert_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Insert Operation Completed Successfully \n")
        elif (user_query == "5"):
            print("\n ***You selected Sculpture DB table for an Insert Operation***\n ")
            insert_values = input("""Please type the values for this Tuple separated by commas in the listed sequence :
                                        IDNum			integer,
                                        Material		varchar(30),
                                        Height			varchar(30),
                                        Weight			varchar(30),
                                        Style			varchar(30)
                                     \n""")

            insert_query="Insert Into Sculpture (IDNum,Material,Height,Weight,Style) Values "
            insert_query=insert_query + " (" + insert_values +" )"
            #print (insert_query)
            cursor=cnx.cursor()
            cursor.execute(insert_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Insert Operation Completed Successfully \n")
        elif (user_query == "6"):
            print("\n ***You selected Statue DB table for an Insert Operation***\n ")
            insert_values = input("""Please type the values for this Tuple separated by commas in the listed sequence :
                                        IDNum			integer,
                                        Material		varchar(30),
                                        Height			varchar(30),
                                        Weight			varchar(30),
                                        Style			varchar(30)
                                     \n""")

            insert_query="Insert Into Statue (IDNum,Material,Height,Weight,Style) Values "
            insert_query=insert_query + " (" + insert_values +" )"
            #print (insert_query)
            cursor=cnx.cursor()
            cursor.execute(insert_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Insert Operation Completed Successfully \n")
        elif (user_query == "7"):
            print("\n ***You selected Exhibition DB table for an Insert Operation***\n ")
            insert_values = input("""Please type the values for this Tuple separated by commas in the listed sequence :
                                        Name			varchar(30),
                                        StartDate		date,
                                        EndDate			date
                                     \n""")

            insert_query="Insert Into Exhibition (Name,StartDate,EndDate) Values "
            insert_query=insert_query + " (" + insert_values +" )"
            #print (insert_query)
            cursor=cnx.cursor()
            cursor.execute(insert_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Insert Operation Completed Successfully \n")
        else:
            print("Please enter a valid key...")
            print("\n")

        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_FIELD_ERROR:
            print("Something went wrong")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def DataEntryUser_Delete():
    try:
        user_query = input("""Select the Database Table you Want to do a Delete Operation (1/2/3..):
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
            print("\n ***You selected Artist DB table for a Delete Operation***\n ")
            delete_condition = input("Type the DB Field name for your delete condition  (like Name,StartDate..):")
            delete_value = input("Type the DB Field value for your delete condition(Use '' Quotes for String/date Values) :")

            delete_query="Delete From Artist Where  "
            delete_query=delete_query + delete_condition + "="+ delete_value
            #print (delete_query)
            cursor=cnx.cursor()
            cursor.execute(delete_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Delete Operation Completed Successfully \n")
        elif (user_query=="2"):
            print("\n ***You selected Painting DB table for a Delete Operation***\n ")
            delete_condition = input("Type the DB Field name for your delete condition  (like IDNum, Style..):")
            delete_value = input("Type the DB Field value for your delete condition(Use '' Quotes for String/date Values) :")

            delete_query="Delete From Painting Where  "
            delete_query=delete_query + delete_condition + "="+ delete_value
            #print (delete_query)
            cursor=cnx.cursor()
            cursor.execute(delete_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Delete Operation Completed Successfully \n")
        elif (user_query == "3"):
            print("\n ***You selected Artobject DB table for a Delete Operation***\n ")
            delete_condition = input("Type the DB Field name for your delete condition  (like Artist,IDNum..):")
            delete_value = input("Type the DB Field value for your delete condition(Use '' Quotes for String/date Values) :")

            delete_query="Delete From Artobject Where  "
            delete_query=delete_query + delete_condition + "="+ delete_value
            #print (delete_query)
            cursor=cnx.cursor()
            cursor.execute(delete_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Delete Operation Completed Successfully \n")
        elif (user_query == "4"):
            print("\n ***You selected Collection DB table for a Delete Operation***\n ")
            delete_condition = input("Type the DB Field name for your delete condition  (like Name,Type..):")
            delete_value = input("Type the DB Field value for your delete condition(Use '' Quotes for String/date Values) :")

            delete_query="Delete From Collection Where  "
            delete_query=delete_query + delete_condition + "="+ delete_value
            #print (delete_query)
            cursor=cnx.cursor()
            cursor.execute(delete_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Delete Operation Completed Successfully \n")
        elif (user_query == "5"):
            print("\n ***You selected Sculpture DB table for a Delete Operation***\n ")
            delete_condition = input("Type the DB Field name for your delete condition  (like Style,IDNum..):")
            delete_value = input("Type the DB Field value for your delete condition(Use '' Quotes for String/date Values) :")

            delete_query="Delete From Sculpture Where  "
            delete_query=delete_query + delete_condition + "="+ delete_value
            #print (delete_query)
            cursor=cnx.cursor()
            cursor.execute(delete_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Delete Operation Completed Successfully \n")
        elif (user_query == "6"):
            print("\n ***You selected Statue DB table for a Delete Operation***\n ")
            delete_condition = input("Type the DB Field name for your delete condition  (like Style,IDNum..):")
            delete_value = input("Type the DB Field value for your delete condition(Use '' Quotes for String/date Values) :")

            delete_query="Delete From Statue Where  "
            delete_query=delete_query + delete_condition + "="+ delete_value
            #print (delete_query)
            cursor=cnx.cursor()
            cursor.execute(delete_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Delete Operation Completed Successfully \n")
        elif (user_query == "7"):
            print("\n ***You selected Exhibition DB table for a Delete Operation***\n ")
            delete_condition = input("Type the DB Field name for your delete condition  (like Name,StartDate..):")
            delete_value = input("Type the DB Field value for your delete condition(Use '' Quotes for String/date Values) :")

            delete_query="Delete From Exhibition Where  "
            delete_query=delete_query + delete_condition + "="+ delete_value
            #print (delete_query)
            cursor=cnx.cursor()
            cursor.execute(delete_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Delete Operation Completed Successfully \n")
        else:
            print("Please enter a valid key...")
            print("\n")

        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_FIELD_ERROR:
            print("Something went wrong")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def DataEntryUser_Update():
    try:
        user_query = input("""Select the Database Table you Want to do an Update Operation (1/2/3..):
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
            print("\n ***You selected Artist DB table for an Update Operation***\n ")
            Update_set_condition=input("Type the DB Field name you want to SET or Update  (like Name,StartDate..):")
            Update_set_value=input("Type the Field value You want to SET or Update(Use '' Quotes for String/date Values) :")
            Update_condition = input("Type the DB Field name for your Update condition  (like Name,StartDate..):")
            Update_value = input("Type the DB Field value for your Update condition(Use '' Quotes for String/date Values) :")


            Update_query="Update Artist SET  "
            Update_query=Update_query+Update_set_condition + "="+Update_set_value+ " Where "+Update_condition+ "="+Update_value
            print (Update_query)
            cursor=cnx.cursor()
            cursor.execute(Update_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Update Operation Completed Successfully \n")
        elif (user_query=="2"):
            print("\n ***You selected Painting DB table for an Update Operation***\n ")
            Update_set_condition=input("Type the DB Field name you want to SET or Update  (like IDNum,Style..):")
            Update_set_value=input("Type the Field value You want to SET or Update(Use '' Quotes for String/date Values) :")
            Update_condition = input("Type the DB Field name for your Update condition  (like IDNum,Style..):")
            Update_value = input("Type the DB Field value for your Update condition(Use '' Quotes for String/date Values) :")


            Update_query="Update Painting SET  "
            Update_query=Update_query+Update_set_condition + "="+Update_set_value+ " Where "+Update_condition+ "="+Update_value
            print (Update_query)
            cursor=cnx.cursor()
            cursor.execute(Update_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Update Operation Completed Successfully \n")
        elif (user_query == "3"):
            print("\n ***You selected Artobject DB table for an Update Operation***\n ")
            Update_set_condition=input("Type the DB Field name you want to SET or Update  (like IDNum,Artist..):")
            Update_set_value=input("Type the Field value You want to SET or Update(Use '' Quotes for String/date Values) :")
            Update_condition = input("Type the DB Field name for your Update condition  (like IDNum,Artist..):")
            Update_value = input("Type the DB Field value for your Update condition(Use '' Quotes for String/date Values) :")


            Update_query="Update Artobject SET  "
            Update_query=Update_query+Update_set_condition + "="+Update_set_value+ " Where "+Update_condition+ "="+Update_value
            print (Update_query)
            cursor=cnx.cursor()
            cursor.execute(Update_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Update Operation Completed Successfully \n")
        elif (user_query == "4"):
            print("\n ***You selected Collection DB table for an Update Operation***\n ")
            Update_set_condition=input("Type the DB Field name you want to SET or Update  (like Name,Type..):")
            Update_set_value=input("Type the Field value You want to SET or Update(Use '' Quotes for String/date Values) :")
            Update_condition = input("Type the DB Field name for your Update condition  (like Name,Type..):")
            Update_value = input("Type the DB Field value for your Update condition(Use '' Quotes for String/date Values) :")


            Update_query="Update Collection SET  "
            Update_query=Update_query+Update_set_condition + "="+Update_set_value+ " Where "+Update_condition+ "="+Update_value
            print (Update_query)
            cursor=cnx.cursor()
            cursor.execute(Update_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Update Operation Completed Successfully \n")
        elif (user_query == "5"):
            print("\n ***You selected Sculpture DB table for an Update Operation***\n ")
            Update_set_condition=input("Type the DB Field name you want to SET or Update  (like IDNum,Style..):")
            Update_set_value=input("Type the Field value You want to SET or Update(Use '' Quotes for String/date Values) :")
            Update_condition = input("Type the DB Field name for your Update condition  (like IDNum,Style..):")
            Update_value = input("Type the DB Field value for your Update condition(Use '' Quotes for String/date Values) :")


            Update_query="Update Sculpture SET  "
            Update_query=Update_query+Update_set_condition + "="+Update_set_value+ " Where "+Update_condition+ "="+Update_value
            print (Update_query)
            cursor=cnx.cursor()
            cursor.execute(Update_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Update Operation Completed Successfully \n")
        elif (user_query == "6"):
            print("\n ***You selected Statue DB table for an Update Operation***\n ")
            Update_set_condition=input("Type the DB Field name you want to SET or Update  (like IDNum,Style..):")
            Update_set_value=input("Type the Field value You want to SET or Update(Use '' Quotes for String/date Values) :")
            Update_condition = input("Type the DB Field name for your Update condition  (like IDNum,Style..):")
            Update_value = input("Type the DB Field value for your Update condition(Use '' Quotes for String/date Values) :")


            Update_query="Update Statue SET  "
            Update_query=Update_query+Update_set_condition + "="+Update_set_value+ " Where "+Update_condition+ "="+Update_value
            print (Update_query)
            cursor=cnx.cursor()
            cursor.execute(Update_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Update Operation Completed Successfully \n")
        elif (user_query == "7"):
            print("\n ***You selected Exhibition DB table for an Update Operation***\n ")
            Update_set_condition=input("Type the DB Field name you want to SET or Update  (like Name,StartDate..):")
            Update_set_value=input("Type the Field value You want to SET or Update(Use '' Quotes for String/date Values) :")
            Update_condition = input("Type the DB Field name for your Update condition  (like Name,StartDate..):")
            Update_value = input("Type the DB Field value for your Update condition(Use '' Quotes for String/date Values) :")


            Update_query="Update Exhibition SET  "
            Update_query=Update_query+Update_set_condition + "="+Update_set_value+ " Where "+Update_condition+ "="+Update_value
            print (Update_query)
            cursor=cnx.cursor()
            cursor.execute(Update_query)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\nYour Update Operation Completed Successfully \n")
        else:
            print("Please enter a valid key...")
            print("\n")

        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_FIELD_ERROR:
            print("Something went wrong")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)