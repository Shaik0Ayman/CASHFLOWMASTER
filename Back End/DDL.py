import mysql.connector

# Function to create a database or table
# create(database or table , Name , if table then database name)
mysql_pass = input("Enter your MySQL Password>>>")
mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = mysql_pass
)

c = mydb.cursor()

def createdb(name):
    c.execute("CREATE DATABASE {}".format(name))

def createtb(dbname, name):
    c.execute("USE {}".format(dbname))
    c.execute("CREATE TABLE {}".format(name))

def insert(dbname, name, value_list):
    c.execute("USE {}".format(dbname))
    c.execute("INSERT INTO {} VALUES{}".format(name, tuple(value_list)))