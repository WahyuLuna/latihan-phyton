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
#Membuat entry in
##Entry adalah perintahnya
e = Entry(root,bg ="gray", fg = "black", width = 60)
e.place(x=40, y=20)

e2 = Entry(root,show = "*",bg ="gray", fg = "black", width = 60) #show agar nilai entry menjadi kosong 
e2.place(x=40, y=40)

def aksi():
    lbl = Label(root, text =e.get()) #e.get = untuk mengambil nilai entry
    lbl.grid()
    lbl = Label(root, text =e2.get())
    lbl.grid()
def hapus():
    e.delete(0,END) # end hapus Semua
    e2.delete(0,None) # None Hapus Satu persatu

btn = Button(root,text = "hasil", command = aksi)
btn.place(x=40, y=60)
btn = Button(root,text = "Hapus", command = hapus)
btn.place(x=40, y=80)


root.mainloop() #agar jendela dapat tampil terus menerus