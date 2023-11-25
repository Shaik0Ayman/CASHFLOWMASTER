import mysql.connector as m
from tkinter import *
from tkinter import messagebox

top1 = Tk()



def entry():
    top1.geometry("500x500")
    monthly_salary_label = Label(top1, text="Monthly Salary:")
    monthly_salary_label.pack()
    monthly_salary_entry = Entry(top1, width=30)
    monthly_salary_entry.pack()
    avg_expenditure_label = Label(top1, text="Average Expenditure:")
    avg_expenditure_label.pack()s
    avg_expenditure_entry = Entry(top1, width=30)
    avg_expenditure_entry.pack()  
    def assets():
        i = 1
        asset = Label(top1, text="ENTER THE ASSET : ")
        asset.pack()
        asset_name_label = Label(top1, text="Asset Name:")
        asset_name_label.pack()
        asset_name_entry = Entry(top1, width=30)
        asset_name_entry.pack()
        asset_value_label = Label(top1, text="Asset Value:")
        asset_value_label.pack()
        asset_value_entry = Entry(top1, width=30)
        asset_value_entry.pack()
        def next():
            top = Toplevel()
            top.geometry("200x200")
            asset = Label(top, text="ENTER THE ASSET : ")
            asset.pack()
            asset_name_label = Label(top, text="Asset Name:")
            asset_name_label.pack()
            asset_name_entry = Entry(top, width=30)
            asset_name_entry.pack()
            asset_value_label = Label(top, text="Asset Value:")
            asset_value_label.pack()
            asset_value_entry = Entry(top, width=30)
            asset_value_entry.pack()
            def done():
                asset = asset_name_entry.get()
                asset_value = asset_value_entry.get() 
                top.destroy()
                return asset,asset_value
            button2 = Button(top, text="DONE ! ", padx=10, pady=10, command=done  )    
            button2.pack()
        button1 = Button(top1, text="NEXT", command=next, padx=10, pady=10,  )
        button1.pack()
        
    button1 = Button(top1, text="ENTER ASSETS", command=assets, padx=10, pady=10,  )
    button1.pack()    
   
