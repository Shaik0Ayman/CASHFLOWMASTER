import mysql.connector as m

# Function to create a database or table
# create(database or table , Name , if table then database name)
mysql_pass = input("Enter your MySQL Password>>>")
mydb = m.connect(
    host = "localhost", 
    user = "root",
    password = mysql_pass
)

c = mydb.cursor()
dbname = 'CASHFLOWMASTER'
try:
    c.execute("CREATE DATABASE {}".format(dbname))
except:
    pass

def createtb(dbname, tbname):
    c.execute("USE {}".format(dbname))
    c.execute("CREATE TABLE {}".format(tbname))

def insert_rec(dbname, tbname, value_list):
    c.execute("USE {}".format(dbname))
    c.execute("INSERT INTO {} VALUES{}".format(tbname, tuple(value_list)))

def delete_rec(dbname, tbname, field_name, del_value):
    c.execute("USE {}".format(dbname))
    c.execute("DELETE FROM {} WHERE {} = {}".format(tbname, field_name, del_value))

def updatetb(dbname, tbname, condition, update):
    c.execute("USE {}".format(dbname))
    c.execute("UPDATE {} SET {} WHERE {}".format(tbname, update, condition))
