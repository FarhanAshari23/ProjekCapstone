import tkinter as tk
from tkinter import ttk
from tkinter_webcam import webcam
from random import choice

class App(tk.Tk):
    def __init__(self, title, size):
        #main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')

        #widgets
        self.detection = Detection(self)

        #function menu
        def historyIn(self):
            self.detection.pack_forget
            HistoryListIn(self)
            
        def detectionAPD(self):
            HistoryListIn(self).pack_forget
            self.detection

        #configure menu
        menu = tk.Menu(self)
        
        #sub menu
        apd_menu = tk.Menu(menu, tearoff=False)
        apd_menu.add_command(label="Pendeteksian APD", command=detectionAPD)
        apd_menu.add_command(label="Pendaftaran Karyawan", command=lambda:print("Tes masuk"))
        menu.add_cascade(label="Fitur-fitur", menu=apd_menu)

        #another sub menu
        history_menu = tk.Menu(menu, tearoff=False)
        history_menu.add_command(label="History Masuk", command=HistoryListIn)
        history_menu.add_command(label="History Keluar")
        menu.add_cascade(label="History Karyawan", menu=history_menu)

        #set the menu
        self.configure(menu=menu)

        #run
        self.mainloop()

class Detection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x =0, y=0, relheight=1, relwidth=1)
        self.create_widgets()
    
    def create_widgets(self):

        #create the widgets
        button_helm = tk.Button(self, text='Deteksi Helm',bg='green', font=('Times New Roman', 30))
        button_vest = tk.Button(self, text='Deteksi Rompi', bg='red', font=('Times New Roman', 30))
        button_idcard = tk.Button(self, text='Deteksi ID Card', bg='red', font=('Times New Roman', 30))
        frameCamera = tk.LabelFrame(self, text="Frame Camera Detection")
        video = webcam.Box(frameCamera)
        video.show_frames()

        #place the widgets
        frameCamera.pack(side='right')
        button_helm.pack(fill='both', expand=True)
        button_vest.pack(fill='both', expand=True)
        button_idcard.pack(fill='both', expand=True)
        
class HistoryListIn(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
    
    def createWidget(self):
        tableIn = ttk.Treeview(self, columns = ('Nama', 'ID', 'Jam Masuk'), show = 'headings')
        tableIn.heading('Nama', text='Nama')
        tableIn.heading('ID', text='ID')
        tableIn.heading('Jam Masuk', text='Jam Masuk')

        names = ["Rifky", "Farhan", "Didi"]
        ID = ["21120120130072", "21120120130074", "21120120130073"]
        jam_masuk = ['7:08 WIB', '7:12 WIB', '7:19 WIB']

        for i in range(70):
            first = choice(names)
            last = choice(ID)
            email = choice(jam_masuk)
            data = (first, last, email)
            tableIn.insert(parent='', index=0, values=data)


App('Pendeteksian APD', (1440,800))

