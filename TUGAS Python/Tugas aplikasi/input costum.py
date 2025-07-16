import tkinter
import customtkinter
from tkinter import messagebox 

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("CustomTkinter")
root.resizable(False,False)

#menentukan Lebar jendela
Lebar = 600
Tinggi = 400

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas
root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}")

# Data base
import mysql.connector
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "db_sewa_lapangan"
)
cursor = db.cursor()
"""===============[ Codingan ]================"""

frame_1 = customtkinter.CTkFrame(master=root)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

#buat judul
logo_label = customtkinter.CTkLabel(frame_1, text="Input Id Pelanggan", font=customtkinter.CTkFont(size=25, weight="bold"))
logo_label.place(x=200, y=0)

# Membuat variable
nama= customtkinter.CTkLabel(master=frame_1,text="nama", justify=tkinter.LEFT)
durasi= customtkinter.CTkLabel(master=frame_1,text="durasi", justify=tkinter.LEFT)
type= customtkinter.CTkLabel(master=frame_1,text="type", justify=tkinter.LEFT)
tgl = customtkinter.CTkLabel(master=frame_1,text="Tanggal", justify=tkinter.LEFT)
tgl2 = customtkinter.CTkLabel(master=frame_1,text="YYYY-MM-DD", justify=tkinter.LEFT)
id = customtkinter.CTkLabel(master=frame_1,text="ID", justify=tkinter.LEFT)

nama.place(x=20, y=60)
durasi.place(x=20, y=110)
type.place(x=20, y=160)
tgl.place(x=20, y=210)
tgl2.place(x=260, y=210)
id.place(x=20, y=260)

e1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
e2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
e3 = customtkinter.CTkOptionMenu(frame_1, values=["FUTSAL","VOLI","BADMINTON","BASKET"])
e4 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
e5 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")


e1.place(x=100, y=60)
e2.place(x=100, y=110)
e3.place(x=100, y=160)
e4.place(x=100, y=210)
e5.place(x=100, y=260)

def check():
    global nolapangan
    if  e3.get() == "BASKET":
        nolapangan = customtkinter.CTkOptionMenu(frame_1, values=["41","42","43"])
    elif e3.get() == "VOLI":
        nolapangan = customtkinter.CTkOptionMenu(frame_1, values=["21","22","23"])
    elif e3.get() == "FUTSAL":
        nolapangan = customtkinter.CTkOptionMenu(frame_1, values=["11","12","13"])
    elif e3.get() == "BADMINTON":
        nolapangan = customtkinter.CTkOptionMenu(frame_1, values=["31","32","33"])
    nolapangan.place(x=420, y=160)
  
def masuk():
    new = int(nolapangan.get())
    try :        
      # gunakan perintah seperti menggunakan MYSQL pada umunya (membuat,mengubah,menambah,menghapus, dll)
      query = (f"INSERT INTO pelanggan (`nama`, `durasi`, `type`, `nolapangan`, `tanggal`, `id`) VALUES ('{e1.get()}', '{e2.get()}', '{e3.get()}', '{new}','{e4.get()}','{e5.get()}')") #perhatikan dengan akurat symbol ""/''/,/()
      cursor.execute(query)# unutk menjalankana program
      db.commit()
      messagebox.showinfo("Notification", "Input anda berhasil")
      frame_1.destroy()
    except :
        messagebox.showinfo("Notification", "Salah Memasukan Input")


cek = customtkinter.CTkButton(master=frame_1,text="cek", command=check)
hasil = customtkinter.CTkButton(master=frame_1,text="Submit", command=masuk)
cek.place(x=260, y=160)
hasil.place(x=100, y=300)


root.mainloop()