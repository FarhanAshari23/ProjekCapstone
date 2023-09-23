import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from tkinter_webcam import webcam
from random import choice

#window
window = ctk.CTk()
window.title('Login')
window_width = 400
window_height = 500
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width/2 - window_width/2)
top = int(display_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

def detectionAPD():
    pass

def historyInEmployee():
    pass

def historyOutEmployee():
    pass

def loginHRD():
    pass

def regist():
    pass

def registEmployee():
    pass

def acceptRegist():
    pass


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

    if entryUser.get() == 'farhan' and entryPassword.get() == 'ashari23':
        window.quit()
        windowMain = ctk.CTk()
        windowMain_width = 1440
        windowMain_height = 850
        display_width = windowMain.winfo_screenwidth()
        display_height = windowMain.winfo_screenheight()
        leftMain = int(display_width/2 - windowMain_width/2)
        topMain = int(display_height/2 - windowMain_height/2)
        windowMain.geometry(f'{windowMain_width}x{windowMain_height}+{leftMain}+{topMain}')
        windowMain.title("Pendeteksian APD Karyawan Pabrik")

        #widgets detection APD
        frameCamera = tk.LabelFrame(windowMain, text="Frame Camera Detection")
        video = webcam.Box(frameCamera)
        video.show_frames()
        frameButton = tk.Frame(windowMain)
        button_helm = tk.Label(frameButton, text='Deteksi Helm',bg='green', font=('Times New Roman', 30), borderwidth=3, relief='ridge')
        button_vest = tk.Label(frameButton, text='Deteksi Rompi', bg='red', font=('Times New Roman', 30), borderwidth=3, relief='ridge')
        button_idcard = tk.Label(frameButton, text='Deteksi ID Card', bg='red', font=('Times New Roman', 30), borderwidth=3, relief='ridge')

        #layout detection
        button_helm.pack(side='top', expand=True, fill='both')
        button_vest.pack(side='top', expand=True, fill='both')
        button_idcard.pack(side='top', expand=True, fill='both')
        frameButton.pack(side='left', fill='both', expand=True)
        frameCamera.pack(side='right')

        
        #menu
        menu = tk.Menu(windowMain)

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

        windowMain.configure(menu=menu)

#login
labelUser = ctk.CTkLabel(window, text="Username")
labelPassword = ctk.CTkLabel(window, text="Password")
entryUser = ctk.CTkEntry(window, width=150, height=20, corner_radius=5)
entryPassword = ctk.CTkEntry(window, width=150, height=20, corner_radius=5)
btnEnter = ctk.CTkButton(window, text="Masuk", command=openWindow)

window.columnconfigure((0,1), weight=1, uniform='a')
window.rowconfigure((0,1,2), weight=1, uniform='a')

labelUser.grid(column=0, row=0)
entryUser.grid(row=0, column=1)
labelPassword.grid(row=1, column=0)
entryPassword.grid(row=1, column=1)
btnEnter.grid(row=2, column=0, columnspan=2, ipadx=50, ipady=20, padx=10)

#run
window.mainloop()