import mysql.connector
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password1234"
DB_NAME = "MyDefaultDatabaseToDelete"
#sql_delete_command = "DROP DATABASE " + DB_NAME

def create_database(nameDB):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('CREATE database ' + nameDB)
    close_connection(conn)
    print('Successful createion of database ' + nameDB)

def delete_database(nameDB):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DROP database IF EXISTS ' + nameDB)
    close_connection(conn)

def create_inputs_table(nameDB):
    conn = create_connection(nameDB)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Inputs (
        Name,
        ObjectID,
        DataType,
        DataTypeAbbreviated,
        SourceID)'''
        )
    cursor.commit()
    cursor.close_connection()

def create_outputs_table(nameDB):
    conn = create_connection(nameDB)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Outputs (
        Name,
        ObjectID,
        DataType,
        DataTypeAbbreviated,
        SourceID)'''
        )
    cursor.commit()
    cursor.close_connection()

def create_alignconsts_table(nameDB):
    conn = create_connection(nameDB)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE AlignConstants (
        Name,
        ObjectID,
        DataType,
        DataTypeAbbreviated,
        SourceID)'''
        )
    cursor.commit()
    cursor.close_connection()

def create_designconsts_table(nameDB):
    conn = create_connection(nameDB)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE DesignConstants (
        Name,
        ObjectID,
        DataType,
        DataTypeAbbreviated,
        SourceID)'''
        )
    cursor.commit()
    cursor.close_connection()

def create_connection(theHost=DB_HOST, theUser=DB_USER, thePassword=DB_PASSWORD, theDatabase='0'):
    '''
    --------------------------------------------------------------------------------------
    Method create_connection:
    Creates a python connection to MySQL.  This method serves as an "overloaded" function,
    in that it can accept a database name for returning a connection to a specific MySQL database
    or simply returning a MySQL connection.
    '''
    if str(theDatabase).strip() == '0': # Just want a connector.  No database yet.
        return mysql.connector.connect(
            host = theHost, #"localhost",
            user = theUser, #"root",
            passwd = thePassword, #"password1234",
            )
    else:
        return mysql.connector.connect(
            host = theHost, #"localhost",
            user = theUser, #"root",
            passwd = thePassword, #"password1234",
            database = theDatabase,
        )

def close_connection(connection):
    connection.close()
