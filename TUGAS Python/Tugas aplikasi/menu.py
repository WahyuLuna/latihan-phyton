from tkinter import * # memanggil Tkinter
import tkinter.font

root = Tk() #membuat jendela
root.title("Menu")#judul root
root.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya

#ubah Font
changefont = tkinter.font.Font(size=20)
#buat judul
judul = Label(root,text="== MENU ==", font=changefont).place(x=180, y=0)

#menentukan Lebar jendela
Lebar = 500
Tinggi = 350

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas
root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}") # menentukan posisi dari variable yg telah di tentukan

"""===============[ Codingan ]================"""
nolap = Button(root,text="Cek", ).place(x=20, y=65)

nolap = Button(root,text="Cek", ).place(x=20, y=125)

nolap = Button(root,text="Cek", ).place(x=20, y=185)



root.mainloop() #agar jendela dapat tampil terus menerus