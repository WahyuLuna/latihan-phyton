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
frame = LabelFrame(root,text="Frame 1",padx =20,pady=40)
frame.grid()

lbl=Label(frame,text="ini adalah frame tulisan")
lbl.grid()


root.mainloop() #agar jendela dapat tampil terus menerus