from tkinter import * # memanggil Tkinter
from tkinter import messagebox 
import tkinter.font


root = Tk() #membuat jendela
root.title("Latihan Tkinter")#judul root
root.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya
root.geometry(f"500x350+500+200") # menentukan posisi dari variable yg telah di tentukan

root2 = Tk() #membuat jendela
root2.title("Latihan Tkinter")#judul root2
root2.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya
root2.geometry(f"500x350+500+200") # menentukan posisi dari variable yg telah di tentukan

root3 = Tk() #membuat jendela
root3.title("Latihan Tkinter")#judul root3
root3.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya
root3.geometry(f"600x350+500+200") # menentukan posisi dari variable yg telah di tentukan


rmenu = Tk() #membuat jendela
rmenu.title("Latihan Tkinter")#judul rmenu
rmenu.resizable(False,False) #agar Window/tampilan tidak dapat di ubah ukuranya
rmenu.geometry(f"500x350+500+200") # menentukan posisi dari variable yg telah di tentukan

#ubah Font
changefont = tkinter.font.Font(size=20)


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

"""===============[ Page 1 ]================"""

def page1():
  global page
  page = 1
  judul = Label(root,text="LOGIN", font=changefont).place(x=190, y=0)
  user= Label(root,text = "Nama")
  Password= Label(root,text = "Password")
  id= Label(root,text = "id")

  click = StringVar()
  e1 = Entry(root,width=40)
  e2 = Entry(root,width=40)
  e3 = OptionMenu(root,click,211,212,213,214)

  user.place(x=20, y=65)
  Password.place(x=20, y=105)
  id.place(x=20, y=145)

  e1.place(x=120, y=65)
  e2.place(x=120, y=105)
  e3.place(x=120, y=145)


  def login():
      pass1 = int(e2.get())
      show_data = f"SELECT * FROM `kasir` WHERE id_pg = '{click.get()}'"
      cursor.execute(show_data) #perintah menampilkan data
      results = cursor.fetchall()
      print(results)
      data_kasir = results[0]
      print(data_kasir)
      nama_pg = data_kasir[0]
      password_pg = data_kasir[1]
      print(nama_pg)
      print(password_pg)
      if nama_pg ==e1.get() and password_pg==pass1:
          messagebox.showinfo("Notification", "Input anda berhasil")
          menu()
      else :
          messagebox.showinfo("Notification", "Salah Memasukan Input")
          
      

  submit = Button(root,text="Login", command=login).place(x=150, y=240)


"""===============[ Page 2 ]================"""  
def page2():
  
  global page
  page = 2
  # Membuat variable
  nama= Label(root2,text = "Nama")
  durasi= Label(root2,text = "Durasi")
  type= Label(root2,text = "Type")
  tgl = Label(root2,text = "Tanggal")
  tgl2 = Label(root2,text = "YYYY-MM-DD")
  id = Label(root2,text = "ID")


  labelfr = LabelFrame(root2,text="Result", padx= 100,pady= 100).place(x=150, y=290)

  click = StringVar()
  click2 = IntVar()

  e1 = Entry(root2,width=40)
  e2 = Entry(root2,width=40)
  e3 = OptionMenu(root2,click,"FUTSAL","VOLI","BADMINTON","BASKET")
  e4 = Entry(root2,width=40)
  e5 = Entry(root2,width=40)

  nama.place(x=20, y=65)
  durasi.place(x=20, y=95)
  type.place(x=20, y=125)
  tgl.place(x=20, y=155)
  tgl2.place(x=350, y=155)
  id.place(x=20, y=185)

  e1.place(x=100, y=65)
  e2.place(x=100, y=95)
  e3.place(x=100, y=120)
  e4.place(x=100, y=155)
  e5.place(x=100, y=185)

  def check():

    if  click.get() == "BASKET":
      no = OptionMenu(root2,click2,41,42,43)
    elif click.get() == "VOLI":
      no = OptionMenu(root2,click2,21,22,23)
    elif click.get() == "FUTSAL":
      no = OptionMenu(root2,click2,11,12,13)
    elif click.get() == "BADMINTON":
      no = OptionMenu(root2,click2,31,32,33)
    no.place(x=250, y=120)
    
      

  def masuk():
      try :
        # gunakan perintah seperti menggunakan MYSQL pada umunya (membuat,mengubah,menambah,menghapus, dll)
        query = (f"INSERT INTO pelanggan (`nama`, `durasi`, `type`, `nolapangan`, `tanggal`, `id`) VALUES ('{e1.get()}', '{e2.get()}', '{click.get()}', '{click2.get()}','{e4.get()}','{e5.get()}')") #perhatikan dengan akurat symbol ""/''/,/()
        cursor.execute(query)# unutk menjalankana program
        db.commit()
        messagebox.showinfo("Notification", "Input anda berhasil")
      except :
        messagebox.showinfo("Notification", "Salah Memasukan Input")


                            
  nolap = Button(root2,text="Cek", command=check).place(x=210, y=123)
  hasil = Button(root2,text="Submit", command=masuk).place(x=150, y=240)
  menubut = Button(root2,text="MENU", command=menu).place(x=420, y=20)

  

"""===============[ Page 3 ]================"""
def page3():
  global page
  page = 3
  judul = Label(root3,text="data costumer", font=changefont).place(x=120, y=0)
  class table():
    
    def __init__(self, root3):
        for i in range(total_row):
            for j in range(total_colum):
                self.e=Entry(root3,width=22)
                self.e.grid(row=i,column=j) #ada dua metode grid/place
                #self.e.place(y=(i*20)+50,x=j*60)
                self.e.insert(END, results[i][j])
                
  show_data = f"SELECT * FROM `struk`"
  cursor.execute(show_data) #perintah menampilkan data
  results = cursor.fetchall()
  print(results)
  total_row = len(results)
  total_colum = len(results[0])
  t = table(root3)
  nolap = Button(root3,text="MENU", command=menu).place(x=420, y=20)
  
  
"""===============[ Menu ]================"""
  
def menu():
    global page
    page = 4
    judul = Label(rmenu,text="== MENU ==", font=changefont).place(x=180, y=0)
  
    nolap = Button(rmenu,text="page 1", command=page1).place(x=20, y=65)

    nolap = Button(rmenu,text="page 2", command=page2).place(x=20, y=125)

    nolap = Button(rmenu,text="page 3", command=page3).place(x=20, y=185)
    
"""===============[ option ]================"""

page1()
if page == 1:
  root.mainloop()
elif page == 2:
  root2.mainloop()
elif page == 3:  
  root3.mainloop()
elif page == 2:
  rmenu.mainloop() 
