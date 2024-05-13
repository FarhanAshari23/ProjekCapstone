import os
import sys
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import mysql.connector as mysql
from mysql.connector.locales.eng import client_error
from mysql.connector.plugins import mysql_native_password
import webview
from PIL import Image, ImageTk
from datetime import datetime

#window
window = ttk.Window(themename="superhero")
#window.geometry('300x400')
window.title('Pabrik Gula Trangkil: Deteksi K3 Karyawan')
window_width = 1440
window_height = 850
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width/2 - window_width/2)
top = int(display_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

entry_ip = tk.StringVar()
entry_ip.set('192.168.32.232')


def change_ip_host():
    labelLeft1.pack_forget()
    frameLogin1.pack_forget()
    labelRight1.pack_forget()
    global labelIP, entryIP, labelNotes,button_enter_ip
    labelIP = ttk.Label(window, text="Harap Masukkan IP Address Internet Sebelum Masuk", font=("Times New Roman", 30))
    entryIP = ttk.Entry(window, width=20, textvariable=entry_ip, font=("Times New Roman", 20),)
    labelNotes = ttk.Label(window, text="*Catatan: Untuk melihat IP address bisa dilihat melalui setting WiFi pada handphone", font=("Times New Roman", 18))
    button_enter_ip = ttk.Button(window, text='Masuk', bootstyle='info',style='detection.TButton',command=firstLogin)
    labelIP.pack(side='top', pady=130)
    entryIP.pack(side='top', ipadx=150, ipady=20, pady=130)
    labelNotes.pack(side='top', pady=50)
    button_enter_ip.pack(side='top', ipadx=80, ipady=40, pady=10)

def seeProfile():
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()
    frameButton.pack_forget()
    frameCamera.pack_forget()
    tableEmployee.pack_forget()
    tableEmployeeHRD.pack_forget()
    frameUpdateHRD.pack_forget()
    frameEmployeeHRD.pack_forget()
    frameDropIn.pack_forget()
    frameDropOut.pack_forget()
    frameRegist.pack_forget()
    frameKiri.pack_forget()
    labelProfile.pack(expand=True, side='left', fill='both', padx=50)
    label_gambar_satu.pack(expand=True, side='left', fill='both', padx=20)

def detectionAPD():
    global total
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    label_gambar_satu.pack_forget()
    labelProfile.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()
    tableEmployee.pack_forget()
    tableEmployeeHRD.pack_forget()
    frameUpdateHRD.pack_forget()
    frameEmployeeHRD.pack_forget()
    frameDropIn.pack_forget()
    frameDropOut.pack_forget()
    frameRegist.pack_forget()
    frameKiri.pack_forget()
    labelBackDashboard.pack_forget()
    frameButton.pack(side='left', fill='both', expand=True)
    frameCamera.pack(side='right', padx=20)
    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT COUNT(*) as totalkaryawan FROM historymasuk WHERE EXTRACT(DAY FROM tanggal) = EXTRACT(DAY FROM CURRENT_DATE)")
    hasil = mycursor.fetchone()[0]
    total = str(hasil)     

def historyInEmployee():
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    frameKiri.pack_forget()
    label_gambar_satu.pack_forget()
    labelProfile.pack_forget()
    frameButton.pack_forget()
    frameCamera.pack_forget()
    frameRegist.pack_forget()
    frameUpdateHRD.pack_forget()
    tableOut.pack_forget()
    tableEmployee.pack_forget()
    frameEmployeeHRD.pack_forget()
    tableEmployeeHRD.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    frameDropOut.pack_forget()
    frameDropIn.pack(side='top', fill='y')
    tableIn.pack(side='top', fill='both', expand=True)

def historyOutEmployee():
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    frameKiri.pack_forget()
    label_gambar_satu.pack_forget()
    labelProfile.pack_forget()
    frameButton.pack_forget()
    frameRegist.pack_forget()
    frameUpdateHRD.pack_forget()
    frameCamera.pack_forget()
    tableIn.pack_forget()
    tableEmployee.pack_forget()
    frameEmployeeHRD.pack_forget()
    tableEmployeeHRD.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    frameDropIn.pack_forget()
    frameDropOut.pack(side='top', fill='y')
    tableOut.pack(fill='both', expand=True)

def seeEmployee():
    frameKiri.pack_forget()
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    labelProfile.pack_forget()
    frameButton.pack_forget()
    frameRegist.pack_forget()
    frameCamera.pack_forget()
    frameUpdateHRD.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()
    tableEmployeeHRD.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    frameDropIn.pack_forget()
    frameDropOut.pack_forget()
    frameEmployeeHRD.pack_forget()
    for record in tableEmployee.get_children():
        tableEmployee.delete(record)
    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()    
    mycursor.execute("select * from karyawan ORDER BY id_emp DESC")
    employee = mycursor.fetchall()
    for baris in employee:
        name = (baris[1])
        rfid = (baris[2])
        role = (baris[3])
        data = (name, rfid, role)
        tableEmployee.insert(parent='', index=0, values=data)
    tableEmployee.pack(fill='both', expand=True)

def loginHRD():
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    frameKiri.pack_forget()
    label_gambar_satu.pack_forget()
    labelProfile.pack_forget()
    frameButton.pack_forget()
    frameCamera.pack_forget()
    frameUpdateHRD.pack_forget()
    frameRegist.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()
    tableEmployee.pack_forget()
    tableEmployeeHRD.pack_forget()
    frameEmployeeHRD.pack_forget()
    frameDropIn.pack_forget()
    frameDropOut.pack_forget()
    labelLeft.pack(side='left', expand=True, fill="both")
    frameLogin.pack(side='left', expand=True, fill="both")
    labelRight.pack(side='left', expand=True, fill="both")

def regist():
    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()
    username = entryHRD.get()
    password = entryPasswordHRD.get()
    roleDetect = entryRole.get()
    sql = "select * from karyawan where username = %s and password = %s and role = %s"
    mycursor.execute(sql, [(username), (password), (roleDetect)])
    hasil = mycursor.fetchall()

    if hasil:
        entryHRD.delete(0, 'end')
        entryPasswordHRD.delete(0, 'end')
        labelAPI.pack_forget()
        entryAPI.pack_forget()
        button_enter_api.pack_forget()
        frameUpdateHRD.pack_forget()
        frameButton.pack_forget()
        frameCamera.pack_forget()
        label_gambar_satu.pack_forget()
        labelProfile.pack_forget()
        tableIn.pack_forget()
        tableOut.pack_forget()
        tableEmployee.pack_forget()
        frameDropIn.pack_forget()
        frameDropOut.pack_forget()
        frameEmployeeHRD.pack_forget()
        tableEmployeeHRD.pack_forget()
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
         toastHRD.show_toast()
    
def registEmployee():
        labelAPI.pack_forget()
        entryAPI.pack_forget()
        button_enter_api.pack_forget()
        frameButton.pack_forget()
        frameCamera.pack_forget()
        tableIn.pack_forget()
        tableOut.pack_forget()
        label_gambar_satu.pack_forget()
        labelProfile.pack_forget()
        frameUpdateHRD.pack_forget()
        tableEmployee.pack_forget()
        frameEmployeeHRD.pack_forget()
        tableEmployeeHRD.pack_forget()
        frameDropIn.pack_forget()
        frameDropOut.pack_forget()
        labelLeft.pack_forget()
        labelRight.pack_forget()
        frameLogin.pack_forget()
        frameRegist.pack_forget()
        frameKiri.pack(side="left", expand=True, fill='both')

def acceptRegist():
    idEmp = ''
    namaEmp = entryNama.get()
    rfidEmp = entryNIP.get()
    roleEmp = entryJobdesk.get()
    userEmp = ''
    passEmp = ''

    if(namaEmp=='' or rfidEmp=='' or roleEmp==''):
        toastKosong.show_toast()
    else:
        mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
        mycursor = mysqldb.cursor()
        mycursor.execute("insert into karyawan values ('"+idEmp+"','"+namaEmp+"','"+rfidEmp+"','"+roleEmp+"','"+userEmp+"','"+passEmp+"')")
        mycursor.execute("commit")
        entryNama.delete(0, 'end')
        entryNIP.delete(0, 'end')
        entryJobdesk.delete(0, 'end')
        toastSucces.show_toast()
        mysqldb.close()
        
def editEmploye():
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()
    tableEmployee.pack_forget()
    label_gambar_satu.pack_forget()
    labelProfile.pack_forget()
    frameDropIn.pack_forget()
    frameDropOut.pack_forget()
    frameRegist.pack_forget()
    frameKiri.pack_forget()
    frameButton.pack_forget()
    frameCamera.pack_forget()
    frameEmployeeHRD.pack(side = 'top', fill='both')
    tableEmployeeHRD.pack(fill='both', expand=True)
    frameUpdateHRD.pack(side='top', fill='y')
    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()
    for record in tableEmployeeHRD.get_children():
        tableEmployeeHRD.delete(record)
    mycursor.execute("select * from karyawan ORDER BY id_emp DESC")
    employeeHRD = mycursor.fetchall()
    for baris in employeeHRD:
        idEmp =(baris[0])
        name = (baris[1])
        rfid = (baris[2])
        role = (baris[3])
        data = (idEmp, name, rfid, role)
        tableEmployeeHRD.insert(parent='', index=0, values=data)
    mysqldb.close()

def deleteEmployee():
     mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
     mycursor = mysqldb.cursor()
     selected_item = tableEmployeeHRD.focus()
     details = tableEmployeeHRD.item(selected_item)
     resultID = details.get("values")[0]
     nameEmp = details.get("values")[1]
     nameEmpReal = str(nameEmp)
     idEmp = str(resultID)
     print(nameEmpReal, idEmp)
     sql  = "DELETE FROM karyawan where id_emp ='"+idEmp+"'"
     mycursor.execute(sql)
     mycursor.execute("commit")
     toastSuccesDelete   = ToastNotification(
              title='Berhasil Menghapus',
              message='Data Karyawan Bernama '+nameEmpReal+" Berhasil Dihapus",
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='info')
     toastSuccesDelete.show_toast()
     for record in tableEmployeeHRD.get_children():
        tableEmployeeHRD.delete(record)
     mycursor.execute("select * from karyawan ORDER BY id_emp DESC")
     employeeHRD = mycursor.fetchall()
     for baris in employeeHRD:
         idEmp = (baris[0])
         name = (baris[1])
         rfid = (baris[2])
         role = (baris[3])
         data = (idEmp, name, rfid, role)
         tableEmployeeHRD.insert(parent='', index=0, values=data)
     mysqldb.close()

def changeDateOut():
    global bariss
    for record in tableOut.get_children():
        tableOut.delete(record)
    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()
    mycursor.execute("select * from historykeluar WHERE EXTRACT(DAY FROM tanggal) = "+dropDateOut.get()+" and EXTRACT(MONTH FROM tanggal) = "+dropMonthOut.get()+" ORDER BY id_hist DESC")
    bariss = mycursor.fetchall()
    for baris in bariss:
        name = (baris[1])
        rfid = (baris[2])
        histories = (baris[3])
        data = (name, rfid, histories)
        tableOut.insert(parent='', index=0, values=data)

def changeDateIn():
    global rows
    for record in tableIn.get_children():
        tableIn.delete(record)
    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()
    mycursor.execute("select * from historymasuk WHERE EXTRACT(DAY FROM tanggal) = "+dropDateIn.get()+" and EXTRACT(MONTH FROM tanggal) = "+dropMonthIn.get()+" ORDER BY id_hist DESC")
    rows = mycursor.fetchall()
    for baris in rows:
        name = (baris[1])
        rfid = (baris[2])
        histories = (baris[3])
        data = (name, rfid, histories)
        tableIn.insert(parent='', index=0, values=data)

def selectEmp():
    global getIDEmp
    entryNewNameEmp.delete(0, 'end')
    entryNewRfidEmp.delete(0, 'end')
    entryNewRoleEmp.delete(0, 'end')

    selected = tableEmployeeHRD.focus()

    values = tableEmployeeHRD.item(selected, 'values')

    getIDEmp = str(values[0])


    entryNewNameEmp.insert(0, values[1])
    entryNewRfidEmp.insert(0, values[2])
    entryNewRoleEmp.insert(0, values[3])

def updateEmp():
    newNameEmp = entryNewNameEmp.get()
    newRfidEmp = entryNewRfidEmp.get()
    newRoleEmp = entryNewRoleEmp.get()
    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()
    mycursor.execute("update karyawan set name='"+newNameEmp+"', id_rfid='"+newRfidEmp+"',role='"+newRoleEmp+"' where id_emp='"+getIDEmp+"'")
    mycursor.execute("commit")
    toastSuccesUpdate   = ToastNotification(
              title='Berhasil Menghapus',
              message='Data Karyawan Bernama '+newNameEmp+" Berhasil Diperbarui",
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='info')
    toastSuccesUpdate.show_toast()
    entryNewNameEmp.delete(0, 'end')
    entryNewRfidEmp.delete(0, 'end')
    entryNewRoleEmp.delete(0, 'end')
    for record in tableEmployeeHRD.get_children():
        tableEmployeeHRD.delete(record)
    mycursor.execute("select * from karyawan ORDER BY id_emp DESC")    
    employeeHRD = mycursor.fetchall()
    for baris in employeeHRD:
        idEmp =(baris[0])
        name = (baris[1])
        rfid = (baris[2])
        role = (baris[3])
        data = (idEmp, name, rfid, role)
        tableEmployeeHRD.insert(parent='', index=0, values=data)
    mysqldb.close()

def open_webview():
    webview.create_window("Camera Detection", url=entry_api.get()) 
    webview.start()

def layoutAPI():
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()
    frameButton.pack_forget()
    frameCamera.pack_forget()
    tableEmployee.pack_forget()
    tableEmployeeHRD.pack_forget()
    frameUpdateHRD.pack_forget()
    frameEmployeeHRD.pack_forget()
    frameDropIn.pack_forget()
    frameDropOut.pack_forget()
    frameRegist.pack_forget()
    frameKiri.pack_forget()
    label_gambar_satu.pack_forget()
    labelProfile.pack_forget()
    labelAPI.pack(side='top', pady=130)
    entryAPI.pack(side='top', ipadx=150, ipady=20, pady=130)
    button_enter_api.pack(side='top', ipadx=30, ipady=20, pady=30)
    labelBackDashboard.pack(side='top',pady=30)

def changeAPI():
    newAPI = entryAPI.get()
    entry_api.set(newAPI)
    if newAPI:
        toastSuccesAPI.show_toast()

def toggle_password_visibility():
    if show_password.get():
        entryPassword.config(show="")
    else:
        entryPassword.config(show="*")

def toggle_password_visibility_HRD():
    if show_password_HRD.get():
        entryPasswordHRD.config(show="")
    else:
        entryPasswordHRD.config(show="*")

def on_item_click(event):
    selected_item = tableEmployeeHRD.selection()
    
def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def changeCountIn():
    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT COUNT(*) as totalkaryawan FROM historymasuk WHERE EXTRACT(DAY FROM tanggal) = EXTRACT(DAY FROM CURRENT_DATE) AND EXTRACT(MONTH FROM tanggal) = EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(YEAR FROM tanggal) = EXTRACT(YEAR FROM CURRENT_DATE)")
    hasil = mycursor.fetchone()[0]
    newcount = str(hasil)
    print(newcount)
    button_helm.configure(text='Jumlah Karyawan Masuk Hari Ini : '+newcount)

def firstLogin():
    labelIP.pack_forget()
    entryIP.pack_forget()
    labelNotes.pack_forget()
    button_enter_ip.pack_forget()
    global show_password, entryPassword, entryUser, show_password_HRD, labelRight1, frameLogin1, labelLeft1
    print(entry_ip.get())
    toastSuccesIP.show_toast()
    labelLeft1 = ttk.Label(window)
    frameLogin1 = tk.Frame(window)
    labelTop1 = ttk.Label(frameLogin1, text='Silakan Login Terlebih Dahulu', font=("Times New Roman", 30))
    labelUser = ttk.Label(frameLogin1, text="Username", font=("Times New Roman", 20))
    labelPassword = ttk.Label(frameLogin1, text="Password", font=("Times New Roman", 20))
    entryUser = ttk.Entry(frameLogin1, width=20, font=("Times New Roman", 20))
    entryPassword = ttk.Entry(frameLogin1, width=20, show="*", font=("Times New Roman", 20))
    btnEnter = tk.Button(frameLogin1, text="Masuk", bg='#0093DD',command=openWindow)
    labelRight1 = ttk.Label(window)
    show_password = tk.BooleanVar()
    show_password_HRD = tk.BooleanVar()
    my_style = ttk.Style()
    my_style.configure('success.CButton', font=("Times New Roman", 16, 'bold'))
    show_password_checkbox = ttk.Checkbutton(frameLogin1, text="Show Password", variable=show_password, style='round-toggle', command=toggle_password_visibility)
    frameLogin1.columnconfigure((0), weight=1, uniform='a')
    frameLogin1.columnconfigure((1), weight=2, uniform='a')
    frameLogin1.rowconfigure((0,1,2,3,4), weight=1, uniform='a')

    labelTop1.grid(row=0, column=0, columnspan=2)
    labelUser.grid(row=1, column=0)
    entryUser.grid(row=1, column=1)
    labelPassword.grid(row=2, column=0)
    entryPassword.grid(row=2, column=1)
    btnEnter.grid(row=4, column=0, columnspan=3, ipadx=100, ipady=30)
    show_password_checkbox.grid(row=3, columnspan=3, pady=5, sticky='e', ipadx=100, ipady=100)

    labelLeft1.pack(side='left', expand=True, fill="both")
    frameLogin1.pack(side='left', expand=True, fill="both")
    labelRight1.pack(side='left', expand=True, fill="both")

def connect_to_database():
    try:
        mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
        )
        toastSuccesDatabase.show_toast()
    except mysql.Error as err:
        toastFailDatabase.show_toast()

