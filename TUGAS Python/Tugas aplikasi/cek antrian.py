from tkinter import * # memanggil Tkinter
import tkinter.font

root = Tk() #membuat jendela
root.title("Latihan Tkinter")#judul root
root.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya

#ubah Font
changefont = tkinter.font.Font(size=20)
#buat judul
judul = Label(root,text="data costumer", font=changefont).place(x=120, y=0)

#menentukan Lebar jendela
Lebar = 600
Tinggi = 350

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas
root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}") # menentukan posisi dari variable yg telah di tentukan
 # menentukan posisi dari variable yg telah di tentukan

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

class table():
    
    def __init__(self, root):
        for i in range(total_row):
            for j in range(total_colum):
                self.e=Entry(root,width=22)
                #self.e.grid(row=i,column=j) #ada dua metode grid/place
                self.e.place(y=(i*20)+50,x=j*60)
                self.e.insert(END, results[i][j])

show_data = f"SELECT * FROM `pelanggan`"
cursor.execute(show_data) #perintah menampilkan data
results = cursor.fetchall()
print(results)
total_row = len(results)
print(total_row)
total_colum = len(results[0])
print(total_colum)
t = table(root)


root.mainloop() #agar jendela dapat tampil terus menerus