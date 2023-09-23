import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
import sqlite3

window = ttk.Window(themename="solar")
#window.geometry('300x400')
window.title('Testing')
window.geometry('400x500')

#databases

#create a database
conn = sqlite3.connect('karyawan_pabrik.db')

#create cursor
c = conn.cursor()

#create table
c.execute("""CREATE TABLE employee (
          name text,
          id text,
          role text,
          username text,
          password text
        )""")

#commit changes
conn.commit()

#close connetion
conn.close()

window.mainloop()