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

class table():
    
    def __init__(self, root):
        for i in range(total_row):
            for j in range(total_colum):
                self.e=Entry(root,width=22)
                #self.e.grid(row=i,column=j) #ada dua metode grid/place
                self.e.place(y=i*20,x=j*60)
                self.e.insert(END, data[i][j])

data=[
    (1,'wahyu', 'mancing',19),
    (2,'putra', 'mabok',20),
    (3,'Azrin', 'menulis',19),
    (4,'ananta', 'membaca',18)      
]
total_row = len(data)
total_colum = len(data[0])

t = table(root)

root.mainloop() #agar jendela dapat tampil terus menerus