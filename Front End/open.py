from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()



def secwin():
    root.wm_state("iconic")
    top = Toplevel()
    top.title("CASH FLOW MASTER")
    top.geometry("400x400")
    
    # Create labels and entry widgets for Monthly salary, Average expenditure, Asset name, and Asset value
    label1 = Label(top, text="CASH FLOW MASTER")
    label1.pack()

    global monthly_salary_entry, avg_expenditure_entry, asset_name_entry, asset_value_entry

    monthly_salary_label = Label(top, text="Monthly Salary:")
    monthly_salary_label.pack()
    monthly_salary_entry = Entry(top, width=30)
    monthly_salary_entry.pack()

    avg_expenditure_label = Label(top, text="Average Expenditure:")
    avg_expenditure_label.pack()
    avg_expenditure_entry = Entry(top, width=30)
    avg_expenditure_entry.pack()

    asset_name_label = Label(top, text="Asset Name:")
    asset_name_label.pack()
    asset_name_entry = Entry(top, width=30)
    asset_name_entry.pack()

    asset_value_label = Label(top, text="Asset Value:")
    asset_value_label.pack()
    asset_value_entry = Entry(top, width=30)
    asset_value_entry.pack()

def firstwin():
    root.geometry("250x200")
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