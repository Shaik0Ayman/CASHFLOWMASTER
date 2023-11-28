from tkinter import *
from tkinter import messagebox
from SQL_init import *

top = Tk()

def secwin():
    top.geometry("100x100")
    top.title("CASH FLOW MASTER")
    top.geometry("200x200")
    label1 = Label(top, text="CASH FLOW MASTER")
    label1.pack() 

    def first_time_user():

    def entry_():
        from page3E import entry
        entry()
        top.destroy()
    def view_():
        from page3V import view 
        view()
        top.destroy()

    button2 = Button(top, text="ENTER DATA", command=entry_, padx=10, pady=10,  )    
    button2.pack()

    button3 = Button(top, text="VIEW DATA", command=view_, padx=10, pady=10,  )    
    button3.pack()