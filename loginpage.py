from tkinter import *
from tkinter import messagebox
import csv
root = Tk()

def firstwin():
    root.geometry("250x300")
    root.title("LOGIN PAGE")
    root.configure(bg="black")

    label1 = Label(root, text="CASH FLOW MASTER", fg="white", bg="black")
    label1.pack()

    label0 = Label(root, text="", fg="white", bg="black")
    label0.pack()

    def creat():
        from create import win 
        win()

    button2 = Button(root, text="NEW USER?", command=creat, padx=5, pady=5, bg="teal", fg="white")
    button2.pack()

    label0 = Label(root, text="", fg="white", bg="black")
    label0.pack()

    label3 = Label(root, text="enter username:", fg="white", bg="black")
    label3.pack()

    u = Entry(root, width=30, fg="white", bg="black")
    u.pack()

    label2 = Label(root, text="", fg="white", bg="black")
    label2.pack()

    label4 = Label(root, text="enter password:", fg="white", bg="black")
    label4.pack()

    p = Entry(root, width=30, fg="white", bg="black", show="*")
    p.pack()

    def verify():
         # Get the values from the entry widgets when the button is clicked
        username_input = u.get()
        user_password_input = p.get()

        found = False  # Flag to check if credentials are found

        with open('users.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                stored_username = row[0]
                stored_password = row[1]
                if username_input == stored_username and user_password_input == stored_password:
                    found = True
                    break

        if found:
            root.destroy()
            from page2 import secwin
            secwin()
        else:
            error_auth = messagebox.showwarning("ERROR", "Incorrect username or password")

    label5 = Label(root, text="", fg="white", bg="black")
    label5.pack()

    button1 = Button(root, text="submit", command=verify, padx=10, pady=10, bg="green", fg="white")
    button1.pack()

    label0 = Label(root, text="", fg="white", bg="black")
    label0.pack()

firstwin()
root.mainloop()
