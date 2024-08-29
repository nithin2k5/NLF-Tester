import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample data
x = [1, 2, 3]
y = [1, 4, 8]

# Create a tkinter window
root = tk.Tk()
root.title("Line Graph using Tkinter")

# Create a matplotlib figure
fig = Figure(figsize=(5, 4), dpi=100)
plot = fig.add_subplot(1, 1, 1)

# Plot the data
plot.plot(x, y, marker='D')  # D is for diamond marker

# Set limits for x and y axes to match the example
plot.set_xlim(0.8, 3.2)
plot.set_ylim(0, 10)

# Add the legend
plot.legend(["Series1"], loc="best")

# Add the canvas to the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the tkinter main loop
root.mainloop()
