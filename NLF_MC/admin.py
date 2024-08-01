import tkinter as tk
from tkinter import ttk

class NLFTesterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("NLF Tester")
        self.createWidgets()

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
        tk.Button(self.button_frame, text="ADD").grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="EDIT").grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="DELETE").grid(row=0, column=2, padx=5)

        
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
