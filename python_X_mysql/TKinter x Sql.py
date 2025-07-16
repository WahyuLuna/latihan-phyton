from tkinter import * # memanggil Tkinter
import tkinter.font

root = Tk() #membuat jendela
root.title("Latihan Tkinter")#judul root
root.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya

#menentukan Lebar jendela
Lebar = 500
Tinggi = 350

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas
root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}") # menentukan posisi dari variable yg telah di tentukan


#ubah Font
changefont = tkinter.font.Font(size=20)
#buat judul
judul = Label(root,text="Input Data", font=changefont).place(x=120, y=0)


# Data base
import mysql.connector
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "latihanpy"
)
cursor = db.cursor()

"""===============[ Codingan ]================"""

# Membuat variable
nama= Label(root,text = "Nama")
harga= Label(root,text = "Alamat")
type= Label(root,text = "Jurusan")

labelfr = LabelFrame(root,text="Result", padx= 100,pady= 100).place(x=150, y=290)

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root,width=40)

nama.place(x=20, y=65)
harga.place(x=20, y=95)
type.place(x=20, y=125)


e1.place(x=100, y=65)
e2.place(x=100, y=95)
e3.place(x=100, y=125)


def masuk():
    
    # gunakan perintah seperti menggunakan MYSQL pada umunya (membuat,mengubah,menambah,menghapus, dll)
    query = (f"INSERT INTO data_diri (nama, alamat, jurusan) VALUES ('{e1.get()}', '{e2.get()}', '{e3.get()}')") #perhatikan dengan akurat symbol ""/''/,/()
    cursor.execute(query)# unutk menjalankana program
    db.commit()

                          
hasil = Button(root,text="Submit", command=masuk).place(x=150, y=240)
root.mainloop() #agar jendela dapat tampil terus menerus