
from tkinter import *
from tkinter import messagebox
top1 = Tk()
def entry():
    top1.geometry("400x400")
    monthly_salary_label = Label(top1, text="Monthly Salary:")
    monthly_salary_label.pack()
    monthly_salary_entry = Entry(top1, width=30)
    monthly_salary_entry.pack()
    avg_expenditure_label = Label(top1, text="Average Expenditure:")
    avg_expenditure_label.pack()
    avg_expenditure_entry = Entry(top1, width=30)
    avg_expenditure_entry.pack()
    nass_label = Label(top1, text="ENTER THE NUMBER OF ASSETS YOU WANt TO ENTER")
    nass_label.pack()
    nass_entry = Entry(top1, width=30)
    nass_entry.pack()
    nass = int(nass_entry.get())
    for i in range(nass):
        asset = Label(top1, text="ENTER THE ASSET NUMBER : "+i)
        asset.pack()
        asset_entry = Entry(top1, width=100) 
        asset_entry.pack()



    button2 = Button(top1, text="ENTER ", command=entry, padx=10, pady=10,  )    
    button2.pack()
    asset_name_label = Label(top1, text="Asset Name:")
    asset_name_label.pack()
    asset_name_entry = Entry(top1, width=30)
    asset_name_entry.pack()
    asset_value_label = Label(top1, text="Asset Value:")
    asset_value_label.pack()
    asset_value_entry = Entry(top1, width=30)
    asset_value_entry.pack()
