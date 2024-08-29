import mysql.connector as mc

try:
    conn = mc.connect(host="127.0.0.1", user="root", password="#Nk446420", database="dataconsole")
    print("Connection successful!")
except mc.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        conn.close()