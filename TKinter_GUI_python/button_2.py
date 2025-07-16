from tkinter import * # memanggil Tkinter

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

"""===============[ Codingan ]================"""
#membuat tombol
# Button adalah perintah
# membuat fungtion aksi untuk aksi dari button
def aksi():
    label = Label(root,text = "Berhasil",padx = 10, pady = 10)
    label.grid()
    btn = Button(root,text = "Clik", command = aksi)
    btn.place(x = 70, y = 40)


btn = Button(root,text = "Clik", command = aksi)
btn.place(x = 70, y = 20)



root.mainloop() #agar jendela dapat tampil terus menerus