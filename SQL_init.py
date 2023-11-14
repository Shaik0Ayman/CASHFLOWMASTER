import mysql.connector as m

def connect_cursor(sql_pass):
    mydb = m.connect(
        host = "localhost", 
        user = "root",
        password = sql_pass
    )
    cursor = mydb.cursor()
    return cursor

def data_init(cursor):
    udb = "users_cashflowmaster"
    cursor.execute("CREATE DATABASE {}".format(udb))
    cursor.execute("USE {}".format(udb))
    cursor.execute("CREATE TABLE users(username varchar(30) PRIMARY KEY, password varchar(16), income int(20), exp int(20), emi int(20)")

def create_user(cursor, uid, username, user_password):
    cursor.execute("INSERT INTO users VALUES({}, '{}', '{}', 0, 0, 0)".format(uid, username, user_password))

def user_check(cursor, username, user_password):
    if username in cursor.execute("SELECT username FROM users WHERE username = {}".format(username)).fetchone()[0] and user_password == cursor.execute("SELECT password FROM users WHERE username = {}".format(username)).fetchone()[0]:
        return True

def create_user_tables(cursor, username):
    cursor.execute("CREATE TABLE assets_{}(asset_name varchar(20), asset_price int(20))".format(username))
    cursor.execute("CREATE TABLE expenses_{}(expense_name varchar(20), expense_price int(20))".format(username))

def insert_asset(cursor, username, asset_name, asset_price):
    cursor.execute("INSERT INTO assets_{} VALUES('{}', {})".format(username, asset_name, asset_price))

def insert_expense(cursor, username, expense_name, expense_price):
    cursor.execute("INSERT INTO expenses_{} VALUES('{}', {})".format(username, expense_name, expense_price))

def update_asset(cursor, username, asset_name, asset_price):
    cursor.execute("UPDATE assets_{} SET asset_price = {} WHERE asset_name = '{}'".format(username, asset_price, asset_name))

def update_expense(cursor, username, expense_name, expense_price):
    cursor.execute("UPDATE expenses_{} SET expense_price = {} WHERE expense_name = '{}'".format(username, expense_price, expense_name))

def delete_asset(cursor, username, asset_name):
    cursor.execute("DELETE FROM assets_{} WHERE asset_name = '{}'".format(username, asset_name))

def delete_expense(cursor, username, expense_name):
    cursor.execute("DELETE FROM expenses_{} WHERE expense_name = '{}'".format(username, expense_name))

def delete_user(cursor, username):
    cursor.execute("DELETE FROM users WHERE username = '{}'".format(username))
    cursor.execute("DROP TABLE expenses_{}, assets_{}".format(username))
