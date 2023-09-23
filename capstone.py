import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from tkinter_webcam import webcam
from ttkbootstrap.toast import ToastNotification
import mysql.connector as mysql

#window
window = ttk.Window(themename="solar")
#window.geometry('300x400')
window.title('Pendeteksian APD Karyawan')

window_width = 1440
window_height = 850
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width/2 - window_width/2)
top = int(display_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

def detectionAPD():
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()
    frameRegist.pack_forget()
    frameKananBefore.pack_forget()
    frameKananAfter.pack_forget()
    frameKiri.pack_forget()
    frameButton.pack(side='left', fill='both', expand=True)
    frameCamera.pack(side='right', padx=20)

def historyInEmployee():
    frameKananBefore.pack_forget()
    frameKananAfter.pack_forget()
    frameKiri.pack_forget()
    frameButton.pack_forget()
    frameCamera.pack_forget()
    frameRegist.pack_forget()
    tableOut.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    tableIn.pack(fill='both', expand=True)

def historyOutEmployee():
    frameKananBefore.pack_forget()
    frameKananAfter.pack_forget()
    frameKiri.pack_forget()
    frameButton.pack_forget()
    frameRegist.pack_forget()
    frameCamera.pack_forget()
    tableIn.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    tableOut.pack(fill='both', expand=True)

def loginHRD():
    frameKananBefore.pack_forget()
    frameKananAfter.pack_forget()
    frameKiri.pack_forget()
    frameButton.pack_forget()
    frameCamera.pack_forget()
    frameRegist.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()

    labelLeft.pack(side='left', expand=True, fill="both")
    frameLogin.pack(side='left', expand=True, fill="both")
    labelRight.pack(side='left', expand=True, fill="both")

def regist():
    if entryHRD.get() == 'farhan' and entryPasswordHRD.get() == 'ashari23':
        frameButton.pack_forget()
        frameCamera.pack_forget()
        tableIn.pack_forget()
        tableOut.pack_forget()
        frameKananBefore.pack_forget()
        frameKananAfter.pack_forget()
        frameKiri.pack_forget()
        labelLeft.pack_forget()
        labelRight.pack_forget()
        frameLogin.pack_forget()
        frameRegist.pack(fill='both', expand=True)
    elif entryHRD.get() == '' and entryPasswordHRD.get() == '':
         print('kosongan')
         toastKosong.show_toast()
    else:
         print('salah pass')
         toastSalah.show_toast()
    
def registEmployee():
        frameButton.pack_forget()
        frameCamera.pack_forget()
        tableIn.pack_forget()
        tableOut.pack_forget()
        labelLeft.pack_forget()
        labelRight.pack_forget()
        frameLogin.pack_forget()
        frameRegist.pack_forget()
        frameKiri.pack(side="left", expand=True, fill='both')
        frameKananBefore.pack(side="left", expand=True, fill='both')

def acceptRegist():
        frameButton.pack_forget()
        frameCamera.pack_forget()
        tableIn.pack_forget()
        tableOut.pack_forget()
        labelLeft.pack_forget()
        labelRight.pack_forget()
        frameLogin.pack_forget()
        frameRegist.pack_forget()
        frameKananBefore.pack_forget()
        frameKiri.pack(side="left", expand=True, fill='both')
        frameKananAfter.pack(side="left", expand=True, fill='both')
        
def openWindow():
    global tableIn
    global tableOut
    global frameButton
    global frameCamera
    global labelLeft, labelRight
    global frameLogin
    global frameRegist
    global entryHRD, entryPasswordHRD
    global frameKananBefore, frameKananAfter, frameKiri

    #create database history
    con = mysql.connect(host="localhost", user='root', password='', database='db_capstone')
    cursor = con.cursor()
    cursor.execute('select * from historymasuk')
    rows = cursor.fetchall()

    #create database username
    kon = mysql.connect(host="localhost", user='root', password='', database='db_capstone')
    kursor = kon.cursor()
    kursor.execute('select * from karyawan')
    bariss = kursor.fetchall()

    mysqldb = mysql.connect(host="localhost", user='root', password='', database='db_capstone')
    mycursor = mysqldb.cursor()
    username = entryUser.get()
    password = entryPassword.get()

    sql = "select * from karyawan where username = %s and password = %s"
    mycursor.execute(sql, [(username), (password)])
    results = mycursor.fetchall()

    if results:
        labelLeft1.pack_forget()
        frameLogin1.pack_forget()
        labelRight1.pack_forget()
        #widgets detection APD
        frameCamera = ttk.LabelFrame(window, text="Frame Camera Detection")
        video = webcam.Box(frameCamera)
        video.show_frames()
        frameButton = ttk.Frame(window)

        my_style = ttk.Style()
        my_style.configure('danger.TButton', font=("Times New Roman", 28, 'bold'), background='red')
        my_style.configure('succes.TButton', font=("Times New Roman", 28, 'bold'), background='green')
        my_style.configure('Treeview.Heading', font=("Times New Roman", 16), rowheight=30)

        label_helm = ttk.Button(frameButton, text='Deteksi Helm', bootstyle="primary", style='succes.TButton')
        label_vest = ttk.Button(frameButton, text='Deteksi Rompi', bootstyle="warning", style='danger.TButton')
        label_idcard = ttk.Button(frameButton, text='Deteksi ID Card', bootstyle="warning", style='danger.TButton')

        #layout detection
        label_helm.pack(side='top', expand=True, fill='both')
        label_vest.pack(side='top', expand=True, fill='both')
        label_idcard.pack(side='top', expand=True, fill='both')
        frameButton.pack(side='left', fill='both', expand=True)
        frameCamera.pack(side='right', padx=20)

        #layout detection historyIn
        tableIn = ttk.Treeview(window, columns = ('Nama', 'ID', 'Jam Masuk'), show = 'headings', style='Treeview.Heading')
        tableIn.heading('Nama', text='Nama',)
        tableIn.heading('ID', text='ID')
        tableIn.heading('Jam Masuk', text='Jam Masuk')


        for baris in rows:
            name = (baris[0])
            rfid = (baris[1])
            histories = (baris[2])
            data = (name, rfid, histories)
            print(rfid)
            tableIn.insert(parent='', index=0, values=data)

        #layout detection historyOut
        tableOut = ttk.Treeview(window, columns = ('Nama', 'ID', 'Jam Pulang'), show = 'headings', style='Treeview.Heading')
        tableOut.heading('Nama', text='Nama')
        tableOut.heading('ID', text='ID')
        tableOut.heading('Jam Pulang', text='Jam Pulang')

        for row in rows:
            name = (row[0])
            rfid = (row[1])
            histories = (row[2])
            data = (name, rfid, histories)
            print(name)
            tableOut.insert(parent='', index=0, values=data)

        #loginHRD
        labelLeft = ttk.Label(window)
        frameLogin = tk.Frame(window)
        labelTop = ttk.Label(frameLogin, text='Silakan Login Menggunakan Akun HRD', font=("Times New Roman", 20))
        labelHRD = ttk.Label(frameLogin, text="Username")
        labelPasswordHRD = ttk.Label(frameLogin, text="Password")
        entryHRD = ttk.Entry(frameLogin, width=30)
        entryPasswordHRD = ttk.Entry(frameLogin, width=30, show="*")
        btnEnter = ttk.Button(frameLogin, text="Masuk", command=regist, bootstyle = 'warning')
        labelRight = ttk.Label(window)

        frameLogin.columnconfigure((0), weight=1, uniform='a')
        frameLogin.columnconfigure((1), weight=2, uniform='a')
        frameLogin.rowconfigure((0,1,2,3), weight=1, uniform='a')

        labelTop.grid(row=0, column=0, columnspan=2)
        labelHRD.grid(row=1, column=0)
        entryHRD.grid(row=1, column=1)
        labelPasswordHRD.grid(row=2, column=0)
        entryPasswordHRD.grid(row=2, column=1)
        btnEnter.grid(row=3, column=0, columnspan=3, ipadx=70, ipady=20)

        #choose registration
        frameRegist = ttk.Frame(window)
        frameRegist.rowconfigure((0,1), weight=1, uniform='a')
        frameRegist.columnconfigure((0,1), weight=1, uniform='a')
        labelRegist = ttk.Label(frameRegist, text='Silakan pilih:', font=('Times New Roman', 24))
        buttonEmployee = tk.Button(frameRegist, text='Tambah Karyawan', font=('Times New Roman', 24), fg='blue', command=registEmployee)
        buttonSupervisi = tk.Button(frameRegist, text='Tambah Supervisi', font=('Times New Roman', 24), fg='blue')
        labelRegist.grid(row=0, column=0, columnspan=2)
        buttonEmployee.grid(row=1, column=0, ipadx=80, ipady=80)
        buttonSupervisi.grid(row=1, column=1, ipadx=80, ipady=80)

        #registration Employee
        frameKananBefore = ttk.Frame(window)
        frameKananAfter = ttk.Frame(window)
        frameKiri = ttk.Frame(window)
        labelOpening = ttk.Label(frameKiri, text="Silakan Masukkan Data:", font=("Times New Roman", 20))
        name_save = tk.StringVar(value = '')
        nip_save = tk.StringVar(value='')
        jobdesk_save = tk.StringVar(value='')
        labelNama = ttk.Label(frameKiri, text='Nama')
        entryNama = ttk.Entry(frameKiri, width=30, textvariable=name_save)
        labelNIP = ttk.Label(frameKiri, text='NIP')
        entryNIP = ttk.Entry(frameKiri, width=30, textvariable=nip_save)
        labelJobdesk = ttk.Label(frameKiri, text='Jobdesk')
        entryJobdesk = ttk.Entry(frameKiri, width=30, textvariable=jobdesk_save)
        buttonRegist = tk.Button(frameKiri, text='Tambah', font=('Times New Roman', 12), bg='blue', fg='white', command=acceptRegist)
        
        frameKiri.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
        frameKiri.columnconfigure((0,1), weight=1, uniform='a')

        labelOpening.grid(row=0, column=0, columnspan=2)
        labelAck = ttk.Label(frameKananAfter, text="Data Berhasil Ditambahkan", font=("Times New Roman", 16))
        labelNamaConfirm1 = ttk.Label(frameKananAfter, text='Nama : ', font=('Times New Roman', 14))
        labelNamaConfirm = ttk.Label(frameKananAfter, textvariable=name_save, font=('Times New Roman', 14))
        labelNIPConfirm1 = ttk.Label(frameKananAfter, text='NIP : ', font=('Times New Roman', 14))
        labelNIPConfirm = ttk.Label(frameKananAfter, textvariable=nip_save, font=('Times New Roman', 14))
        labelJobdeskConfirm1 = ttk.Label(frameKananAfter, text='Jobdesk :', font=('Times New Roman', 14))
        labelJobdeskConfirm = ttk.Label(frameKananAfter, textvariable=jobdesk_save, font=('Times New Roman', 14))
        buttonClear = tk.Button(frameKananAfter, text='Selesai', font=('Times New Roman', 12), bg='green')
        labelAck.grid(row=0, column=0, columnspan=2)
        labelNamaConfirm1.grid(row=1, column=0)
        labelNamaConfirm.grid(row=1, column=1)
        labelNIPConfirm1.grid(row=2, column=0)
        labelNIPConfirm.grid(row=2, column=1)
        labelJobdeskConfirm1.grid(row=3, column=0)
        labelJobdeskConfirm.grid(row=3, column=1)
        buttonClear.grid(row=4, column=0, columnspan=2, ipadx=50, ipady=20)
        labelNama.grid(row=1, column=0)
        entryNama.grid(row=1, column=1)
        labelNIP.grid(row=2, column=0)
        entryNIP.grid(row=2, column=1)
        labelJobdesk.grid(row=3, column=0)
        entryJobdesk.grid(row=3, column=1)
        buttonRegist.grid(row=4, column=0, columnspan=2, ipadx=50, ipady=20)

        frameKananAfter.columnconfigure((0,1), weight=1, uniform='a')
        frameKananAfter.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
        
        #menu
        menu = tk.Menu(window)

        #sub menu
        apd_menu = tk.Menu(menu, tearoff=False)
        apd_menu.add_command(label="Pendeteksian APD", command=detectionAPD)
        apd_menu.add_command(label="Pendaftaran Karyawan", command=loginHRD)
        menu.add_cascade(label="Fitur-fitur", menu=apd_menu)


        #another sub menu
        history_menu = tk.Menu(menu, tearoff=False)
        history_menu.add_command(label="History Masuk", command=historyInEmployee)
        history_menu.add_command(label="History Keluar", command=historyOutEmployee)
        menu.add_cascade(label="History Karyawan", menu=history_menu)

        window.configure(menu=menu)
    elif entryUser.get() == '' and entryPassword.get() == '':
         toastKosong.show_toast()
    else:
         print('salah pass')
         print(entryUser.get())
         print (entryPassword.get())
         toastSalah.show_toast()

#login
labelLeft1 = ttk.Label(window)
frameLogin1 = tk.Frame(window)
labelTop1 = ttk.Label(frameLogin1, text='Silakan Login Terlebih Dahulu', font=("Times New Roman", 20))
labelUser = ttk.Label(frameLogin1, text="Username")
labelPassword = ttk.Label(frameLogin1, text="Password")
entryUser = ttk.Entry(frameLogin1, width=30)
entryPassword = ttk.Entry(frameLogin1, width=30, show="*")
btnEnter = ttk.Button(frameLogin1, text="Masuk", bootstyle='info',command=openWindow)
labelRight1 = ttk.Label(window)

toastKosong = ToastNotification(
              title='Terjadi Kesalahan',
              message='Harap isi kolom username dan password yang telah disediakan',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='danger')

toastSalah = ToastNotification(
              title='Terjadi Kesalahan',
              message='Username atau password yang diisikan salah, harap coba lagi',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='danger')

frameLogin1.columnconfigure((0), weight=1, uniform='a')
frameLogin1.columnconfigure((1), weight=2, uniform='a')
frameLogin1.rowconfigure((0,1,2,3), weight=1, uniform='a')

labelTop1.grid(row=0, column=0, columnspan=2)
labelUser.grid(row=1, column=0)
entryUser.grid(row=1, column=1)
labelPassword.grid(row=2, column=0)
entryPassword.grid(row=2, column=1)
btnEnter.grid(row=3, column=0, columnspan=3, ipadx=70, ipady=20)

labelLeft1.pack(side='left', expand=True, fill="both")
frameLogin1.pack(side='left', expand=True, fill="both")
labelRight1.pack(side='left', expand=True, fill="both")

#run
window.mainloop()