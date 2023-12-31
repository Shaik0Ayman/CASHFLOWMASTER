import mysql.connector as m

db = m.connect(
    host="localhost",
    user="root",
    passwd="0786",
)
udb = "cashflowmaster"
with open('temp.txt', 'r+') as f:
    username = f.read()
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(udb))
cursor.execute("USE {}".format(udb))
cursor.execute("CREATE TABLE IF NOT EXISTS users (username varchar(30) PRIMARY KEY, income int(40), exp int(40), emi int(40))")

def create_user(username):
    create_user_tables(username)
    cursor.execute("INSERT INTO users VALUES('{}', 0, 0, 0)".format(username))
    db.commit()

def create_user_tables(username):
    cursor.execute("CREATE TABLE IF NOT EXISTS assets_{}(asset_name varchar(40), asset_price int(40))".format(username))
    cursor.execute("CREATE TABLE IF NOT EXISTS expenses_{}(expense_name varchar(40), expense_price int(40))".format(username))

def user_check(username, user_password):
    if (username in cursor.execute("SELECT username FROM users WHERE username = {}".format(username)).fetchone()[0] and
        user_password in cursor.execute("SELECT password FROM users WHERE username = {}".format(username)).fetchone()[0]):
        return True
    else:
        return False

def insert_asset(username, asset_name, asset_price):
    cursor.execute("INSERT INTO assets_{} VALUES('{}', {})".format(username, asset_name, asset_price))
    db.commit()

def insert_expense(username, expense_name, expense_price):
    cursor.execute("INSERT INTO expenses_{} VALUES('{}', {})".format(username, expense_name, expense_price))
    db.commit()

def update_asset(username, asset_name, asset_price):
    cursor.execute("UPDATE assets_{} SET asset_price = {} WHERE asset_name = '{}'".format(username, asset_price, asset_name))
    db.commit()

def update_expense(username, expense_name, expense_price):
    cursor.execute("UPDATE expenses_{} SET expense_price = {} WHERE expense_name = '{}'".format(username, expense_price, expense_name))
    db.commit()

def delete_asset(username, asset_name):
    cursor.execute("DELETE FROM assets_{} WHERE asset_name = '{}'".format(username, asset_name))
    db.commit()

def delete_expense(username, expense_name):
    cursor.execute("DELETE FROM expenses_{} WHERE expense_name = '{}'".format(username, expense_name))
    db.commit()

def delete_user(username):
    cursor.execute("DELETE FROM users WHERE username = '{}'".format(username))
    cursor.execute("DROP TABLE expenses_{}, assets_{}".format(username, username))
    db.commit()