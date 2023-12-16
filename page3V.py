import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector as m

db = m.connect(
    host="localhost",
    user="root",
    passwd="0786",
)
udb = "cashflowmaster"
cursor = db.cursor()
cursor.execute("USE {}".format(udb))
with open('temp.txt', 'r+') as f:
                username = f.read()
cursor.execute("SELECT SUM(expense_price) from expenses_{};".format(username));
assets = cursor.fetchone()
for i in assets:
    print (i)
window = tk.Tk()
window.title('portfolio graph')

fig = Figure(figsize=(5, 4), dpi=100)

labels = ["Assets", "Expenditure"]
A = 39
E = 20
sizes = [A, E]

# Define the colors for the sectors
colors = ['green', 'red']

ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90, colors=colors)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

window.mainloop()