import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]

# Function to create the line graph
def create_line_graph():
    # Create a new figure
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    
    # Create the line graph
    ax.plot(x_values, y_values, marker='o', linestyle='-', color='blue')
    ax.set_title('Sample Line Graph')
    ax.set_xlabel('X Values')
    ax.set_ylabel('Y Values')
    
    # Add the figure to the Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the main window
root = tk.Tk()
root.title("Statistic Line Graph")
root.geometry("700x500")

# Frame for the chart
chart_frame = tk.Frame(root)
chart_frame.pack(pady=20)

# Button to generate the chart
chart_button = tk.Button(root, text="Generate Line Graph", command=create_line_graph)
chart_button.pack(pady=10)

# Run the application
root.mainloop()
