from tkinter import * # memanggil Tkinter
from tkinter import messagebox 
import tkinter.font


root2 = Tk() #membuat jendela
root2.title("Latihan Tkinter")#judul root2
root2.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya

#menentukan Lebar jendela
Lebar = 500
Tinggi = 350

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas
root2.geometry(f"{Lebar}x{Tinggi}+{x}+{y}") # menentukan posisi dari variable yg telah di tentukan


#ubah Font
changefont = tkinter.font.Font(size=20)
#buat judul
judul = Label(root2,text="Input Id Pelanggan", font=changefont).place(x=120, y=0)


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

# Membuat variable
nama= Label(root2,text = "Nama")
durasi= Label(root2,text = "Durasi")
type= Label(root2,text = "Type")
tgl = Label(root2,text = "Tanggal")
tgl2 = Label(root2,text = "YYYY-MM-DD")
id = Label(root2,text = "ID")


labelfr = LabelFrame(root2,text="Result", padx= 100,pady= 100).place(x=150, y=290)

click = StringVar()
click2 = IntVar()

e1 = Entry(root2,width=40)
e2 = Entry(root2,width=40)
e3 = OptionMenu(root2,click,"FUTSAL","VOLI","BADMINTON","BASKET")
e4 = Entry(root2,width=40)
e5 = Entry(root2,width=40)

nama.place(x=20, y=65)
durasi.place(x=20, y=95)
type.place(x=20, y=125)
tgl.place(x=20, y=155)
tgl2.place(x=350, y=155)
id.place(x=20, y=185)

e1.place(x=100, y=65)
e2.place(x=100, y=95)
e3.place(x=100, y=120)
e4.place(x=100, y=155)
e5.place(x=100, y=185)

def check():

  if  click.get() == "BASKET":
    no = OptionMenu(root2,click2,41,42,43)
  elif click.get() == "VOLI":
    no = OptionMenu(root2,click2,21,22,23)
  elif click.get() == "FUTSAL":
    no = OptionMenu(root2,click2,11,12,13)
  elif click.get() == "BADMINTON":
    no = OptionMenu(root2,click2,31,32,33)
  no.place(x=250, y=120)
  
    

def masuk():
    try :
      # gunakan perintah seperti menggunakan MYSQL pada umunya (membuat,mengubah,menambah,menghapus, dll)
      query = (f"INSERT INTO pelanggan (`nama`, `durasi`, `type`, `nolapangan`, `tanggal`, `id`) VALUES ('{e1.get()}', '{e2.get()}', '{click.get()}', '{click2.get()}','{e4.get()}','{e5.get()}')") #perhatikan dengan akurat symbol ""/''/,/()
      cursor.execute(query)# unutk menjalankana program
      db.commit()
      messagebox.showinfo("Notification", "Input anda berhasil")
    except :
      messagebox.showinfo("Notification", "Salah Memasukan Input")


                          
nolap = Button(root2,text="Cek", command=check).place(x=210, y=123)
hasil = Button(root2,text="Submit", command=masuk).place(x=150, y=240)


root2.mainloop() #agar jendela dapat tampil terus menerus
