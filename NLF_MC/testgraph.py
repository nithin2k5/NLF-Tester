import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("NLF TESTER")
root.geometry("1920x1080")

title_label = tk.Label(root, text="NLF TESTER", font=("Arial",16),bg ="lightblue", relief="solid")
title_label.pack(fill="x")

product_info_frame = ttk.Frame(root,relief="solid", borderwidth=1)
product_info_frame.place(x=10,y=50,width=320,height=200)


scan_codes_frame = ttk.Frame(root,relief="solid",borderwidth=1)
scan_codes_frame.place(x=340,y=50,width=320,height=200)

production_count_frame = ttk.Frame(root,relief="solid",borderwidth=1)
production_count_frame.place(x=650, y=50,width=450,height=200)

function_frame = ttk.Frame(root, relief="solid", borderwidth=1)
function_frame.place(x=1150, y=50, width=320, height=200)


fields = ["Customer","Model","Part no", "Part Name", "ALC", "#OF CHLS"]
for i, field in enumerate(fields):
    ttk.Label(product_info_frame,text=field).grid(row = i, column = 0, padx = 5, pady = 5, sticky="w")
    ttk.Entry(product_info_frame).grid(row = i, column = 1, padx = 5, pady = 5)


scan_fields = ["Master cable", "Master Jig", "Employee Code"]
for i, field in enumerate(scan_fields):
    ttk.Label(scan_codes_frame, text=field).grid(row = i, column=0, padx = 7, pady = 5)
    ttk.Entry(scan_codes_frame).grid(row = i, column = 1, padx = 5, pady = 5)


production_fields_one = ["Total", "PPM", "UPH"]
for i, field in enumerate(production_fields_one):
    ttk.Label(production_count_frame, text = field).grid(row = i, column = 0, padx = 5, pady = 5)
    ttk.Entry(production_count_frame, text = field).grid(row = i, column = 1, padx = 5, pady = 5)

production_fields_two = ["PASS", "NG", "Test (sec)", "V_code"] 
for i, field in enumerate(production_fields_two):
    ttk.Label(production_count_frame, text = field).grid(row = i, column = 3, padx = 5, pady = 5)
    ttk.Entry(production_count_frame, text = field).grid(row = i, column = 4, padx = 5, pady = 5)
     
root.mainloop()