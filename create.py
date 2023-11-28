from tkinter import *
from tkinter import messagebox
import csv
from SQL_init import *

root1 = Tk()

def win():
    root1.geometry("250x230")
    root1.title("NEW USER")
    root1.configure(bg="black")

    # Function to handle user registration
    def register_user():
        # Get the values entered by the user
        username = username_entry.get()
        user_password = password_entry.get()

        # Check if username or password is empty
        if not username or not user_password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        # Save the user to a CSV file and create user tables
        with open("users.csv", 'a+', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([username, user_password])

        # Display a confirmation message
        messagebox.showinfo("Success", "User registered successfully")

        # Clear the entry fields
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        root1.destroy()

    label1 = Label(root1, text="CASH FLOW MASTER", fg="white", bg="black")
    label1.pack()

    label2 = Label(root1, text="", fg="white", bg="black")
    label2.pack()

    label3 = Label(root1, text="enter username:", fg="white", bg="black")
    label3.pack()

    username_entry = Entry(root1, width=30, fg="white", bg="black")
    username_entry.pack()

    label4 = Label(root1, text="enter password:", fg="white", bg="black")
    label4.pack()

    password_entry = Entry(root1, width=30, fg="white", bg="black", show="*")
    password_entry.pack()

    label5 = Label(root1, text="", fg="white", bg="black")
    label5.pack()

    # Button to trigger the registration function
    button2 = Button(root1, text="confirm", command=register_user, padx=5, pady=5, bg="green", fg="white")
    button2.pack()

