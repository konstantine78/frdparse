import mysql.connector
from mysql.connector import errorcode
'''
-------------------
mysql_lib 
-------------------
The mysql_lib module contains five globals:
1. DB_HOST - database host value
2. DB_USER - database user value
3. DB_PASSWORD - database password value
4. DB_NAME - database name value
5. tables - dictionary of table creation commands for use in methods.

Four tables are created:
1. Inputs
2. Outputs
3. Constants
4. Faults

'''
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'password1234'
DB_NAME = 'MySQLDatabase'

tables = {}
tables['Inputs'] = ('''CREATE TABLE Inputs (id INT AUTO_INCREMENT PRIMARY KEY, 
SectionID VARCHAR(255), ObjectID VARCHAR(255), Name VARCHAR(255), VI_Name VARCHAR(255), 
DataType VARCHAR(255), DataTypeAbbrev VARCHAR(255), Source VARCHAR(255), Intermediate VARCHAR(255))''')

tables['Outputs'] = ('''CREATE TABLE Outputs (id INT AUTO_INCREMENT PRIMARY KEY, 
SectionID VARCHAR(255), ObjectID VARCHAR(255), Name VARCHAR(255), VI_Name VARCHAR(255), 
DataType VARCHAR(255), DataTypeAbbrev VARCHAR(255), Destination VARCHAR(255))''')

tables['Constants'] = ('''CREATE TABLE Constants (id INT AUTO_INCREMENT PRIMARY KEY, 
SectionID VARCHAR(255), ObjectID VARCHAR(255), Name VARCHAR(255), VI_Name VARCHAR(255), 
DataType VARCHAR(255), DataTypeAbbrev VARCHAR(255), ConstType VARCHAR(255), Units VARCHAR(255), 
DefaultValue VARCHAR(255), MinimumValue VARCHAR(255), MaximumValue VARCHAR(255))''')

tables['Faults'] = ('''CREATE TABLE Faults (id INT AUTO_INCREMENT PRIMARY KEY, 
SectionID VARCHAR(255), ObjectID VARCHAR(255), Name VARCHAR(255), VI_Name VARCHAR(255), 
FaultCode VARCHAR(255), Description VARCHAR(255), CumulativeLimit VARCHAR(255), ConsecutiveLimit VARCHAR(255))''')

def create_database(theHost, theUser, thePassword, theDatabase):
    '''
    create_database(theHost, theUser, thePassword, theDatabase): Attempts to make a connection with MySQL, 
    and once the connection is made and cursor created, a database can be made.  The connection is made using
    the arguments passed into this method.

    '''
    try:
        connection = mysql.connector.connect(
            host = theHost,
            user = theUser,
            passwd = thePassword
        )
        cursor = connection.cursor()
        print('A successful cursor has been made with connection to the {} database.'.format(theDatabase))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Your HOST, USER, or PASSWORD settings are invalid/incorrect.')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Your database does not exist.')
        else:
            print(err)

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
    '''
    create_tables(database): Creates the various MSYQL tables in the database that is passed in as an argument.
    It uses the tables dictionary to call each individual table command.

    '''
    try:
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            passwd = DB_PASSWORD,
            database = database
        )
        cursor = connection.cursor()
        print('You have successfully connected to the {} database.'.format(database))
    except mysql.connector.Error as err:
        print(err)

    for individual_table in tables:
        table_command = tables[individual_table]
        try:
            cursor.execute(table_command)
            connection.commit()
        except mysql.connector.Error as err:
            print(err)
    close_connection(connection, 'create_tables method')

def update_inputs_table(database, inputs):
    '''
    update_inputs_table(database, inputs): Inserts the contents of the 'inputs' list into the Inputs table that resides
    in the 'database'.

    '''
    try:
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            passwd = DB_PASSWORD,
            database = database
        )
        cursor = connection.cursor()
        print('You have successfully connected to the {} database.'.format(database))
    except mysql.connector.Error as err:
        print(err)

    for i in inputs:
        command = '''INSERT INTO Inputs (SectionID, ObjectID, Name, VI_Name, DataType, DataTypeAbbrev, Source, Intermediate) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''

        commandTuple = (i.sectionID, i.objectID, i.name, i.vi_name, i.datatype, i.datatype_abbreviated, i.source, i.intermediate)
        try:
            cursor.execute(command, commandTuple)
            connection.commit()
        except mysql.connector.Error as err:
            print(err)
    close_connection(connection, 'update_inputs_table method')
 
def update_outputs_table(database, outputs):
    '''
    update_outputs_table(database, outputs): Inserts the contents of the 'outputs' list into the Outputs table that resides
    in the 'database'.

    '''
    try:
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            passwd = DB_PASSWORD,
            database = database
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        print(err)

    for o in outputs:
        command = '''INSERT INTO Outputs (SectionID, ObjectID, Name, VI_Name, DataType, DataTypeAbbrev, Destination) 
        VALUES(%s,%s,%s,%s,%s,%s,%s)'''

        commandTuple = (o.sectionID, o.objectID, o.name, o.vi_name, o.datatype, o.datatype_abbreviated, o.destination)
        try:
            cursor.execute(command, commandTuple)
            connection.commit()
        except mysql.connector.Error as err:
            print(err)
    close_connection(connection, 'update_outputs_table method')

def update_constants_table(database, constants):
    '''
    update_constants_table(database, constants): Inserts the contents of the 'constants' list into the Constants 
    table that resides in the 'database'.

    '''
    try:
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            passwd = DB_PASSWORD,
            database = database
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        print(err)

    for c in constants:
        command = '''INSERT INTO Constants (SectionID, ObjectID, Name, VI_Name, DataType, DataTypeAbbrev, ConstType, Units, DefaultValue, MinimumValue, MaximumValue) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

        commandTuple = (c.sectionID, c.objectID, c.name, c.vi_name, c.datatype, c.datatype_abbreviated, c.const_type, c.units, c.defaultvalue, c.minvalue, c.maxvalue)
        try:
            cursor.execute(command, commandTuple)
            connection.commit()
        except mysql.connector.Error as err:
            print(err)

    close_connection(connection, 'update_constants_table method')

def update_faults_table(database, faults):
    '''
    update_faults_table(database, faults): Inserts the contents of the 'faults' list into the Faults table 
    that resides in the 'database'.

    '''
    try:
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            passwd = DB_PASSWORD,
            database = database
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        print(err)

    for f in faults:
        command = '''INSERT INTO Faults (SectionID, ObjectID, Name, VI_Name, FaultCode, Description, CumulativeLimit, ConsecutiveLimit) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''

        commandTuple = (f.sectionID, f.objectID, f.faultname, f.vi_name, f.faultcode, f.faultdescr, f.faultcumlimit, f.faultconlimit)
        try:
            cursor.execute(command, commandTuple)
            connection.commit()
        except mysql.connector.Error as err:
            print(err)
    close_connection(connection, 'update_faults_table method')