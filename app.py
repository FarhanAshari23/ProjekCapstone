from tkinter import *
from tkinter_webcam import webcam
from tkinter import ttk
from random import choice

root = Tk()
root.geometry('300x400')
root.title("Pendeteksian APD Karyawan Pabrik")

def open():
    if entryUser.get() == 'farhan':
        root.destroy()
        window4_main = Tk()
        window4_main.geometry('750x500')
        window4_main.title("Pendaftaran Karyawan")

        myLabel = Label(window4_main, text='Silakan Pilih:', font=('Helvetica', 18))
        button_karyawan = Button(window4_main, text='Tambahkan Karyawan', pady=80, padx=300, font=('Helvetica', 12),command=tambahOperator)
        button_supervisi = Button(window4_main, text='Tambahkan Operator', pady=80, padx=300, font=('Helvetica', 12), command=tambahOperator)
    
        myLabel.grid(row=1, column=0, columnspan=2, sticky='w', ipadx=20)
        button_karyawan.grid(row=2, column=0, columnspan=2, pady=10, padx=20, ipady=20)
        button_supervisi.grid(row=3, column=0, columnspan=2, pady=10)

        window4_main.mainloop()

    global window2_main
    root.destroy()
    window2_main = Tk()
    window2_main.geometry('1440x960')
    window2_main.title("Pendeteksian APD Karyawan Pabrik")
    frame = LabelFrame(window2_main, text="Frame Camera Detection")
    video = webcam.Box(frame)
    video.show_frames()
    button_helm = Button(window2_main, text='Deteksi Helm', pady=80, padx=300, bg='red')
    button_vest = Button(window2_main, text='Deteksi Rompi', pady=80, padx=300, bg='green')
    button_idcard = Button(window2_main, text='Deteksi ID Card', pady=80, padx=300, bg='green')
    button_enter = Button(window2_main, text='Riwayat Karyawan Masuk', pady=60, padx=95, command=HistoryIn)
    button_quit = Button(window2_main, text='Riwayat Karyawan Keluar', pady=60, padx=95, command=HistoryOut)
    
    button_helm.grid(row=1, column=0, columnspan=2, pady=10, padx=20, ipady=20)
    button_vest.grid(row=2, column=0, columnspan=2, pady=10)
    button_idcard.grid(row=3, column=0, columnspan=2, pady=10)
    button_enter.grid(row=5, column=0)
    button_quit.grid(row=5, column=1)
    frame.grid(row=1, column=3, rowspan=5, padx=100)
    window2_main.mainloop()

def HistoryIn():
    window2_main.destroy
    window3_main = Tk()
    window3_main.geometry('800x800')
    window3_main.title("Riwayat Masuk Pabrik")
    table = ttk.Treeview(window3_main, columns = ('Nama', 'ID', 'Jam Masuk'), show = 'headings')
    table.heading('Nama', text='Nama')
    table.heading('ID', text='ID')
    table.heading('Jam Masuk', text='Jam Masuk')
    table.pack(fill='both', expand=True)

    names = ["Rifky", "Farhan", "Didi"]
    ID = ["21120120130072", "21120120130074", "21120120130073"]
    jam_masuk = ['7:08 WIB', '7:12 WIB', '7:19 WIB']

    for i in range(70):
        first = choice(names)
        last = choice(ID)
        email = choice(jam_masuk)
        data = (first, last, email)
        table.insert(parent='', index=0, values=data)
    window3_main.mainloop()

def HistoryOut():
    window2_main.destroy
    window3_main = Tk()
    window3_main.geometry('800x800')
    window3_main.title("Riwayat Keluar Pabrik")
    table = ttk.Treeview(window3_main, columns = ('Nama', 'ID', 'Jam Masuk'), show = 'headings')
    table.heading('Nama', text='Nama')
    table.heading('ID', text='ID')
    table.heading('Jam Masuk', text='Jam Masuk')
    table.pack(fill='both', expand=True)

    names = ["Rifky", "Farhan", "Didi"]
    ID = ["21120120130072", "21120120130074", "21120120130073"]
    jam_masuk = ['7:08 WIB', '7:12 WIB', '7:19 WIB']

    for i in range(70):
        first = choice(names)
        last = choice(ID)
        email = choice(jam_masuk)
        data = (first, last, email)
        table.insert(parent='', index=0, values=data)
    window3_main.mainloop()

def openHRD():
    global window4_main
    root.destroy()
    window4_main = Tk()
    window4_main.geometry('780x500')
    window4_main.title("Pendaftaran Karyawan")

    myLabel = Label(window4_main, text='Silakan Pilih:', font=('Helvetica', 18))
    button_karyawan = Button(window4_main, text='Tambahkan Karyawan', pady=80, padx=300, font=('Helvetica', 12),command=tambahOperator)
    button_supervisi = Button(window4_main, text='Tambahkan Operator', pady=80, padx=300, font=('Helvetica', 12), command=tambahOperator)
    
    myLabel.grid(row=1, column=0, columnspan=2, sticky='w', ipadx=20)
    button_karyawan.grid(row=2, column=0, columnspan=2, pady=10, padx=20, ipady=20)
    button_supervisi.grid(row=3, column=0, columnspan=2, pady=10)

    window4_main.mainloop()

def tambahOperator():
    window4_main.deletecommand
    window5_main = Tk()
    window5_main.geometry('300x400')
    window5_main.title("Pendeteksian APD Karyawan Pabrik")

    labelUser = Label(window5_main, text="Username")
    labelPassword = Label(window5_main, text="Password")
    entryUser = Entry(window5_main, width=30, borderwidth=5)
    entryPassword = Entry(window5_main, width=30, borderwidth=5)
    btnEnterSupervisi = Button(window5_main, text="Supervisi", command=open, padx=50, pady=10)
    window5_main.columnconfigure(0, weight=1)
    window5_main.columnconfigure(1, weight=1)
    window5_main.columnconfigure(2, weight=1)
    window5_main.rowconfigure(0, weight=1)
    window5_main.rowconfigure(1, weight=1)
    labelUser.grid(column=0, row=0)
    entryUser.grid(column=1, row=0, pady=5, )
    labelPassword.grid(column=0, row=1)
    entryPassword.grid(column=1, row=1, pady=5)
    btnEnterSupervisi.grid(column=0, row=2, pady=30)


labelUser = Label(root, text="Username")
labelPassword = Label(root, text="Password")
entryUser = Entry(root, width=30, borderwidth=5)
entryPassword = Entry(root, width=30, borderwidth=5)
btnEnterSupervisi = Button(root, text="Masuk",padx=50, pady=10, command=open)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


labelUser.grid(column=0, row=0)
entryUser.grid(column=1, row=0, pady=5, )
labelPassword.grid(column=0, row=1)
entryPassword.grid(column=1, row=1, pady=5)
btnEnterSupervisi.grid(column=0, row=2, pady=30, columnspan=2)


root.mainloop()