def backHRD():
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    frameUpdateHRD.pack_forget()
    frameButton.pack_forget()
    frameCamera.pack_forget()
    label_gambar_satu.pack_forget()
    labelProfile.pack_forget()
    tableIn.pack_forget()
    tableOut.pack_forget()
    tableEmployee.pack_forget()
    frameDropIn.pack_forget()
    frameDropOut.pack_forget()
    frameEmployeeHRD.pack_forget()
    tableEmployeeHRD.pack_forget()
    frameKiri.pack_forget()
    labelLeft.pack_forget()
    labelRight.pack_forget()
    frameLogin.pack_forget()
    frameRegist.pack(fill='both', expand=True)

def backDashboardAPI():
    labelAPI.pack_forget()
    entryAPI.pack_forget()
    button_enter_api.pack_forget()
    labelBackDashboard.pack_forget()
    button_helm.pack(side='top', expand=True, fill='both', pady=10)
    button_vest.pack(side='top', expand=True, fill='both', pady=10)
    button_detection.pack(side='top', ipadx=80, ipady=80, pady=40)
    button_changeAPI.pack(side='top', ipadx=70, ipady=30)
    frameButton.pack(side='left', fill='both', expand=True)
    frameCamera.pack(side='right', padx=20)

def openWindow():
    global label_gambar_satu, labelProfile
    global tableIn
    global tableOut
    global tableEmployee
    global tableEmployeeHRD
    global frameDropIn
    global frameDropOut
    global frameEmployeeHRD
    global frameButton
    global frameCamera
    global labelLeft, labelRight
    global frameLogin
    global frameRegist
    global entryHRD, entryPasswordHRD, entryRole
    global entryNama, entryNIP, entryJobdesk
    global entryNewNameEmp, entryNewRfidEmp, entryNewRoleEmp
    global frameKiri
    global dropDateOut
    global dropMonthOut
    global dropDateIn
    global dropMonthIn
    global labelAPI,entryAPI,button_enter_api,entry_api
    global frameUpdateHRD,labelBackDashboard
    global button_helm,button_vest,button_detection,button_changeAPI


    mysqldb = mysql.connect(
        user='root',
        password='Tekkom20!',
        host=entry_ip.get(),
        database='capstone',
        auth_plugin='caching_sha2_password',
    )
    mycursor = mysqldb.cursor()


    #create database historyout
    mycursor.execute('select * from historykeluar')
    bariss = mycursor.fetchall()

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
        frameCamera = ttk.Label(window)
        frameButton = tk.Label(window)
        my_style = ttk.Style()
        my_style.configure('detection.TButton', font=("Times New Roman", 28, 'bold'))
        my_style.configure('API.TButton', font=("Times New Roman", 16, 'bold'))
        my_style.configure('edit.TButton', font=("Times New Roman", 14))
        my_style.configure('Treeview.Heading', font=("Times New Roman", 16), rowheight=30)
        my_style.configure("Treeview",
                highlightthickness=0,
                rowheight=30,
                background="#005b96", # Warna latar belakang Treeview
                font=("Times New Roman", 16),  
                fieldbackground="#011f4b")  # Warna latar belakang sel (item) Treeview

        my_style.map("Treeview",
          background=[('selected', '#347083')],  # Warna penyorotan pada item yang dipilih
          foreground=[('selected', '#FFFFFF')])

        mycursor.execute("SELECT COUNT(*) as totalkaryawan FROM historymasuk WHERE EXTRACT(DAY FROM tanggal) = EXTRACT(DAY FROM CURRENT_DATE) AND EXTRACT(MONTH FROM tanggal) = EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(YEAR FROM tanggal) = EXTRACT(YEAR FROM CURRENT_DATE)")
        hasil = mycursor.fetchone()[0]
        total = str(hasil)  

        button_helm = ttk.Button(frameButton, text='Jumlah Karyawan Masuk Hari Ini : '+total, bootstyle='info', style='detection.TButton', command=changeCountIn)
        button_vest = ttk.Button(frameButton, text='Lihat Data Karyawan', bootstyle='info',style='detection.TButton',command=seeEmployee)
        button_detection = ttk.Button(frameCamera, text='Lihat Deteksi Kamera', style='detection.TButton', bootstyle='info',command=open_webview)
        button_changeAPI = ttk.Button(frameCamera, text='Ubah Link API Camera', bootstyle='info',style='API.TButton',width=10, command=layoutAPI)

        def show_text(event):
            # Display text near the cursor when it enters the button
            labelHover.place(x=event.x_root + 10, y=event.y_root - 25)
        def hide_text(event):
            # Hide the text when the cursor leaves the button
            labelHover.place_forget()

        labelHover = ttk.Label(window, text="Tekan Button Untuk Mengupdate Data", font=("Times New Roman", 16), background='blue')
        button_helm.bind("<Enter>", show_text)
        button_helm.bind("<Leave>", hide_text)

        #layout detection
        button_helm.pack(side='top', expand=True, fill='both', pady=10)
        button_vest.pack(side='top', expand=True, fill='both', pady=10)
        button_detection.pack(side='top', ipadx=80, ipady=80, pady=40)
        button_changeAPI.pack(side='top', ipadx=70, ipady=30)
        frameButton.pack(side='left', fill='both', expand=True)
        frameCamera.pack(side='right', padx=20)

        #checkDateNow
        time_now = datetime.now()
        day_now = str(time_now.day)
        month_now = str(time_now.month)

        #layout detection historyIn
        optionsDateIn = [
             '','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', 
             '13','14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 
             '24', '26','27', '28', '29', '30', '31'
        ]
        optionsMonthIn = [
             '','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'
        ]

        frameDropIn = ttk.Frame(window)

        dropDateIn = ttk.Combobox(frameDropIn, values=optionsDateIn, font=("Times New Roman", 16))
        dropDateIn.current(day_now)
        dropMonthIn = ttk.Combobox(frameDropIn, values=optionsMonthIn, font=("Times New Roman", 16))
        dropMonthIn.current(month_now)
        btnInsertDate = ttk.Button(frameDropIn, text="Ubah", command=changeDateIn, bootstyle = 'info')

        labelTanggalMasuk = ttk.Label(frameDropIn, text='Tanggal :', font=("Times New Roman", 16))
        labelBulanMasuk = ttk.Label(frameDropIn, text='Bulan :', font=("Times New Roman", 16))

        tableIn = ttk.Treeview(window, columns = ('Nama', 'ID RFID', 'Jam Masuk'), show = 'headings', style='Treeview.Heading')
        tableIn.heading('Nama', text='Nama',)
        tableIn.heading('ID RFID', text='ID RFID')
        tableIn.heading('Jam Masuk', text='Jam Masuk')
        tableIn.tag_configure("heading", font=("Times New Roman", 20))

        selectedInDate = day_now
        selectedInMonth = month_now

        #create database historyin
        mycursor.execute("select * from historymasuk WHERE EXTRACT(DAY FROM tanggal) = "+selectedInDate+" and EXTRACT(MONTH FROM tanggal) = "+selectedInMonth+" ORDER BY id_hist DESC")
        rows = mycursor.fetchall()

        for baris in rows:
            name = (baris[1])
            rfid = (baris[2])
            histories = (baris[3])
            data = (name, rfid, histories)
            tableIn.insert(parent='', index=0, values=data)
        
        
        labelTanggalMasuk.grid(row=0, column=0, padx=20)
        dropDateIn.grid(row=0, column=1)
        labelBulanMasuk.grid(row=0, column=2, padx=20)
        dropMonthIn.grid(row=0, column=3, padx=20)
        btnInsertDate.grid(row=0, column=4)

        #layout detection historyOut
        optionsDateOut = [
             '','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', 
             '13','14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 
             '24', '26','27', '28', '29', '30', '31'
        ]
        optionsMonthOut = [
             '','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'
        ]

        frameDropOut = ttk.Frame(window)

        labelTanggalKeluar = ttk.Label(frameDropOut, text='Tanggal :', font=("Times New Roman", 16))
        labelBulanKeluar = ttk.Label(frameDropOut, text='Bulan :', font=("Times New Roman", 16))

        dropDateOut = ttk.Combobox(frameDropOut, values=optionsDateOut, font=("Times New Roman", 15))
        dropDateOut.current(day_now)
        dropMonthOut = ttk.Combobox(frameDropOut, values=optionsMonthOut, font=("Times New Roman", 16))
        dropMonthOut.current(month_now)
        btnInsertDateOut = ttk.Button(frameDropOut, text="Ubah", command=changeDateOut, bootstyle = 'info')

        tableOut = ttk.Treeview(window, columns = ('Nama', 'ID RFID', 'Jam Pulang'), show = 'headings', style='Treeview.Heading')
        tableOut.heading('Nama', text='Nama',)
        tableOut.heading('ID RFID', text='ID RFID')
        tableOut.heading('Jam Pulang', text='Jam Pulang')
        tableOut.tag_configure("heading", font=("Times New Roman", 20))

        selectedOutDate = day_now
        selectedOutMonth = month_now

        mycursor.execute("select * from historykeluar WHERE EXTRACT(DAY FROM tanggal) = "+selectedOutDate+" and EXTRACT(MONTH FROM tanggal) = "+selectedOutMonth+" ORDER BY id_hist DESC")
        bariss = mycursor.fetchall()

        for baris in bariss:
            name = (baris[1])
            rfid = (baris[2])
            histories = (baris[3])
            data = (name, rfid, histories)
            tableOut.insert(parent='', index=0, values=data)
        
        labelTanggalKeluar.grid(row=0, column=0, padx=20)
        dropDateOut.grid(row=0, column=1)
        labelBulanKeluar.grid(row=0, column=2, padx=20)
        dropMonthOut.grid(row=0, column=3, padx=20)
        btnInsertDateOut.grid(row=0, column=4)

        #Table Employee
        tableEmployee = ttk.Treeview(window, columns = ('Nama', 'ID RFID', 'Role'), show = 'headings', style='Treeview.Heading')
        tableEmployee.heading('Nama', text='Nama',)
        tableEmployee.heading('ID RFID', text='ID RFID')
        tableEmployee.heading('Role', text='Role')
        
        #loginHRD
        labelLeft = ttk.Label(window)
        frameLogin = tk.Frame(window)
        labelTop = ttk.Label(frameLogin, text='Silakan Login Menggunakan Akun HRD', font=("Times New Roman", 30))
        labelHRD = ttk.Label(frameLogin, text="Username", font=("Times New Roman", 20))
        labelPasswordHRD = ttk.Label(frameLogin, text="Password", font=("Times New Roman", 20))
        entryHRD = ttk.Entry(frameLogin, width=20, font=("Times New Roman", 20))
        entryRole = ttk.Entry(frameLogin, width=20, font=("Times New Roman", 20))
        entryRole.insert(0, "HRD")
        entryPasswordHRD = ttk.Entry(frameLogin, width=20, show="*", font=("Times New Roman", 20))
        btnEnter = tk.Button(frameLogin, text="Masuk", command=regist, bg='#0093DD', font=("Times New Roman", 18))
        show_password_checkbox_HRD = ttk.Checkbutton(frameLogin, text="Show Password", variable=show_password_HRD, style='round-toggle', command=toggle_password_visibility_HRD)
        labelRight = ttk.Label(window)

        frameLogin.columnconfigure((0), weight=1, uniform='a')
        frameLogin.columnconfigure((1), weight=2, uniform='a')
        frameLogin.rowconfigure((0,1,2,3,4), weight=1, uniform='a')

        labelTop.grid(row=0, column=0, columnspan=2)
        labelHRD.grid(row=1, column=0)
        entryHRD.grid(row=1, column=1)
        labelPasswordHRD.grid(row=2, column=0)
        entryPasswordHRD.grid(row=2, column=1)
        show_password_checkbox_HRD.grid(row=3, columnspan=3, pady=5, sticky='e', ipadx=100, ipady=100)
        btnEnter.grid(row=4, column=0, columnspan=3, ipadx=70, ipady=20)

        #Table Employee in HRD
        frameEmployeeHRD = ttk.Frame(window)
        frameUpdateHRD = ttk.Frame(window)

        tableEmployeeHRD = ttk.Treeview(window, columns = ('ID Karyawan','Nama', 'ID RFID', 'Role'), show = 'headings', style='Treeview')
        tableEmployeeHRD.heading('ID Karyawan', text='ID Karyawan',)
        tableEmployeeHRD.heading('Nama', text='Nama',)
        tableEmployeeHRD.heading('ID RFID', text='ID RFID')
        tableEmployeeHRD.heading('Role', text='Role')

        mycursor.execute("select * from karyawan ORDER BY id_emp DESC")
        employess = mycursor.fetchall()

        for baris in employess:
            idEmp = (baris[0])
            name = (baris[1])
            rfid = (baris[2])
            role = (baris[3])
            data = (idEmp, name, rfid, role)
            tableEmployeeHRD.insert(parent='', index=0, values=data)
        
        tableEmployeeHRD.bind("<ButtonRelease-1>", on_item_click)

        btnPilihEmp = ttk.Button(frameEmployeeHRD, text="Pilih", bootstyle = 'primary', style='edit.TButton', command=selectEmp)
        btnHapusEmp = ttk.Button(frameEmployeeHRD, text="Hapus", bootstyle = 'danger', style='edit.TButton', command=deleteEmployee)
        btnKembali = ttk.Button(frameEmployeeHRD, text="Kembali", bootstyle = 'primary', style='edit.TButton', command=backHRD)
        nameNewEmp = ttk.Label(frameUpdateHRD, text="Nama:", font=("Times New Roman", 20))
        entryNewNameEmp = ttk.Entry(frameUpdateHRD, width=20, font=("Times New Roman", 20))
        rfidNewEmp = ttk.Label(frameUpdateHRD, text="ID RFID:", font=("Times New Roman", 20))
        entryNewRfidEmp = ttk.Entry(frameUpdateHRD, width=20, font=("Times New Roman", 20))
        roleNewEmp = ttk.Label(frameUpdateHRD, text="Role:", font=("Times New Roman", 20))
        entryNewRoleEmp = ttk.Entry(frameUpdateHRD, width=20, font=("Times New Roman", 20))
        btnUbahEmp = ttk.Button(frameUpdateHRD, text="Perbarui", bootstyle = 'info', command=updateEmp)

        btnPilihEmp.grid(row=0, column=0, padx=20, ipadx=20, ipady=5)
        btnHapusEmp.grid(row=0, column=1, ipadx=20, padx=20, ipady=5)
        btnKembali.grid(row=0, column=2, ipadx=20, ipady=5)
        nameNewEmp.grid(row=0, column=0)
        rfidNewEmp.grid(row=0, column=1)
        roleNewEmp.grid(row=0, column=2)
        entryNewNameEmp.grid(row=1, column=0, padx=20)
        entryNewRfidEmp.grid(row=1, column=1, padx=20)
        entryNewRoleEmp.grid(row=1, column=2, padx=20)
        btnUbahEmp.grid(row=2, column=0, columnspan=3, pady=20, ipadx=30, ipady=20)

        #choose registration
        frameRegist = ttk.Frame(window)
        frameRegist.rowconfigure((0,1), weight=1, uniform='a')
        frameRegist.columnconfigure((0,1), weight=1, uniform='a')
        labelRegist = ttk.Label(frameRegist, text='Silakan pilih:', font=('Times New Roman', 24))
        buttonEmployee = tk.Button(frameRegist, text='Tambah Karyawan', font=('Times New Roman', 24), fg='blue', command=registEmployee)
        buttonSupervisi = tk.Button(frameRegist, text='Ubah Data Karyawan', font=('Times New Roman', 24), fg='blue', command=editEmploye)
        labelRegist.grid(row=0, column=0, columnspan=2)
        buttonEmployee.grid(row=1, column=0, ipadx=80, ipady=80)
        buttonSupervisi.grid(row=1, column=1, ipadx=80, ipady=80)

        #registration Employee
        frameKiri = ttk.Frame(window)
        labelOpening = ttk.Label(frameKiri, text="Silakan Masukkan Data:", font=("Times New Roman", 30))
        labelNama = ttk.Label(frameKiri, text='Nama', font=("Times New Roman", 20))
        entryNama = ttk.Entry(frameKiri, width=20, font=("Times New Roman", 20))
        labelNIP = ttk.Label(frameKiri, text='ID RFID', font=("Times New Roman", 20))
        entryNIP = ttk.Entry(frameKiri, width=20, font=("Times New Roman", 20))
        labelJobdesk = ttk.Label(frameKiri, text='Jobdesk', font=("Times New Roman", 20))
        entryJobdesk = ttk.Entry(frameKiri, width=20, font=("Times New Roman", 20))
        buttonRegist = tk.Button(frameKiri, text='Tambah', font=('Times New Roman', 12), bg='blue', fg='white', command=acceptRegist)
        labelBackHRD = ttk.Label(frameKiri, text='Kembali', font=("Times New Roman", 16), cursor="hand2")
        labelBackHRD.bind("<Button-1>", lambda event: backHRD())
        
        frameKiri.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')
        frameKiri.columnconfigure((0,1), weight=1, uniform='a')

        labelOpening.grid(row=0, column=0, columnspan=2)
        labelNama.grid(row=1, column=0)
        entryNama.grid(row=1, column=1)
        labelNIP.grid(row=2, column=0)
        entryNIP.grid(row=2, column=1)
        labelJobdesk.grid(row=3, column=0)
        entryJobdesk.grid(row=3, column=1)
        buttonRegist.grid(row=4, column=0, columnspan=2, ipadx=50, ipady=20)
        labelBackHRD.grid(row=5, column=0, columnspan=2)

        #widget profile
        labelProfile = ttk.Label(window, text='Pabrik Gula Trangkil merupakan cabang dari PT Kebon Agung yang terletak di Desa Trangkil Kecamatan Trangkil, Kabupaten Pati. PG Trangkil memilih tebu berkualitas tinggi sebagai bahan baku produksi gula kristal. PG Trangkil menerapkan Keselamatan dan Kesehatan Kerja (K3) bagi karyawan di lingkungan kantor dan pabrik. Proses pembuatan gula menggunakan mesin modern sehingga menghasilkan gula yang bersih dengan minim limbah lingkungan.\n\nVisi PG Trangkil adalah menjadi perusahaan yang berdaya saing tingkat tinggi di tingkat regional. Sedangkan kami memiliki 4 misi yaitu Memberikan nilai tambah optimal bagi Pemegang Saham. Membangun kemitraan dengan Pemangku Kepentingan berdasarkan asas saling menguntungkan. Mengembangkan usaha agribisnis berbasis tebu dan turunannya secara berkesinambungan. Memberikan nilai tambah kepada konsumen dengan menghasilkan produk berkualitas. Mewujudkan bisnis berwawasan lingkungan.\n\nNomor Telepon : 0295-381005, 0295-393283\nFaksimile: 0295-393284\nEmail : pgtk@ptkebonagung.com\nInstagram : pgtrangkil_official', font=("Times New Roman", 16, 'bold'), wraplength=900)
        gambar_pil_satu = Image.open(resource_path0("profile.png"))
        gambar_tk_satu = ImageTk.PhotoImage(gambar_pil_satu)
        label_gambar_satu = ttk.Label(window)
        label_gambar_satu.config(image=gambar_tk_satu)
        label_gambar_satu.image = gambar_tk_satu

        #widget Change API
        entry_api = tk.StringVar()
        entry_api.set("http://192.168.216.80:18331/")
        labelAPI = ttk.Label(window, text="Silakan Masukkan API Camera Terbaru:", font=("Times New Roman", 30))
        entryAPI = ttk.Entry(window, width=20, textvariable=entry_api, font=("Times New Roman", 20),)
        button_enter_api = tk.Button(window, text='Ubah', font=("Times New Roman", 18), bg='#0093DD', command=changeAPI)
        labelBackDashboard = ttk.Label(window, text='Kembali', font=("Times New Roman", 16), cursor="hand2")
        labelBackDashboard.bind("<Button-1>", lambda event: backDashboardAPI())

        #menu
        menu = tk.Menu(window)

        #menu fitur
        apd_menu = tk.Menu(menu, tearoff=False)
        apd_menu.add_command(label="Pendeteksian APD", command=detectionAPD)
        apd_menu.add_command(label="Pendaftaran Karyawan", command=loginHRD)
        menu.add_cascade(label="Fitur-fitur", menu=apd_menu)


        #menu history
        history_menu = tk.Menu(menu, tearoff=False)
        history_menu.add_command(label="History Masuk", command=historyInEmployee)
        history_menu.add_command(label="History Keluar", command=historyOutEmployee)
        menu.add_cascade(label="History Karyawan", menu=history_menu)

        #menu others
        apd_menu = tk.Menu(menu, tearoff=False)
        apd_menu.add_command(label="Profil Perusahaan", command=seeProfile)
        menu.add_cascade(label="Lainnya", menu=apd_menu)

        window.configure(menu=menu)
    elif entryUser.get() == '' and entryPassword.get() == '':
         toastKosong.show_toast()
    elif mysql.errors:
        toastSalah.show_toast()
    else:
         print('salah pass')
         print(entryUser.get())
         print (entryPassword.get())
         toastSalah.show_toast()

