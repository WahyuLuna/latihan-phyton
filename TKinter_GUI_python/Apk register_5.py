from tkinter import * # memanggil Tkinter
import tkinter.font

root = Tk() #membuat jendela
root.title("Form Pendaftaran")#judul root
root.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya

#menentukan Lebar jendela
Lebar = 600
Tinggi = 600

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas
root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}") # menentukan posisi dari variable yg telah di tentukan

#ubah Font
changefont = tkinter.font.Font(size=20)
#buat judul
judul = Label(root,text="Form Registrasi", font=changefont).place(x=180, y=0)

"""===============[ Codingan ]================"""
# Membuat variable
nama= Label(root,text = "First Name")
nama2= Label(root,text = "Last Name")
age= Label(root,text = "Umur")
User= Label(root,text = "User Name")
Email= Label(root,text = "Email")
Gender= Label(root,text = "Gender")


labelfr = LabelFrame(root,text="Result", padx= 100,pady= 100).place(x=150, y=290)

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root)
e4 = Entry(root,width=40)
e5 = Entry(root,width=40)
e6 = Entry(root,width=40)

nama.place(x=20, y=30)
nama2.place(x=20, y=60)
age.place(x=20, y=90)
User.place(x=20, y=120)
Email.place(x=20, y=150)
Gender.place(x=20, y=180)

e1.place(x=100, y=30)
e2.place(x=100, y=60)
e3.place(x=100, y=90)
e4.place(x=100, y=120)
e5.place(x=100, y=150)



r = StringVar()# untuk menampung semua variabel (Intvar/Stringvar)
r.set("male")#memberiakn nilai default

rb =Radiobutton(root,text = "male",variable = r,value="male").place(x=100, y=180)
rb2 =Radiobutton(root,text = "female",variable = r,value="female").place(x=150, y=180)

def cetak():
    class data:
        
        def __init__(self, nama,nama2,age,User,Email,Gender):
            self.nama = nama
            self.nama2 = nama2
            self.age = age
            self.User = User
            self.Email = Email
            self.Gender = Gender
            
        def Tampil(self):
            label = Label(labelfr, text = "Tampil\n"                      
                          "\nnama : "+self.nama+self.nama2+
                          "\nAge : "+self.age+
                          "\nUser : "+self.User+
                          "\nEmail : "+self.Email+
                          "\nGender : "+self.Gender).place(x=150, y=300)
            
    ditampilkan = data(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),r.get())
    ditampilkan.Tampil()
    
hasil = Button(root,text="Submit",command=cetak).place(x=150, y=240)







root.mainloop() #agar jendela dapat tampil terus menerus