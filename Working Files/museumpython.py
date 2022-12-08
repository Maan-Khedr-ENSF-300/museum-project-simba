import mysql.connector

#THIS IS THE USERNAME AND PASSCODE
#user = root, passcode = 1234

def menu():
    tablewanted = input('please enter which table you would like to veiw: \n 1. View the all Art pieces information \n 2. view the paintings information \n 3. view the statues information \n 4. view the sculptures information \n 5. view the all the artists information \n you choice: ')
    print('you have chosen', tablewanted)
    return tablewanted

userinput = input('please enter your user name: ')
passcode = input ('please enter your passcode: ')



cnx = mysql.connector.connect(
    user = userinput,
    port = 3306, 
    password = passcode,
    host='127.0.0.1')

cursor = cnx.cursor()
cursor.execute('SELECT CURDATE()')
row = cursor.fetchone()
print('current date is: {0}'.format(row[0]))

# display (2a)

tablewanted = menu()



if tablewanted == '1' :
    cursor.execute('use Museum')
    cursor.execute('select * from ArtObject')
    colnames = cursor.column_names
    print('Attribute list: \n')
    attsize = len(colnames)
    for i in range (attsize):
        print(colnames[i], '\t', end = '')
    print()
    print(110*'-')
    rows = cursor.fetchall()
    print('current rows: \n')
    size = len(rows)
    for i in range(size):
        for x in range(len(rows[i])):
            print(rows[i][x], end = '\t')
        print()


    '''
    rows = cursor.fetchone()
    print('number of entries in table \n', len(rows))
    print('content of table \n', rows)
      
    print('number of entries in table \n', len(rows))
    print('content of table \n', rows)
    
    '''

    '''

    colnames = cursor.column_names
    print('Attribute list: \n' , colnames)
    
    
    print('number of entries in table \n', len(rows))
    print('content of table \n', rows)
    
 

    print('all art pieces information: \n')
    #cursor.execute('use Museum')
    cursor.execute('select * from ArtObject')
    #rows = cursor.fetchall()
    size = len(rows)
    for i in range(size-1):
            print(row[i])


    '''

if tablewanted == '2' :
    
    cursor.execute('use Museum')
    cursor.execute('select * from Painting')
    colnames = cursor.column_names
    #attsize = len(colnames)
    print('Attribute list: \n')
    attsize = len(colnames)
    for i in range (attsize):
        print(colnames[i], '\t', end = '')
    print()
    print(110*'-')
    rows = cursor.fetchall()
    print('current rows: \n')
    size = len(rows)
    for i in range(size):
        for x in range(len(rows[i])):
            print(rows[i][x], end = '\t')
        print()


if tablewanted == '3' :
    
    cursor.execute('use Museum')
    cursor.execute('select * from Statue')
    colnames = cursor.column_names
    #attsize = len(colnames)
    print('Attribute list: \n')
    attsize = len(colnames)
    for i in range (attsize):
        print(colnames[i], '\t', end = '')
    print()
    print(110*'-')
    rows = cursor.fetchall()
    print('current rows: \n')
    size = len(rows)
    for i in range(size):
        for x in range(len(rows[i])):
            print(rows[i][x], end = '\t')
        print()

if tablewanted == '4' :
    
    cursor.execute('use Museum')
    cursor.execute('select * from Sculpture')
    colnames = cursor.column_names
    #attsize = len(colnames)
    print('Attribute list: \n')
    attsize = len(colnames)
    for i in range (attsize):
        print(colnames[i], '\t', end = '')
    print()
    print(110*'-')
    rows = cursor.fetchall()
    print('current rows: \n')
    size = len(rows)
    for i in range(size):
        for x in range(len(rows[i])):
            print(rows[i][x], end = '\t')
        print()

if tablewanted == '5' :
    cursor.execute('use Museum')
    cursor.execute('select * from Artist')
    colnames = cursor.column_names
    #attsize = len(colnames)
    print('Attribute list: \n')
    attsize = len(colnames)
    for i in range (attsize):
        print(colnames[i], '\t', end = '')
    print()
    print(110*'-')
    rows = cursor.fetchall()
    print('current rows: \n')
    size = len(rows)
    for i in range(size):
        for x in range(len(rows[i])):
            print(rows[i][x], end = '\t')
        print()




cnx.close()