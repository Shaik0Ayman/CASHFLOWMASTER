from tkinter import *
from tkinter import messagebox


root1 = Tk()

def win():
    root1.geometry("250x230")
    root1.title("NEW USER")
    root1.configure(bg="black")
    label1  = Label(root1, text="CASH FLOW MASTER", fg = "white", bg = "black")
    label1.pack()
    label2  = Label(root1, text="", fg = "white", bg = "black")
    label2.pack()
    label3  = Label(root1, text="enter username:", fg = "white", bg = "black")
    label3.pack()
    u = Entry(root1, width=30, fg = "white", bg = "black")
    u.pack()
    global username
    username = u.get()
    label4  = Label(root1, text="enter password:", fg = "white", bg = "black")
    label4.pack()
    p = Entry(root1, width=30, fg = "white", bg = "black", show="*")
    p.pack()
    global user_password
    user_password = p.get()
    def dis():
        import pickle as pk
        try:
            with open('users.bin', 'rb') as f:
                users = pk.load(f)
        except:
            with open('users.bin', 'wb') as f:
                pk.dump([], f)
        with open('users.bin', 'ab') as f:
            pk.dump({username:user_password}, f)
        root1.destroy()
    label4  = Label(root1, text="", fg = "white", bg = "black")
    label4.pack()    
    button2 = Button(root1, text="confirm", command=dis, padx=5, pady=5, bg="green" , fg = "white")    
    button2.pack()