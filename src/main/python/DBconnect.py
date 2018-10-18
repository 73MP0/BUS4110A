import sqlite3

conn = sqlite3.connect("OS_Employee.db")

with conn:
    cur = conn.cursor()
try:
    cur.execute("SELECT * FROM ")
    results = cur.fetchall()
    rowcounter = 0
    print(results)
except sqlite3.Error as e:
    print(e)
