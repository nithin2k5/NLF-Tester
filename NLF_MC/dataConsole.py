import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector
import pandas as pd

class DataConsoleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Console")

        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        title_label = ttk.Label(main_frame, text="DATA CONSOLE", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=10)

        ttk.Label(main_frame, text="PART NUMBER:").grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.part_number = ttk.Combobox(main_frame)
        self.part_number.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        ttk.Label(main_frame, text="START DATE:").grid(row=1, column=2, sticky=tk.E, padx=5, pady=5)
        self.start_date = DateEntry(main_frame, date_pattern='yyyy-mm-dd')
        self.start_date.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)

        ttk.Label(main_frame, text="END DATE:").grid(row=1, column=4, sticky=tk.E, padx=5, pady=5)
        self.end_date = DateEntry(main_frame, date_pattern='yyyy-mm-dd')
        self.end_date.grid(row=1, column=5, sticky=tk.W, padx=5, pady=5)

        ttk.Label(main_frame, text="RESULT:").grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
        self.result = ttk.Combobox(main_frame, values=["Pass", "Fail", "Pending", "In Progress"])
        self.result.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        self.result.current(0)

        ttk.Label(main_frame, text="PART STATUS:").grid(row=2, column=2, sticky=tk.E, padx=5, pady=5)
        self.part_status = ttk.Combobox(main_frame)
        self.part_status.grid(row=2, column=3, sticky=tk.W, padx=5, pady=5)

        search_button = ttk.Button(main_frame, text="Search", command=self.search)
        search_button.grid(row=2, column=4, padx=5, pady=5)

        export_button = ttk.Button(main_frame, text="ExportToExcel", command=self.export_to_excel)
        export_button.grid(row=2, column=5, padx=5, pady=5)

        columns = ("SNO", "partnumber", "date", "time", "result", "model", "customerID")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings")
        self.tree.grid(row=3, column=0, columnspan=6, pady=10, sticky=(tk.W, tk.E))

        for col in columns:
            self.tree.heading(col, text=col.upper().replace("_", " "))
            self.tree.column(col, width=100)

        for col in columns:
            self.tree.column(col, minwidth=100, width=100, stretch=tk.YES)

        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(3, weight=1)
        main_frame.columnconfigure(5, weight=1)
        main_frame.rowconfigure(3, weight=1)


        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="#Nk446420",  
            database="dataconsole"  
        )
        self.cursor = self.conn.cursor()


        self.populate_part_numbers()
        self.populate_customer_id()

    def populate_part_numbers(self):
  
        query = "SELECT DISTINCT partnumber FROM data"
        self.cursor.execute(query)
        part_numbers = [row[0] for row in self.cursor.fetchall()]


        self.part_number['values'] = part_numbers

    def populate_customer_id(self):

        query = "SELECT DISTINCT customerid FROM data"
        self.cursor.execute(query)
        part_statuses = [row[0] for row in self.cursor.fetchall()]


        self.part_status['values'] = part_statuses

    def search(self):
        part_number = self.part_number.get()
        start_date = self.start_date.get_date()
        end_date = self.end_date.get_date()
        result = self.result.get()
        part_status = self.part_status.get()

        query = """
        SELECT SNO, partnumber, date, time, result, model, customerID 
        FROM data 
        WHERE partnumber = %s AND date >= %s AND date <= %s AND result = %s AND status = %s
        """
        params = (part_number, start_date, end_date, result, part_status)

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()


        for item in self.tree.get_children():
            self.tree.delete(item)


        for row in rows:
            self.tree.insert("", "end", values=row)

        if not rows:
            messagebox.showinfo("No Results", "No data found for the selected criteria.")

    def export_to_excel(self):
        part_number = self.part_number.get()
        start_date = self.start_date.get_date()
        end_date = self.end_date.get_date()
        result = self.result.get()
        part_status = self.part_status.get()

        query = """
        SELECT SNO, partnumber, date, time, result, model, customerID 
        FROM data 
        WHERE partnumber = %s AND date >= %s AND date <= %s AND result = %s AND status = %s
        """
        params = (part_number, start_date, end_date, result, part_status)

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()

        if rows:
            df = pd.DataFrame(rows, columns=[desc[0] for desc in self.cursor.description])
            file_path = "data_console_export.xlsx"
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Export Successful", f"Data exported to {file_path}")
        else:
            messagebox.showinfo("No Results", "No data to export.")

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataConsoleApp(root)
    root.mainloop()
    