labelLeft1 = ttk.Label(window)
frameLogin1 = tk.Frame(window)
labelTop1 = ttk.Label(frameLogin1, text='Silakan Login Terlebih Dahulu', font=("Times New Roman", 30))
labelUser = ttk.Label(frameLogin1, text="Username", font=("Times New Roman", 20))
labelPassword = ttk.Label(frameLogin1, text="Password", font=("Times New Roman", 20))
entryUser = ttk.Entry(frameLogin1, width=20, font=("Times New Roman", 20))
entryPassword = ttk.Entry(frameLogin1, width=20, show="*", font=("Times New Roman", 20))
btnEnter = tk.Button(frameLogin1, text="Masuk", bg='#0093DD', font=("Times New Roman", 18), command=openWindow)
btnChangeIP = tk.Button(frameLogin1, text="Ubah IP", bg='#0093DD',command=change_ip_host)
btnDatabase = tk.Button(frameLogin1, text="Cek Database", bg='#0093DD',command=connect_to_database)
labelRight1 = ttk.Label(window)
show_password = tk.BooleanVar()
show_password_HRD = tk.BooleanVar()
my_style = ttk.Style()
my_style.configure('success.CButton', font=("Times New Roman", 16, 'bold'))
show_password_checkbox = ttk.Checkbutton(frameLogin1, text="Show Password", variable=show_password, style='round-toggle', command=toggle_password_visibility)
frameLogin1.columnconfigure((0,1), weight=1, uniform='a')
frameLogin1.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')

