
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
    mysqlpass = Entry(root, width=30)
    mysqlpass.pack()
    label3  = Label(root, text="enter username:")
    label3.pack()
    u = Entry(root, width=30)
    u.pack()
    label4  = Label(root, text="enter password:")
    label4.pack()
    p = Entry(root, width=30)
    p.pack()
    label4  = Label(root, text="sql password:")
    label4.pack()
    S = Entry(root, width=30)
    S.pack()
    

    

    global passw
    sql_pass = mysqlpass.get()

    def check():
        user = u.get()
        passw = p.get()
        if ():
            root.destroy()
            from page2 import secwin
            secwin()
        else:
            error = messagebox.showwarning("inccorect password or username", "inccorect password or username")
            Label(root, text= error).pack()
            
           
    
    button1 = Button(root, text="submit", command=check, padx=10, pady=10, fg="green" )    
    button1.pack()


firstwin()
root.mainloop()
