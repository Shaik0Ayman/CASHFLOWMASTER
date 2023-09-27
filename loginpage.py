from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
def secwin():
    root.wm_state("iconic")
    top = Toplevel()
    top.title("CASH FLOW MASTER")
    top.geometry("400x400")
    label5 = Label(top, text="CASH FLOW MASTER")
    label5.pack()



def firstwin():
    root.geometry("250x150")
    root.title("LOGIN PAGE")
    label1  = Label(root, text="CASH FLOW MASTER")
    label1.pack()
    label2  = Label(root, text="enter username:")
    label2.pack()
    u = Entry(root, width=30)
    u.pack()
    label3  = Label(root, text="enter password:")
    label3.pack()
    p = Entry(root, width=30)
    p.pack()
    label6  = Label(root, text="enter your sql password:")
    label6.pack()
    s = Entry(root, width=30)
    s.pack()
    global sqlpass
    sqlpass = s.get()
    
    def check():
        user = u.get()
        passw = p.get()
        if (user == "ayman" and passw == "ayman"):
            w = "welcome : " + u.get()
            label4 = Label(root, text= w)    
            label4.pack()
            secwin()   
        else:
            error = messagebox.showwarning("inccorect password or username", "inccorect password or username")
            Label(root, text= error).pack()
    button1 = Button(root, text="submit", command=check, padx=10, pady=10, fg="green" )    
    button1.pack()
    
firstwin()
root.mainloop()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=sqlpass,
    )
