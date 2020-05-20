import mysql.connector
from mysql.connector import errorcode

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'password1234'
DB_NAME = 'MySQLDatabase'

tables = {}
tables['Inputs'] = ('''CREATE TABLE Inputs (id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), DataType VARCHAR(255),
ObjectID VARCHAR(255), Source VARCHAR(255), Units VARCHAR(255), InitialValue VARCHAR(255))''')

tables['Outputs'] = (
    "CREATE TABLE 'Outputs' ("
    "'UniqueID' int(11) NOT NULL AUTO_INCREMENT,"
    "'Name' varchar(255) NOT NULL,"
    "'DataType' varchar(255) NOT NULL,"
    #"'DataTypeAbbreviated' varchar(255) NOT NULL,"
    "'ObjectID' varchar(255) NOT NULL,"
    #"'Source' varchar(255) NOT NULL,"
    "'Destination' varchar(255) NOT NULL,"
    "'Units' varchar(255) NOT NULL,"
    "'DefaultValue' varchar(255) NOT NULL,"
    #"'MinValue' varchar(255) NOT NULL,"
    #"'MaxValue' varchar(255) NOT NULL"
    )
    
tables['AlignmentConstants'] = (
    "CREATE TABLE 'AlignmentConstants' ("
    "'UniqueID' int(11) NOT NULL AUTO_INCREMENT,"
    "'Name' varchar(255) NOT NULL,"
    "'DataType' varchar(255) NOT NULL,"
    #"'DataTypeAbbreviated' varchar(255) NOT NULL,"
    "'ObjectID' varchar(255) NOT NULL,"
    #"'Source' varchar(255) NOT NULL,"
    #"'Destination' varchar(255) NOT NULL,"
    "'Units' varchar(255) NOT NULL,"
    "'DefaultValue' varchar(255) NOT NULL,"
    "'MinValue' varchar(255) NOT NULL,"
    "'MaxValue' varchar(255) NOT NULL"
    )
    
tables['DesignConstants'] = (
    "CREATE TABLE 'DesignConstants' ("
    "'UniqueID' int(11) NOT NULL AUTO_INCREMENT,"
    "'Name' varchar(255) NOT NULL,"
    "'DataType' varchar(255) NOT NULL,"
    #"'DataTypeAbbreviated' varchar(255) NOT NULL,"
    "'ObjectID' varchar(255) NOT NULL,"
    #"'Source' varchar(255) NOT NULL,"
    #"'Destination' varchar(255) NOT NULL,"
    "'Units' varchar(255) NOT NULL,"
    "'DefaultValue' varchar(255) NOT NULL,"
    #"'MinValue' varchar(255) NOT NULL,"
    #"'MaxValue' varchar(255) NOT NULL"
    )

tables['LocalVariables'] = (
    "CREATE TABLE 'LocalVariables' ("
    "'UniqueID' int(11) NOT NULL AUTO_INCREMENT,"
    "'Name' varchar(255) NOT NULL,"
    "'DataType' varchar(255) NOT NULL,"
    #"'DataTypeAbbreviated' varchar(255) NOT NULL,"
    "'ObjectID' varchar(255) NOT NULL,"
    #"'Source' varchar(255) NOT NULL,"
    "'Destination' varchar(255) NOT NULL,"
    #"'Units' varchar(255) NOT NULL,"
    "'DefaultValue' varchar(255) NOT NULL,"
    #"'MinValue' varchar(255) NOT NULL,"
    #"'MaxValue' varchar(255) NOT NULL"
    )

tables['ApplicationFaults'] = (
    "CREATE TABLE 'ApplicationFaults' ("
    "'UniqueID' int(11) NOT NULL AUTO_INCREMENT,"
    "'Name' varchar(255) NOT NULL,"
    "'Code' varchar(255) NOT NULL,"
    "'Description' varchar(255) NOT NULL,"
    "'ObjectID' varchar(255) NOT NULL,"
    "'CumulativeLimit' int(11) NOT NULL,"
    "'ConsecutiveLimit' int(11) NOT NULL,"
    )

def create_database(theHost, theUser, thePassword, theDatabase):
    '''
    First a connector must be made with MySQL, before a database is made.
    Once the connection is made, a database is created.
    '''
    try:
        connection = mysql.connector.connect(
            host = theHost,
            user = theUser,
            passwd = thePassword
        )
        #print('A successful connection has been made to the {} database.'.format(theDatabase))
        cursor = connection.cursor()
        print('A successful cursor has been made with connection to the {} database.'.format(theDatabase))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Your HOST, USER, or PASSWORD settings are invalid/incorrect.')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Your database does not exist.')
        else:
            print(err)

    '''
    If the connection has succeeded, we can now create database.

    '''
    try:
        cursor.execute(
            'CREATE DATABASE {}'.format(theDatabase)
        )
        print('You have successfully created the {} database.'.format(theDatabase))

    except mysql.connector.Error as err:
        print('Failed creating database: {}!!!'.format(err))
    close_connection(connection, 'create_database method')

def delete_database(database):
    try:
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            passwd = DB_PASSWORD, 
            database = database
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Your HOST, USER, or PASSWORD settings are invalid/incorrect.')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Your database does not exist.')
        else:
            print(err)
    cursor.execute('DROP database IF EXISTS ' + database)

    print('Deleted database: {}'.format(database))
    close_connection(connection, 'delete_database method')

def close_connection(connection, source):
    print('Closing MYSQL connection from {}.'.format(source))
    connection.close()

def create_tables(database):
    try:
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            passwd = DB_PASSWORD,
            database = database
        )
        print('A successful connection has been made to the {} database.'.format(database))
        cursor = connection.cursor()
        print('A successful cursor has been made with connection to the {} database.'.format(database))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Your HOST, USER, or PASSWORD settings are invalid/incorrect.')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Your database does not exist.')
        else:
            print(err)

    for individual_table in tables:
        table_command = tables[individual_table]
        try:
            print('Creating table {}:'.format(individual_table),end='')
            cursor.execute(table_command)
            cursor.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Table {} already exists.'.format(individual_table))
    close_connection(connection, 'create_tables method')

def update_input_table(database, inputs):
    pass
    #connection = create_connection(DB_HOST, DB_USER, DB_PASSWORD, database)
    #cursor = connection.cursor()
    #command = '''INSERT INTO Inputs VALUES(
    #    :Name, :DataType, :ObjectID, :Source, :Units, :DefaultValue)''',{'Name':inputs.name, 'DataType':inputs.datatype, 'ObjectID':inputs.objectID, 'Source':inputs.source, 'Units':inputs.units, 'DefaultValue':inputs.defaultvalue}
    #cursor.execute(command)
    #cursor.commit()
    #    
    #print('Added {} to the Inputs table.'.format(inputs.name))
    #cursor.close_connection(connection)
