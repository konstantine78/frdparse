import mysql.connector
DB_NAME = "iodb"
sql_delete_command = "DROP DATABASE " + DB_NAME


cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password1234",
    database = DB_NAME,
)
#cnx = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    passwd = "password1234",
#    database = "iodb",
#)

# Create instance of cursor.
cursor = cnx.cursor()

#Delete the database:
"DROP DATABASE "