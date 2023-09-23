import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename="solar")
#window.geometry('300x400')
window.title('Testing')

window_width = 1440
window_height = 850
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width/2 - window_width/2)
top = int(display_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

my_style = ttk.Style()
my_style.configure('danger.TButton', font=("Helvetica", 48))

button = ttk.Button(window, text='Button test', style='danger.Tbutton').pack()

window.mainloop()