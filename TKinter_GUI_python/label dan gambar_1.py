from tkinter import * # memanggil Tkinter

window = Tk() #membuat jendela
window.title("Latihan Tkinter")#judul window
window.resizable(False,False) #agar window tidak dapat di ubah ukuranya

#menentukan Lebar jendela
Lebar = 500
Tinggi = 350

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas

window.geometry(f"{Lebar}x{Tinggi}+{x}+{y}") # menentukan posisi dari variable yg telah di tentukan

# membuat label jendela
#Label untuk perintahnya
#text untuk menampilkan text  
#bg untuk  warna background text
#fg untuk Warna Font
#padx & pady untuk luas background text
lbl = Label(window,text  = "Hello World", bg="red",fg="black",padx = 10,pady = 10)
#lbl.grid() # untuk lokasi yang tidak di tentukan
lbl.place(x=20,y=10) #<-- digunakan apa bila ingin menempatkan posisi lebih akurat X dan Y


# menambahkan Foto
# PhotoImage adalah perintahnya
#file harus berada satu directory
photo = PhotoImage(file="Foto.png")
lbl2=Label(window, image=photo)
lbl2.place(x= 10, y=30)


window.mainloop() #agar jendela dapat tampil terus menerus