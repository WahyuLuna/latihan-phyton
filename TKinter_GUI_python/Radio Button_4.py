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
#membuat radio button

r = StringVar()# untuk menampung semua variabel (Intvar/Stringvar)
r.set("male")#memberiakn nilai default

def cetak(nilai):
    Label(root,text= nilai).grid()

rb =Radiobutton(root,text = "male",variable = r,value="male",command = lambda:cetak(r.get())).grid()
rb2 =Radiobutton(root,text = "female",variable = r,value="female",command = lambda:cetak(r.get())).grid()





root.mainloop() #agar jendela dapat tampil terus menerus