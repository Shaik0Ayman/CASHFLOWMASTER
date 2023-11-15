import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
window = tk.Tk()
window.title('portfolio graph')
fig = Figure(figsize=(5, 4), dpi=100)
labels = ["Assets", "Expenditure", "Savings"]
A = 39
E = 20
S = 10
sizes = [A, E, S]
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()
window.mainloop()