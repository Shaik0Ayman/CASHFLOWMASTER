from tkinter import *
from tkinter import messagebox
top = Tk()
def secwin():
    top.geometry("100x100")
    top.title("CASH FLOW MASTER")
    top.geometry("100x100")
    label1 = Label(top, text="CASH FLOW MASTER")
    label1.pack() 
    def entry_():
        from page3E import entry
        entry()
        top.destroy()
    button2 = Button(top, text="ENTER DATA", command=entry_, padx=10, pady=10,  )    
    button2.pack()
    def view_():
        from page3V import view 
        view()
    button3 = Button(top, text="VIEW DATA", command=view_, padx=10, pady=10,  )    
    button3.pack()