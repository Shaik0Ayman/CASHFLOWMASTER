from tkinter import *
from tkinter import messagebox
top = Tk()
def secwin():
    top.geometry("250x200")
    top.title("CASH FLOW MASTER")
    top.geometry("400x400")
    
    # Create labels and entry widgets for Monthly salary, Average expenditure, Asset name, and Asset value
    label1 = Label(top, text="CASH FLOW MASTER")
    label1.pack() 
    def entry_():
        from entrypage import entry
        entry()

    button2 = Button(top, text="ENTER DATA", command=entry_, padx=10, pady=10,  )    
    button2.pack()

    '''global monthly_salary_entry, avg_expenditure_entry, asset_name_entry, asset_value_entry

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
'''