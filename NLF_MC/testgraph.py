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
product_info_frame.place(x=50,y=50,width=320,height=200)


scan_codes_frame = ttk.Frame(root,relief="solid",borderwidth=1)
scan_codes_frame.place(x=380,y=50,width=320,height=200)

production_count_frame = ttk.Frame(root,relief="solid",borderwidth=1)
production_count_frame.place(x=710, y=50,width=450,height=200)

function_frame = ttk.Frame(root, relief="solid", borderwidth=1)
function_frame.place(x=1170, y=50, width=320, height=200)


fields = ["Customer","Model","Part no", "Part Name", "ALC", "#OF CHLS"]
for i, field in enumerate(fields):
    ttk.Label(product_info_frame,text=field).grid(row = i, column = 0, padx = 5, pady = 5, sticky="w")
    ttk.Entry(product_info_frame).grid(row = i, column = 1, padx = 5, pady = 5)


scan_fields = ["Master cable", "Master Jig", "Employee Code"]
for i, field in enumerate(scan_fields):
    ttk.Label(scan_codes_frame, text=field).grid(row = i, column=0, padx = 5, pady = 5, sticky="w")
    ttk.Entry(scan_codes_frame).grid(row = i, column = 1, padx = 5, pady = 5)


production_fields_one = ["Total", "PPM", "UPH"]
for i, field in enumerate(production_fields_one):
    ttk.Label(production_count_frame, text = field).grid(row = i, column = 0, padx = 5, pady = 5,sticky="w")
    ttk.Entry(production_count_frame, text = field).grid(row = i, column = 1, padx = 5, pady = 5)

production_fields_two = ["PASS", "NG", "Test (sec)", "V_code"] 
for i, field in enumerate(production_fields_two):
    ttk.Label(production_count_frame, text = field).grid(row = i, column = 3, padx = 5, pady = 5, sticky="w")
    ttk.Entry(production_count_frame, text = field).grid(row = i, column = 4, padx = 5, pady = 5)

buttons_one = ["ADMIN", "REPORT","LABEL PRINT"]
for i, field in enumerate(buttons_one):
    ttk.Button(function_frame, text=field).grid(row=i, column=0, padx =5, pady=5) 

buttons_two = ["SETTINGS", "NEW PART_NO", "COMPORT"] 
for i, fields in enumerate(buttons_two):
    ttk.Button(function_frame,text=field).grid(row=i, column=2, padx=5, pady=5)


main_frame = ttk.Frame(root)
main_frame.place(x = 10, y=270, width= 1800, height=500)

select_cable_frame = ttk.Frame(main_frame, relief="solid", borderwidth=1)
select_cable_frame.place(x=47, y=0, width=700,height=500)

shift_cable_frame = ttk.Frame(main_frame,relief="solid",borderwidth=1)
shift_cable_frame.place(x=760,y=0,width=700,height=500)

test_condition_label = tk.Label(select_cable_frame, text="TEST CONDITION", font=("arial",10))
test_condition_label.place(x=0, y = 0, width=350, height=50)

test_result_label = tk.Label(select_cable_frame, text="TEST RESULT", font=("arial",10))
test_result_label.place(x=350, y = 0, width=350, height=50)

shift_test_condition_label = tk.Label(shift_cable_frame, text="TEST CONDITION", font=("arial",10))
shift_test_condition_label.place(x=0, y = 0, width=350, height=50)

shift_test_result_label = tk.Label(shift_cable_frame, text="TEST RESULT", font=("arial",10))
shift_test_result_label.place(x=350, y = 0, width=350, height=50)


columns = ("Test Conditon", "Test Result")
tree = ttk.Treeview(select_cable_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col,text=col)
    tree.column(col, width=100)

tree.place(x=0,y=30, width=350, height=200)

shift_tree = ttk.Treeview(shift_cable_frame, columns=columns, show="headings")
for col in columns:
    shift_tree.heading(col,text=col)
    shift_tree.column(col, width=100)

shift_tree.place(x=0, y=30, width=350, height=200)

columns = ("Test Conditon", "Test Result")
tree = ttk.Treeview(select_cable_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col,text=col)
    tree.column(col, width=100)

tree.place(x=0,y=30, width=350, height=200)

shift_tree = ttk.Treeview(shift_cable_frame, columns=columns, show="headings")
for col in columns:
    shift_tree.heading(col,text=col)
    shift_tree.column(col, width=100)

shift_tree.place(x=0, y=30, width=350, height=200)


footer_frame = ttk.Frame(root, relief="solid", borderwidth=1)
footer_frame.place(x=50,y=600, width=1300, height=40)

footer_fields = ["LOAD", "KGF", "STROKE", "MM", "SPEED", "MM/SEC"]
for i, field in enumerate(footer_fields):
    ttk.Label(footer_frame, text=field).grid(row=0, column=i*2,padx=5,pady=5)
    ttk.Entry(footer_frame).grid(row=0, column=i*2+1, padx=5, pady=5)

root.mainloop()