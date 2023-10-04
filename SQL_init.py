import mysql.connector as m
def init():
    from loginpage import sqlpass
    #mysql_pass = sqlpass()
    mysql_pass = password
    mydb = m.connect(
        host = "localhost", 
        user = "root",
        password = mysql_pass
    )

    c = mydb.cursor()
    udb = "users_cashflowmaster"
    db = "cashflowmaster"
def showdb():
    from loginpage import sqlpass
    mysql_pass = sqlpass()
    mydb = m.connect(
        host = "localhost", 
        user = "root",
        password = mysql_pass
    )

    c = mydb.cursor()

    c.execute("SHOW DATABASES")
    L1 = []
    for i in c:
        L1.append(i)
    return L1
def db(dbname):
    c.execute("CREATE DATABASE {}".format(dbname))
    c.execute("USE {}".format(dbname))
    db(udb)
    c.execute("CREATE TABLE users(uid INT(20) PRIMARY KEY, username varchar(30), password varchar(16)")