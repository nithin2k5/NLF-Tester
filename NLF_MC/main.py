import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as mc

class SettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings")
        self.root.geometry("800x500")
        self.create_widgets()
        self.connect_db()
        
    def connect_db(self):
        try:
            self.conn = mc.connect(host="127.0.0.1", user="root", password="#Nk446420", database="dataconsole")
            self.cursor = self.conn.cursor()
        except mc.Error as err:
            messagebox.showerror("Database error", f"Error connecting to the database: {err}")
     
    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def load_data(self):
        for row in self.table.get_children():
            self.table.delete(row)
        try:
            self.cursor.execute("SELECT * FROM settings") 
            rows = self.cursor.fetchall()
            for row in rows:
                self.table.insert("", "end", values=row)
        except mc.Error as err:
            messagebox.showerror("Database error", f"Error loading data: {err}")

    def save_data(self):
        data = {key: entry.get() for key, entry in self.entries.items()}
        try:
            self.cursor.execute("""INSERT INTO settings (part_number, part_name, customer_name, vendor_code, model_year, sequence_order, load_selection)
                                VALUES (%(part_number)s, %(part_name)s, %(customer_name)s, %(vendor_code)s, %(model_year)s, %(sequence_order)s, %(load_selection)s)""", data)
            self.conn.commit()
            self.load_data()
            self.clear_entries()
        except mc.Error as err:
            messagebox.showerror("Database error", f"Error saving data: {err}")

    def delete_data(self):
        try:
            select_item = self.table.selection()[0]
            item_id = self.table.item(select_item)['values'][0]
            self.cursor.execute("DELETE FROM settings WHERE id = %s", (item_id,))
            self.conn.commit()
            self.load_data()
        except mc.Error as err:
            messagebox.showerror("Database error", f"Error deleting data: {err}")
        except IndexError:
            messagebox.showwarning("Selection Error", "No item selected for deletion")

    def retrieve_from_tree(self):
        try:
            selected_item = self.table.selection()[0]
            values = self.table.item(selected_item)['values']
            for key, entry in zip(self.entries.keys(), values[1:]):
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, entry)

        except IndexError:
                messagebox.showwarning("Selection Error", "No item selected for retrieval")          

    def update_data(self):
        try:
            selected_item = self.table.selection()[0]
            item_id = self.table.item(selected_item)['values'][0]
            data = {key: entry.get() for key, entry in self.entries.items()}
            data['id'] = item_id
            self.cursor.execute("""UPDATE settings SET part_number = %(part_number)s, part_name = %(part_name)s,
                                customer_name = %(customer_name)s, vendor_code = %(vendor_code)s, model_year = %(model_year)s,
                                sequence_order = %(sequence_order)s, load_selection = %(load_selection)s WHERE id = %(id)s""", data)
            self.conn.commit()
            self.load_data()
            self.clear_entries()
        except mc.Error as err:
            messagebox.showerror("Database error", f"Error updating data: {err}")
        except IndexError:
            messagebox.showwarning("Selection Error", "No item selected for update")

    def create_widgets(self):
        header_frame = tk.Frame(self.root)
        header_frame.pack(fill='x')
        header_label = tk.Label(header_frame, text="SETTINGS", bg="blue", fg="white", font=("Helvetica", 16))
        header_label.pack(fill='x')

        left_frame = tk.Frame(self.root)
        left_frame.pack(side='left', padx=10, pady=5, anchor='n')

        labels = ['Part Number:', 'Part Name:', 'Customer Name:', 'Vendor Code:',
                  'Model Year:', 'Sequence Order:', 'Load Selection:']
        self.entries = {}
        for i, label_text in enumerate(labels):
            label = ttk.Label(left_frame, text=label_text)
            label.grid(column=0, row=i, sticky='w', padx=5, pady=2)
            entry_var = tk.StringVar()
            entry_box = ttk.Entry(left_frame, width=30, textvariable=entry_var)
            entry_box.grid(column=1, row=i, padx=5, pady=2)
            self.entries[label_text[:-1].replace(' ', '_').lower()] = entry_box

        center_frame = tk.Frame(self.root)
        center_frame.pack(side='left', padx=10, pady=5, expand=True, fill='both')

        self.table = ttk.Treeview(center_frame, columns=('#', 'Part No.', 'Part Name', 'Customer Name', 'Vendor Code', 'Model Year', 'Sequence Order', 'Load Selection'), show="headings", height=10)
        self.table.heading('#', text='#')
        self.table.heading('Part No.', text='Part No.')
        self.table.heading('Part Name', text='Part Name')
        self.table.heading('Customer Name', text='Customer Name')
        self.table.heading('Vendor Code', text='Vendor Code')
        self.table.heading('Model Year', text='Model Year')
        self.table.heading('Sequence Order', text='Sequence Order')
        self.table.heading('Load Selection', text='Load Selection')
        
        self.table.column('#', width=30)
        self.table.column('Part No.', width=100)
        self.table.column('Part Name', width=100)
        self.table.column('Customer Name', width=100)
        self.table.column('Vendor Code', width=100)
        self.table.column('Model Year', width=100)
        self.table.column('Sequence Order', width=100)
        self.table.column('Load Selection', width=100)

        self.table.pack(expand=True, fill='both')

        right_frame = tk.Frame(self.root)
        right_frame.pack(side='right', padx=10, pady=5, anchor='n')

        buttons = [('CREATE', self.save_data), ('RETRIEVE', self.load_data), ('UPDATE', self.update_data), ('DELETE', self.delete_data), ('CLEAR', self.clear_entries),  ('FILL FROM TREE', self.retrieve_from_tree)]
        for i, (button_text, command) in enumerate(buttons):
            button = ttk.Button(right_frame, text=button_text, command=command)
            button.grid(column=0, row=i, padx=5, pady=2)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(1, weight=1)

        


if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsApp(root)
    root.mainloop()
