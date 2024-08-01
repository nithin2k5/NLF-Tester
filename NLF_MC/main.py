import tkinter as tk
from tkinter import ttk
import messagebox
import mysql.connector as mc


class SettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings")
        self.root.geometry("800x500")  # Adjusted window size for better fit
        self.create_widgets()

    def connect_db(self):
        try:
            self.conn = mc.connect(host = "", user= "", password = "", database="")
            self.cursor = self.conn.cursor()
        except mc.Error as err:
            messagebox.showerror("Database error", "Error with connecting database:{err}")

    def create_table(self):
        self.execute.cursor("""CREATE TABLE IF NOT EXISTS employee (id INT AUTO_INCREMENT PRIMARY KEY, 
                            part_number VARCHAR(15),
                            part_name VARCHAR(15),
                            customer_name VARCHAR(15),
                            vendor_code VARCHAR(8),
                            model_year VARCHAR(8),
                            sequence_order VARCHAR(8),
                            load_selection VARCHAR(10))""")
        
        self.conn.commit()

    def button_action(self, action):
         if action == "NEW":
             self.clear_entries()
         elif action == "RESET":
             self.reset_data()
         elif action == "DELETE":
            self.delete_data()
         elif action == "UPDATE":  
            self.update_data()
         elif action == "SAVE":
             self.save_data()   


    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def load_data(self):   
        for row in self.table.get_children():
            self.table.delete(row)
        self.cursor.execute("SELECT * from employees") 
        rows = self.cursor.fetchall()
        for row in rows:
            self.table.insert("", "end", values=row)   

    def save_data(self):
        data = {key: entry.get() for key, entry in self.entries.items()}
        self.cursor.execute("""INSERT INTO employee (part_number, part_name, customer_name, vendor_code, model_year, sequence_order, load_selection)
                            VALUES (%(part_number)s, %(part_name)s,%(customer_name)s, %(vendor_code)s,%(model_year)s, %(sequence_order)s, %(load_selection)s)""", data)
        self.conn.commit()
        self.load_data()
        self.clear_entries()
            

    def delete_data(self):
        select_item = self.table.selection()[0]
        item_id = self.table.item(select_item)['values'][0]
        self.cursor.execute("DELETE * from employee WHERE id = %s", item_id)
        self.conn.commit()
        self.load_data()

    def update_data(self):
        selected_item = self.table.selection()[0]
        item_id = self.table.item(selected_item)['values'][0]
        data = {key: entry.get() for key, entry in self.entries.items()}
        data['id'] = item_id
        self.cursor.execute("""UPDATE employee SET part_number = %(part_number)s,part_name = %(part_name)s,
                            customer_name = %(customer_name)s,vedor_code = %(vendor_code)s,model_year = %(model_year)s,sequence_order = %(sequence_order)s,load_selection = %(load_selection)s WHERE id= %(id)s""")
        self.conn.commit()
        self.load_data()
        self.clear_entries()
        

    def create_widgets(self):
        
        header_frame = tk.Frame(self.root)
        header_frame.pack(fill='x')
        header_label = tk.Label(header_frame, text="SETTINGS", bg="blue", fg="white", font=("Helvetica", 16))
        header_label.pack(fill='x')

       
        left_frame = tk.Frame(self.root)
        left_frame.pack(side='left', padx=10, pady=5, anchor='n')

        labels = ['Part Number:', 'Part Name:', 'Customer Name:', 'Vendor Code:',
                  'Model Year:', 'Sequence Order:', 'Load Selection:']
        for i, label_text in enumerate(labels):
            label = ttk.Label(left_frame, text=label_text)
            label.grid(column=0, row=i, sticky='w', padx=5, pady=2)
            entry_var = tk.StringVar()
            entry_box = ttk.Entry(left_frame, width=30, textvariable=entry_var)
            entry_box.grid(column=1, row=i, padx=5, pady=2)

       
        center_frame = tk.Frame(self.root)
        center_frame.pack(side='left', padx=10, pady=5, expand=True, fill='both')

        #table = ttk.Treeview(center_frame, columns=('#', 'Part No.', 'Part Name'), show="headings")
        table = self.table = ttk.Treeview(center_frame, columns=('#', 'Part No.', 'Part Name', 'Customer Name', 'Vendor Code', 'Model Year', 'Sequence Order', 'Load Selection'), show="headings", height=10)
        self.table.heading('#', text='#')
        self.table.heading('Part No.', text='Part No.')
        self.table.heading('Part Name', text='Part Name')
        self.table.heading('Customer Name', text='Customer Name')
        self.table.heading('Vendor Code', text='Vendor Code')
        self.table.heading('Model Year', text='Model Year')
        self.table.heading('Sequence Order', text='Sequence Order')
        self.table.heading('Load Selection', text='Load Selection')
        
        # Set specific column widths
        self.table.column('#', width=30)
        self.table.column('Part No.', width=100)
        self.table.column('Part Name', width=100)
        self.table.column('Customer Name', width=100)
        self.table.column('Vendor Code', width=100)
        self.table.column('Model Year', width=100)
        self.table.column('Sequence Order', width=100)
        self.table.column('Load Selection', width=100)

        table.pack(expand=True, fill='both')

        # Right Frame for Buttons
        right_frame = tk.Frame(self.root)
        right_frame.pack(side='right', padx=10, pady=5, anchor='n')

        buttons = ['NEW', 'RETRIEVE', 'DELETE', 'SAVE', 'UPDATE', 'CLEAR']
        for i, button_text in enumerate(buttons):
            button = ttk.Button(right_frame, text=button_text)
            button.grid(column=0, row=i, padx=5, pady=2)

        # Make frames and table responsive
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(1, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsApp(root)
    root.mainloop()
