from SQL_init import *
from tkinter import *
from tkinter import messagebox

root = Tk()

def firstwin():
    root.geometry("250x230")
    root.title("LOGIN PAGE")
    root.configure(bg="black")
    label1  = Label(root, text="CASH FLOW MASTER", fg = "white", bg = "black")
    label1.pack()
    label2  = Label(root, text="", fg = "white", bg = "black")
    label2.pack()
    label3  = Label(root, text="enter username:", fg = "white", bg = "black")
    label3.pack()
    u = Entry(root, width=30, fg = "white", bg = "black")
    u.pack()
    global username
    username = u.get()
    label4  = Label(root, text="enter password:", fg = "white", bg = "black")
    label4.pack()
    p = Entry(root, width=30, fg = "white", bg = "black", show="*")
    p.pack()
    global user_password
    user_password = p.get()
    def verify():
        try:   
            if (username == user_password):
                root.destroy()
                from page2 import secwin
                secwin()
            else:
                error_auth = messagebox.showwarning("ERROR", "Incorrect username or password")
                Label(root, text= error_auth).pack()
        except m.ProgrammingError as e:
            error_mysql = messagebox.showwarning("ERROR", e)
            Label(root, text= error_mysql).pack()
    label5  = Label(root, text="", fg = "white", bg = "black")
    label5.pack()
    button1 = Button(root, text="submit", command=verify, padx=10, pady=10, bg="green" , fg = "white")    
    button1.pack()
    label0  = Label(root, text="", fg = "white", bg = "black")
    label0.pack()
firstwin()
root.mainloop()

