from tkinter import * # memanggil Tkinter
from tkinter.ttk import * # memanggil Tkinter

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

page_check = 0
def halaman_1():
    
    global lblframe01,page_check,lbl1,btn1
    if page_check ==0:
        pass
    else:
        lbl2.destroy()
        btn2.destroy()    
    
    page_check = 1
    lblframe01=LabelFrame(root).grid()
    lbl1=Label(lblframe01,text="Halaman 1")
    lbl1.grid(row=0,column=0)
    btn1=Button(lblframe01,text="Page 02",command=halaman_2)
    btn1.grid(row=1)
    

def halaman_2():
    lbl1.destroy()
    btn1.destroy()
    global lblframe02,page_check,lbl2,btn2
    page_check = 2
    lblframe02=LabelFrame(root).grid()
    lbl2=Label(lblframe02,text="Halaman 2")
    lbl2.grid(row=0,column=5)
    btn2=Button(lblframe02,text="Page 01",command=halaman_1)
    btn2.grid(row=1)


halaman_1()

root.mainloop() #agar jendela dapat tampil terus menerus