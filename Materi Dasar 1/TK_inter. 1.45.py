
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk() #menampilkan jendela tkinter


window.title("Latihan Tkinter")#judul window
window.configure(bg="#37aed5") #bisa menggunakan warna rgb dengan mengambil code di CSS
window.geometry("500x500")#membuat ukuran window
window.resizable(False,False) #agar window tidak dapat di ubah ukuranya

#membuat frame
input = ttk.Frame(window)
input.pack(padx=5, pady=20, fill="x", expand=True),

#membuat komponen
#1 Label nama depan
sapa = ttk.Label(input,text="Hello World")
sapa.pack(padx=10, pady=10, fill="x", expand=True)

#2 Entry
# nama depan
sapa_label = ttk.Label(input,text="Nama Depan")
sapa_label.pack(padx=10, pady=10, fill="x", expand=True)

nama=tk.StringVar()
Nama = ttk.Entry(input,textvariable=nama)
Nama.pack(padx=10, fill="x", expand=True)

# nama belakang
sapa_label2 = ttk.Label(input,text="Nama Belakang")
sapa_label2.pack(padx=10, pady=10, fill="x", expand=True)

nama2=tk.StringVar()
Nama2 = ttk.Entry(input,textvariable=nama2)
Nama2.pack(padx=10, fill="x", expand=True)

#3 Tombol
def tombol_click():
    label2 = tk.Label(window, text="Hallo "+Nama.get()+ Nama2.get())
    label2.pack()
    showinfo(title="Sapa",message="Hallo "+Nama.get()+ Nama2.get())

tombol= ttk.Button(input, text=" Sapa", command=tombol_click)
tombol.pack(padx=10,pady=10, fill="x", expand=True)

window.mainloop() # agar terus menampilkan jendela hingga file di close