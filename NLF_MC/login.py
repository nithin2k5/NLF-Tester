import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

def login():
    emp_number = emp_number_var.get()
    password = password_var.get()

    try:
        connection = mysql.connector.connect(
            host = '127.0.0.1',
            database = 'Employees',
            user = 'root',
            password = '#Nk446420'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("Select * from employees WHERE emp_number = %s AND password = %s", (emp_number, password))
            record = cursor.fetchone()


            if record:
                messagebox.showinfo("Login success", "Login successful")
            else:
                messagebox.showerror("Login Failed", "Invalid employyee Number or Password")    

    except Error as e:
        messagebox.showerror("Error", f"Error while connectiong to mysql: {str(e)}")

    finally:
        if connection.is_connection():
            cursor.close()
            connection.close()

    if emp_number == "123" and password == "password":
        messagebox.showinfo("Login success", "Login successful")
    else:
        messagebox.showerror("Login failed", "Invalid employee Number or Password")


def cancel():
    root.destroy()   
    
root = tk.Tk()
root.title("Login1")
root.geometry("400x400")


emp_number_label = tk.Label(root, text="EMPLOYEE NUMBER :", font=("Arial",12))
emp_number_label.pack(pady=10)

emp_number_var = tk.StringVar()
emp_number_combo = ttk.Combobox(root, textvariable=emp_number_var)
emp_number_combo['value'] = ('123', '456', '789')
emp_number_combo.pack(pady=5)

password_label = tk.Label(root, text="PASSWORD :", font=("Arial", 12))
password_label.pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, show="*")
password_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

enter_button = tk.Button(button_frame, text="Enter", bg="green", fg="white", command=login)
enter_button.grid(row=0, column=0, padx=10)

cancel_button = tk.Button(button_frame, text="CANCEL", bg="red", fg="white", command=cancel)
cancel_button.grid(row=0, column=1, padx=10)


root.mainloop()
