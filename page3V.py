import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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