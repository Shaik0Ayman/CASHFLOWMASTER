import mysql.connector as m

# Function to create a database or table
# create(database or table , Name , if table then database name)
from loginpage import sqlpass
mysql_pass = sqlpass()
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
c.execute("USE {}".format(dbname))

def init_tables():
    c.execute("CREATE TABLE monthly_salary()")