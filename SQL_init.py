import pickle as pk
import mysql.connector as m

db = m.connect(
    host="localhost",
    user="root",
    passwd="Pianist1",
)
udb = "cashflowmaster"
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(udb))
cursor.execute("USE {}".format(udb))
try:
    with open('users.bin', 'rb') as f:
        users = pk.load(f)
except:
    with open('users.bin', 'wb') as f:
        pk.dump([], f)
cursor.execute("CREATE TABLE IF NOT EXISTS users (username varchar(30) PRIMARY KEY, password varchar(16), income int(20), exp int(20), emi int(20))")

def create_user_tables(username):
    cursor.execute("CREATE TABLE IF NOT EXISTS assets_{}(asset_name varchar(20), asset_price int(20))".format(username))
    cursor.execute("CREATE TABLE IF NOT EXISTS expenses_{}(expense_name varchar(20), expense_price int(20))".format(username))

def create_user(username, user_password):
    with open('users.bin', 'ab') as f:
        pk.dump([username, user_password, 0, 0, 0], f)
    cursor.execute("INSERT INTO users VALUES('{}', '{}', 0, 0, 0)".format(username, user_password))
    db.commit()
    create_user_tables(username)

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