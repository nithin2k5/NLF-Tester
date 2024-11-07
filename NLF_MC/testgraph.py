import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_product_info_frame(parent):
    frame = ttk.Frame(parent, relief="solid", borderwidth=1)
    frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    fields = ["Customer", "Model", "Part no", "Part Name", "ALC", "#OF CHLS"]
    for i, field in enumerate(fields):
        ttk.Label(frame, text=field).grid(row=i, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(frame).grid(row=i, column=1, padx=5, pady=5)

    return frame

def create_scan_codes_frame(parent):
    frame = ttk.Frame(parent, relief="solid", borderwidth=1)
    frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    scan_fields = ["Master cable", "Master Jig", "Employee Code"]
    for i, field in enumerate(scan_fields):
        ttk.Label(frame, text=field).grid(row=i, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(frame).grid(row=i, column=1, padx=5, pady=5)

    return frame

def create_production_count_frame(parent):
    frame = ttk.Frame(parent, relief="solid", borderwidth=1)
    frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

    production_fields_one = ["Total", "PPM", "UPH"]
    for i, field in enumerate(production_fields_one):
        ttk.Label(frame, text=field).grid(row=i, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(frame).grid(row=i, column=1, padx=5, pady=5)

    production_fields_two = ["PASS", "NG", "Test (sec)", "V_code"] 
    for i, field in enumerate(production_fields_two):
        ttk.Label(frame, text=field).grid(row=i, column=3, padx=5, pady=5, sticky="w")
        ttk.Entry(frame).grid(row=i, column=4, padx=5, pady=5)

    return frame

def create_function_frame(parent):
    frame = ttk.Frame(parent, relief="solid", borderwidth=1)
    frame.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

    buttons_one = ["ADMIN", "REPORT", "LABEL PRINT"]
    for i, field in enumerate(buttons_one):
        ttk.Button(frame, text=field).grid(row=i, column=0, padx=5, pady=5)

    buttons_two = ["SETTINGS", "NEW PART_NO", "COMPORT"] 
    for i, field in enumerate(buttons_two):
        ttk.Button(frame, text=field).grid(row=i, column=2, padx=5, pady=5)

    return frame

def create_main_frame(parent):
    frame = ttk.Frame(parent)
    frame.grid(row=1, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

    select_cable_frame = ttk.Frame(frame, relief="solid", borderwidth=1)
    select_cable_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    shift_cable_frame = ttk.Frame(frame, relief="solid", borderwidth=1)
    shift_cable_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    create_test_condition_labels(select_cable_frame, shift_cable_frame)
    create_treeview(select_cable_frame, shift_cable_frame)
    create_charts(select_cable_frame, shift_cable_frame)

    return frame

def create_test_condition_labels(select_frame, shift_frame):

    ttk.Label(select_frame, text="TEST CONDITION", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    ttk.Label(select_frame, text="TEST RESULT", font=("Arial", 10)).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

  
    ttk.Label(shift_frame, text="TEST CONDITION", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    ttk.Label(shift_frame, text="TEST RESULT", font=("Arial", 10)).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

def create_treeview(select_frame, shift_frame):
    columns = ("Test Condition", "Test Result")
    
    
    tree = ttk.Treeview(select_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    
    shift_tree = ttk.Treeview(shift_frame, columns=columns, show="headings")
    for col in columns:
        shift_tree.heading(col, text=col)
        shift_tree.column(col, width=100)
    shift_tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

def create_charts(select_frame, shift_frame):
    
    fig = Figure(figsize=(6, 2), dpi=100)
    plot = fig.add_subplot(1, 1, 1)


    x = [1, 2, 3]
    y = [1, 4, 8]
    plot.plot(x, y, marker='D')  

    plot.set_xlim(0.8, 3.2)
    plot.set_ylim(0, 10)
    plot.legend(["Series1"], loc="best")

 
    canvas_select = FigureCanvasTkAgg(fig, master=select_frame)
    canvas_select.draw()
    canvas_select.get_tk_widget().grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")


    canvas_shift = FigureCanvasTkAgg(fig, master=shift_frame)
    canvas_shift.draw()
    canvas_shift.get_tk_widget().grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

def create_footer_frame(parent):
    frame = ttk.Frame(parent, relief="solid", borderwidth=1)
    frame.grid(row=2, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

    footer_fields = ["LOAD", "KGF", "STROKE", "MM", "SPEED", "MM/SEC"]
    for i, field in enumerate(footer_fields):
        ttk.Label(frame, text=field).grid(row=0, column=i*2, padx=15, pady=10)
        ttk.Entry(frame).grid(row=0, column=i*2+1, padx=15, pady=10)

    return frame

def setup_main_window():
    root = tk.Tk()
    root.title("NLF TESTER")
    root.geometry("1920x1080")

    title_label = tk.Label(root, text="NLF TESTER", font=("Arial", 16), bg="lightblue", relief="solid")
    title_label.grid(row=0, column=0, columnspan=4, padx=20, pady=5, sticky="nsew")

    root.grid_rowconfigure(1, weight=1)  
    root.grid_columnconfigure(0, weight=1)  

   
    create_product_info_frame(root)
    create_scan_codes_frame(root)
    create_production_count_frame(root)
    create_function_frame(root)
    create_main_frame(root)
    create_footer_frame(root)

    return root

if __name__ == "__main__":
    root = setup_main_window()
    root.mainloop()
