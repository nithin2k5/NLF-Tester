import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class NLFTesterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("NLF Tester")
        self.createWidgets()

        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#Nk446420",
            database="dataconsole"
        )

        self.cursor = self.db.cursor()

        self.createWidgets()
        self.load_data()

    def add_employee(self):
        name = self.full_name_entry.get()
        number = self.employee_number_entry.get()
        password = self.password_entry.get()
        designation = self.designation_entry.get()
        department = self.department_entry.get()

        if name and number and password and designation and department:
            try:
                self.cursor.execute(
    "INSERT INTO employees (name, number, password, designation, department) VALUES (%s, %s, %s, %s, %s)",
    (name, number, password, designation, department)
)
              
                self.db.commit()
                self.load_data()
                self.clear_entries()
                messagebox.showinfo("Success", "data added successfully..!")
            except mysql.connector.Error as err:
                messagebox.showerror("Error",f"Failed to add employee: {err}")

        else:
            messagebox.showwarning("Input error", "Please fill in all fields") 

    def edit_employee(self):
        selected_item = self.tree.selection()
        if selected_item:
            employee_id = self.tree.item(selected_item)['Values'][0]
            name = self.full_name_entry.get()
            number = self.employee_number_entry.get()
            designation = self.designation_entry.get()
            department = self.department_entry.get()

            if name and number and designation and department:
                try:
                    self.cursor.execute(
                        "UPDATE employee SET name=%s, number=%s,designation=%s, department=%s WHERE id=%s", (name, number, designation,department,employee_id)
                    ) 
                    self.db.commit()
                    self.load_data()
                    self.clear_entries()

                    messagebox.showinfo("Success", "Employee updated successfully!")

                except mysql.connector.Error as err:
                    messagebox.showerror("ERROR", f"Failed to update employee: {err}")

            else:
                messagebox.showwarning("Input error", "Please fill in all fields")

        else:
            messagebox.showwarning("Selection error","Please select an employee to edit.")

    def delete_employee(self):
        selected_item = self.tree.selection()
        if selected_item:
            employee_id = self.tree.item(selected_item)['values'][0]
            try:
                self.cursor.execute("Delete from employees where id=%s", (employee_id,))
                self.db.commit()
                self.load_data()
                self.clear_entries()
                messagebox.showinfo("Success", "Employee deleted successfully!")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"failed to delete employee: {err}")

        else:
            messagebox.showwarning("selection error", "please select an employee to delete.")    


    def load_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        self.cursor.execute("Select id,name,password,number,designation,department from employees")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)


    def on_tree_select(self, event):
        selected_items = self.tree.selection[0]
        values = self.tree.item(selected_items, "values")

        self.full_name_entry.delete(0, tk.END)
        self.full_name_entry.insert(0, values[1])
        self.employee_number_entry.delete(0, tk.END)
        self.employee_number_entry.insert(0, values[2])
        self.designation_entry.delete(0, tk.END)
        self.designation_entry.insert(0, values[3])
        self.department_entry.delete(0, tk.END)
        self.department_entry.insert(0, values[4])


    def clear_entries(self):
        self.full_name_entry.delete(0, tk.END)
        self.employee_number_entry.delete(0, tk.END)
        self.password_entry.delete(0,tk.END)   
        self.designation_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)



    def createWidgets(self):
        
        tk.Label(self.root, text="INFAC INDIA", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="NLF TESTER", font=("Helvetica", 14)).grid(row=1, column=0, columnspan=2, pady=5)

        tk.Label(self.root, text="EMPLOYEE FULL NAME:", anchor="w").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.full_name_entry = tk.Entry(self.root, width=30)
        self.full_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.root, text="EMPLOYEE NUMBER:", anchor="w").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.employee_number_entry = tk.Entry(self.root, width=30)
        self.employee_number_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.root, text="PASSWORD:", anchor="w").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.password_entry = tk.Entry(self.root, show='*', width=30)
        self.password_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.root, text="DESIGNATION:", anchor="w").grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.designation_entry = tk.Entry(self.root, width=30)
        self.designation_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.root, text="DEPARTMENT:", anchor="w").grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.department_entry = tk.Entry(self.root, width=30)
        self.department_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(self.button_frame, text="ADD", command=self.add_employee).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="EDIT", command=self.edit_employee).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="DELETE", command=self.delete_employee).grid(row=0, column=2, padx=5)

        
        self.tree = ttk.Treeview(self.root, columns=("name", "number", "designation", "department"), show="headings")
        self.tree.heading("name", text="EMPLOYEE NAME")
        self.tree.heading("number", text="EMPLOYEE NUMBER")
        self.tree.heading("designation", text="DESIGNATION")
        self.tree.heading("department", text="DEPARTMENT")
        self.tree.grid(row=9, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

        
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(9, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = NLFTesterApp(root)
    root.mainloop()
