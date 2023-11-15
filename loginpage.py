from SQL_init import *
from tkinter import *
from tkinter import messagebox

root = Tk()

def firstwin():
    root.geometry("250x200")
    root.title("LOGIN PAGE")
    label1  = Label(root, text="CASH FLOW MASTER")
    label1.pack()
    label2  = Label(root, text="enter mysql password:")
    label2.pack()
    sqlpass = Entry(root, width=30)
    sqlpass.pack()
    sql_pass = sqlpass.get()
    label3  = Label(root, text="enter username:")
    label3.pack()
    u = Entry(root, width=30)
    u.pack()
    username = u.get()
    label4  = Label(root, text="enter password:")
    label4.pack()
    p = Entry(root, width=30)
    p.pack()
    user_password = p.get()
    
    def verify():
        try:
            global c
            c = connect_cursor(sql_pass)
        except m.Error as e:
            error_mysql = messagebox.showwarning("ERROR", e)
            Label(root, text= error_mysql).pack()

        if user_check(c, username, user_password):
            root.destroy()
            from page2 import secwin
            secwin()
        else:
            error_auth = messagebox.showwarning("ERROR", "Incorrect username or password")
            Label(root, text= error_auth).pack()

    button1 = Button(root, text="submit", command=verify, padx=10, pady=10, bg="green" )    
    button1.pack()


firstwin()
root.mainloop()
