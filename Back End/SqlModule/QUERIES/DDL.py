

import mysql.connector

# Function to create a database or table
# create(database or table , Name , if table then database name)
def create(dort, name, dbname):
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        password="0786"
    )
    c = mydb.cursor()

    if dort == 'd':
        c.execute("CREATE DATABASE {}".format(name))
    elif dort == 't':
        c.execute("USE {}".format(dbname))
        c.execute("CREATE TABLE {}".format(name))