labelTop1.grid(row=0, column=0, columnspan=2)
labelUser.grid(row=1, column=0)
entryUser.grid(row=1, column=1)
labelPassword.grid(row=2, column=0)
entryPassword.grid(row=2, column=1)
btnEnter.grid(row=4, column=0, columnspan=3, ipadx=100, ipady=30)
btnDatabase.grid(row=5, column=1, ipadx=50, ipady=15)
btnChangeIP.grid(row=5, column=0, ipadx=50, ipady=15)
show_password_checkbox.grid(row=3, columnspan=3, pady=5, sticky='e', ipadx=100, ipady=100)

labelLeft1.pack(side='left', expand=True, fill="both")
frameLogin1.pack(side='left', expand=True, fill="both")
labelRight1.pack(side='left', expand=True, fill="both")


toastKosong = ToastNotification(
              title='Terjadi Kesalahan',
              message='Harap isi kolom yang disediakan',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='danger')

toastSalah = ToastNotification(
              title='Terjadi Kesalahan',
              message='Username atau password yang diisikan salah, harap coba lagi',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='danger')

toastHRD   = ToastNotification(
              title='Terjadi Kesalahan',
              message='Harap masuk dengan menggunakan akun HRD',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='danger')

toastSucces   = ToastNotification(
              title='Berhasil',
              message='Data Karyawan Berhasil Ditambahkan',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='info')

toastSuccesAPI   = ToastNotification(
              title='Berhasil',
              message='API berhasil diubah',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='info')

toastSuccesIP   = ToastNotification(
              title='Berhasil',
              message='IP berhasil diubah',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='info')

toastSuccesDatabase   = ToastNotification(
              title='Sesuai',
              message='Database berhasil terhubung',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='info')

toastWaitDatabase   = ToastNotification(
              title='Mohon Ditunggu',
              message='Aplikasi sedang mencoba terhubung dengan database....',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='info')

toastFailDatabase   = ToastNotification(
              title='Terputus',
              message='Koneksi dengan database terputus, harap ubah ip melalui button "Ubah IP"',
              duration=3000,
              position=(15, 15, 'nw'),
              bootstyle='danger')

window.iconbitmap(resource_path0('Logo.ico'))

#run
window.mainloop()