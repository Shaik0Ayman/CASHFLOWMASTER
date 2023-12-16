import mysql.connector as m
from tkinter import *
from tkinter import messagebox
import csv

top1 = Tk()

def entry():
    top1.geometry("500x500")
    top1.title("ASSET ENTRY")
    top1.configure(bg="black")

    label1 = Label(top1, text="Monthly Salary:", fg="white", bg="black")
    label1.pack()

    monthly_salary_entry = Entry(top1, width=30, fg="white", bg="black")
    monthly_salary_entry.pack()

    label2 = Label(top1, text="Average Expenditure:", fg="white", bg="black")
    label2.pack()

    avg_expenditure_entry = Entry(top1, width=30, fg="white", bg="black")
    avg_expenditure_entry.pack()

    def assets():
        top = Toplevel()
        top.geometry("200x200")
        top.title("ASSET ENTRY")
        top.configure(bg="black")

        asset_label = Label(top, text="ENTER THE ASSET NO {} : ".format(1), fg="white", bg="black")
        asset_label.pack()

        asset_name_label = Label(top, text="Asset Name:", fg="white", bg="black")
        asset_name_label.pack()

        asset_name_entry = Entry(top, width=30, fg="white", bg="black")
        asset_name_entry.pack()

        asset_value_label = Label(top, text="Asset Value:", fg="white", bg="black")
        asset_value_label.pack()

        asset_value_entry = Entry(top, width=30, fg="white", bg="black")
        asset_value_entry.pack()

        def done():
            asset = asset_name_entry.get()
            asset_value = asset_value_entry.get()
            top.destroy()

            # Write the asset name and value to the assets.csv file
            with open('assets.csv', 'a+', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([asset, asset_value])

            # Create user tables
            with open('temp.txt', 'r+') as f:
                username = f.read()
                f.write("")
            import SQL_init
            SQL_init.insert_asset(username, asset, asset_value)

            # Display a confirmation message
            messagebox.showinfo("Success", "Asset added successfully")

            return asset, asset_value

        button2 = Button(top, text="DONE !", padx=10, pady=10, command=done, bg="green", fg="white")
        button2.pack()

    button1 = Button(top1, text="ENTER ASSETS", command=assets, padx=10, pady=10, bg="teal", fg="white")
    button1.pack()

    top1.mainloop()

entry()
