import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("DATA CONSOLE")
root.geometry("1500x700")


upper_frame = tk.Frame(root)
upper_frame.pack(fill='x')


part_number_label = tk.Label(upper_frame, text="PART NUMBER:")
part_number_label.pack(side='left', padx=(10, 2))
part_number_entry = tk.Entry(upper_frame)
part_number_entry.pack(side='left', padx=(0, 10))

start_date_label = tk.Label(upper_frame, text="START DATE:")
start_date_label.pack(side='left', padx=(10, 2))
start_date_entry = tk.Entry(upper_frame)
start_date_entry.pack(side='left', padx=(0, 10))

end_date_label = tk.Label(upper_frame, text="END DATE:")
end_date_label.pack(side='left', padx=(10, 2))
end_date_entry = tk.Entry(upper_frame)
end_date_entry.pack(side='left', padx=(0, 10))

result_label = tk.Label(upper_frame, text="RESULT:")
result_label.pack(side='left', padx=(10, 2))
result_entry = tk.Entry(upper_frame)
result_entry.pack(side='left', padx=(0, 10))


lower_frame = tk.Frame(root)
lower_frame.pack(fill='both', expand=True)


table = ttk.Treeview(lower_frame, columns=('#', 'DATE', 'TIME', 'VEHICLE MODEL', 'VIN NUMBER', 'RESULT'))
table.heading('#', text='#')
table.heading('DATE', text='DATE')
table.heading('TIME', text='TIME')
table.heading('VEHICLE MODEL', text='VEHICLE MODEL')
table.heading('VIN NUMBER', text='VIN NUMBER')
table.heading('RESULT', text='RESULT')
table.pack(fill='both', expand=True)

root.mainloop()
