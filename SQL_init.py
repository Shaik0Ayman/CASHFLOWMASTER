import mysql.connector as m
from loginpage import passw
mydb = m.connect(
    host = "localhost", 
    user = "root",
    password = passw
)

c = mydb.cursor()

udb = "users_cashflowmaster"
c.execute("CREATE DATABASE {}".format(udb))
c.execute("USE {}".format(udb))
c.execute("CREATE TABLE users(uid INT(20) PRIMARY KEY, username varchar(30), password varchar(16), income int(20), exp int(20), emi int(20)")

def create_asset(username):
    c.execute("CREATE TABLE assets_{}(asset_name varchar(20), asset_price int(20))".format(username))