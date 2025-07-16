import tkinter
import customtkinter
from tkinter import messagebox 
from PIL import Image

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("Sewa Lapangan")
root.resizable(False,False)

#menentukan Lebar jendela
Lebar = 600
Tinggi = 400

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas
root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}")

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

"""===============[ LOGIN ]================"""
def login_menu():
    frame_log = customtkinter.CTkFrame(master=root)
    frame_log.pack(pady=20, padx=60, fill="both", expand=True)
    
    #buat judul
    logo_label = customtkinter.CTkLabel(frame_log, text="LOGIN", font=customtkinter.CTkFont(size=25, weight="bold"))
    logo_label.place(x=200, y=10)

    user= customtkinter.CTkLabel(master=frame_log,text="user", justify=tkinter.LEFT)
    Password= customtkinter.CTkLabel(master=frame_log,text="Password", justify=tkinter.LEFT)
    id = customtkinter.CTkLabel(master=frame_log,text="ID", justify=tkinter.LEFT)

    user.place(x=20, y=60)
    Password.place(x=20, y=110)
    id.place(x=20, y=160)

    e1 = customtkinter.CTkEntry(master=frame_log, placeholder_text="")
    e2 = customtkinter.CTkEntry(master=frame_log, placeholder_text="")
    e3 = customtkinter.CTkOptionMenu(frame_log, values=["211","212","213","214"])

    e1.place(x=100, y=60)
    e2.place(x=100, y=110)
    e3.place(x=100, y=160)

    def login():
        global id_kas
        nama1 = e1.get()
        nama1 = nama1.lower()
        pass1 = int(e2.get())
        id_kas = int(e3.get())
        show_data = f"SELECT * FROM `kasir` WHERE id_pg = '{id_kas}'"
        cursor.execute(show_data) #perintah menampilkan data
        results = cursor.fetchall()
        print(results)
        data_kasir = results[0]
        print(data_kasir)
        nama_pg = data_kasir[0]
        password_pg = data_kasir[1]
        print(nama_pg)
        print(password_pg)
        if nama_pg ==nama1 and password_pg==pass1:
            messagebox.showinfo("Notification", "Input anda berhasil")
            frame_log.destroy()
            menu()
        else :
            messagebox.showinfo("Notification", "Salah Memasukan Input")
            
    def admin_log():
        global id_kas
        dialog = customtkinter.CTkInputDialog(text="Enter Password", title="Admin")
        ad = int(dialog.get_input())
        if  ad== 1:
            id_kas = 111
            messagebox.showinfo("Notification", "hallo Wahyu")
            frame_log.destroy()
            menu()
        else :
            messagebox.showinfo("Notification"
                                , "Password salah")
 
    masuk = customtkinter.CTkButton(master=frame_log,text="Login", command=login)
    masuk.place(x=170, y=300)
    admin = customtkinter.CTkButton(master=frame_log,text="Admin", command=admin_log, width=10, height=10)
    admin.place(x=400, y=15)

"""===============[ MENU ]================"""
def menu():
    frame_men = customtkinter.CTkFrame(master=root)
    frame_men.pack(pady=20, padx=60, fill="both", expand=True)
    
    #buat judul
    logo_label = customtkinter.CTkLabel(frame_men, text="MENU", font=customtkinter.CTkFont(size=25, weight="bold"))
    logo_label.place(x=200, y=10)

    def to_log():
        frame_men.destroy()
        login_menu()
    def to_in():
        frame_men.destroy()
        menu_input()
    def to_data():
        frame_men.destroy()
        data_user()
    def to_lap():
        frame_men.destroy()
        data_lap()
    input_user= customtkinter.CTkLabel(master=frame_men,text="Input Costumer", justify=tkinter.LEFT)
    data_costumer= customtkinter.CTkLabel(master=frame_men,text="Data Costumer", justify=tkinter.LEFT)
    data_lapangan = customtkinter.CTkLabel(master=frame_men,text="Data Lapangan", justify=tkinter.LEFT)

    input_user.place(x=20, y=60)
    data_costumer.place(x=20, y=110)
    data_lapangan.place(x=20, y=160)

    e1 = customtkinter.CTkButton(master=frame_men,text="Go", command=to_in)
    e2 = customtkinter.CTkButton(master=frame_men,text="Go", command=to_data)
    e3 = customtkinter.CTkButton(master=frame_men,text="Go", command=to_lap)

    e1.place(x=130, y=60)
    e2.place(x=130, y=110)
    e3.place(x=130, y=160)    
    back_menu = customtkinter.CTkButton(master=frame_men,text="Logout", command=to_log,width=10, height=25)
    back_menu.place(x=10, y=10)

"""===============[ INPUT COSTUMER ]================"""
def menu_input():
    frame_in = customtkinter.CTkFrame(master=root)
    frame_in.pack(pady=20, padx=20, fill="both", expand=True)

    #buat judul
    logo_label = customtkinter.CTkLabel(frame_in, text="Input Id Pelanggan", font=customtkinter.CTkFont(size=25, weight="bold"))
    logo_label.place(x=200, y=0)

    # Membuat variable
    nama= customtkinter.CTkLabel(master=frame_in,text="nama", justify=tkinter.LEFT)
    durasi= customtkinter.CTkLabel(master=frame_in,text="durasi", justify=tkinter.LEFT)
    type= customtkinter.CTkLabel(master=frame_in,text="type", justify=tkinter.LEFT)
    tgl = customtkinter.CTkLabel(master=frame_in,text="Tanggal", justify=tkinter.LEFT)
    tgl2 = customtkinter.CTkLabel(master=frame_in,text="YYYY-MM-DD", justify=tkinter.LEFT)
    id = customtkinter.CTkLabel(master=frame_in,text="ID", justify=tkinter.LEFT)

    nama.place(x=20, y=60)
    durasi.place(x=20, y=110)
    type.place(x=20, y=160)
    tgl.place(x=20, y=210)
    tgl2.place(x=260, y=210)
    id.place(x=20, y=260)

    e1 = customtkinter.CTkEntry(master=frame_in, placeholder_text="")
    e2 = customtkinter.CTkEntry(master=frame_in, placeholder_text="")
    e3 = customtkinter.CTkOptionMenu(frame_in, values=["FUTSAL","VOLI","BADMINTON","BASKET"])
    e4 = customtkinter.CTkEntry(master=frame_in, placeholder_text="")
    e5 = customtkinter.CTkEntry(master=frame_in, placeholder_text="")

    e1.place(x=100, y=60)
    e2.place(x=100, y=110)
    e3.place(x=100, y=160)
    e4.place(x=100, y=210)
    e5.place(x=100, y=260)

    def check():
        global nolapangan, harga
        if  e3.get() == "BASKET":
            nolapangan = customtkinter.CTkOptionMenu(frame_in, values=["41","42","43"])
            harga = 50000
        elif e3.get() == "VOLI":
            nolapangan = customtkinter.CTkOptionMenu(frame_in, values=["21","22","23"])
            harga = 30000
        elif e3.get() == "FUTSAL":
            nolapangan = customtkinter.CTkOptionMenu(frame_in, values=["11","12","13"])
            harga = 70000
        elif e3.get() == "BADMINTON":
            nolapangan = customtkinter.CTkOptionMenu(frame_in, values=["31","32","33"])
            harga = 35000
        nolapangan.place(x=300, y=160)
    
    def masuk():
        global new
        import random
        new = int(nolapangan.get())
        lama = int(e2.get())
        ran = random.randint(1,100)
        try :        
            # gunakan perintah seperti menggunakan MYSQL pada umunya (membuat,mengubah,menambah,menghapus, dll)
            query = (f"INSERT INTO pelanggan (`nama`, `durasi`, `type`, `nolapangan`, `tanggal`, `id`) VALUES ('{e1.get()}', '{e2.get()}', '{e3.get()}', '{new}','{e4.get()}','{e5.get()}')") #perhatikan dengan akurat symbol ""/''/,/()
            cursor.execute(query)# unutk menjalankana program
            db.commit()
            total = harga*lama
            query = (f"INSERT INTO `struk` (`no_struk`, `nama`, `id`, `durasi`, `type`, `tanggal`, `nolapangan`, `id_pg`, `total`) VALUES ('{ran}', '{e1.get()}', '{e5.get()}', '{e2.get()}', '{e3.get()}', '{e4.get()}', '{new}', '{id_kas}', '{total}')")
            cursor.execute(query)
            db.commit()
            messagebox.showinfo("Notification", "Input anda berhasil")
        except :
            messagebox.showinfo("Notification", "Salah Memasukan Input")


    cek = customtkinter.CTkButton(master=frame_in,text="cek", command=check,width=10, height=10)
    hasil = customtkinter.CTkButton(master=frame_in,text="Submit", command=masuk)
    cek.place(x=260, y=165)
    hasil.place(x=100, y=300)
    
    def back_in():
        frame_in.destroy()
        menu()
    back_menu = customtkinter.CTkButton(master=frame_in,text="MENU", command=back_in,width=10, height=20)
    back_menu.place(x=10, y=10)
    def to_user():
        frame_in.destroy()
        data_user()
    to_user = customtkinter.CTkButton(master=frame_in,text="Check_Out", command=to_user,width=10, height=20)
    to_user.place(x=450, y=10)

"""===============[ DATA COSTUMER ]================"""
def data_user():
    global frame_data
    root.geometry(f"800x400+500+200")
    frame_data = customtkinter.CTkFrame(master=root)
    frame_data.pack(pady=10, padx=10, fill="both", expand=True)
    
    #buat judul
    logo_label = customtkinter.CTkLabel(frame_data, text="Input Id Pelanggan", font=customtkinter.CTkFont(size=25, weight="bold"))
    logo_label.place(x=250, y=0)
    
    class table():
    
        def __init__(self, frame_data):
            for i in range(total_row):
                for j in range(total_colum):
                    self.e = customtkinter.CTkTextbox(master=frame_data, width=150, height=10)
                    self.e.place(y=(i*20)+50,x=j*75)
                    self.e.insert("0.0",f"{results[i][j]}")
    
    show_data = f"SELECT * FROM `struk`"
    cursor.execute(show_data) #perintah menampilkan data
    results = cursor.fetchall()
    print(results)
    total_row = len(results)
    total_colum = len(results[0])
    t = table(frame_data)
    
    def to_menu():
        frame_data.destroy()
        root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}")
        menu()
    back_menu = customtkinter.CTkButton(master=frame_data,text="MENU", command=to_menu,width=10, height=20)
    back_menu.place(x=10, y=10)
    cek_out = customtkinter.CTkButton(master=frame_data,text="Check Out", command=check_out,width=10, height=20)
    cek_out.place(x=550, y=10)
  
"""===============[ Check Out ]================"""   
def check_out():
    frame_data.destroy()
    root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}")
    frame_check = customtkinter.CTkFrame(master=root)
    frame_check.pack(pady=2, padx=10, fill="both", expand=True)

    #buat judul
    logo_label = customtkinter.CTkLabel(frame_check, text="Check Out", font=customtkinter.CTkFont(size=25, weight="bold"))
    logo_label.place(x=250, y=0)
    
    nostruk= customtkinter.CTkLabel(master=frame_check,text="No Struk", justify=tkinter.LEFT)
    nostruk.place(x=20, y=60)
    e1 = customtkinter.CTkEntry(master=frame_check, placeholder_text="")
    e1.place(x=100, y=60)
    
    def tampil_struk():

        frame_check2 = customtkinter.CTkFrame(master=frame_check,width=350, height=160)
        frame_check2.place(y=210, x=10)
        show_data = f"SELECT nama,id,tanggal,type,nolapangan,durasi FROM `pelanggan` WHERE id= {no_user}"
        cursor.execute(show_data)
        results2 = cursor.fetchall()
        print(results2)
        data_user = results2[0]
        print(data_user)
        data_1 = data_user[0]
        data_2 = data_user[1]
        data_3 = data_user[2]
        data_4 = data_user[3]
        data_5 = data_user[4]
        data_6 = data_user[5]

        nama= customtkinter.CTkLabel(master=frame_check2,text=f"nama \t\t:   {data_1}", justify=tkinter.LEFT).place(x=20, y=10)
        id= customtkinter.CTkLabel(master=frame_check2,text=f"id \t\t:   {data_2}", justify=tkinter.LEFT).place(x=20, y=40)
        tgl= customtkinter.CTkLabel(master=frame_check2,text=f"Tanggal \t\t: {data_3}", justify=tkinter.LEFT).place(x=20, y=70)
        lapangan= customtkinter.CTkLabel(master=frame_check2,text=f"Lapangan\t\t:    {data_4} - {data_5}", justify=tkinter.LEFT).place(x=20, y=100)
        durasi= customtkinter.CTkLabel(master=frame_check2,text=f"durasi \t\t:   {data_6}", justify=tkinter.LEFT).place(x=20, y=130)

        
    def cek_user():
        global no_user
        try:        
            no_st = int(e1.get())
            cari_id = f"SELECT id FROM `struk` WHERE no_struk = {no_st}"
            cursor.execute(cari_id)
            results1 = cursor.fetchall()
            print(results1)
            data_struk = results1[0]
            print(data_struk)
            no_user = data_struk[0]
            print(no_user)
            tampil_struk()
        except :
            messagebox.showinfo("Notification", "Salah Memasukan No struk")

    def delete_data():
        dialog = customtkinter.CTkInputDialog(text="Apakah anda ingin menghapus data ?", title="root")
        ad = int(dialog.get_input())
        if ad == 123:
            try:
                delete = (f"DELETE FROM pelanggan where id = '{no_user}'") 
                cursor.execute(delete)
                db.commit()
                messagebox.showinfo("Notification", "data telah di hapus")
            except :
                messagebox.showinfo("Notification", "data tidak ditemukan")
        else:
            messagebox.showinfo("Notification", "salah code")
                    
    def to_data():
        frame_check.destroy()
        data_user()
        
    
    cek_data = customtkinter.CTkButton(master=frame_check,text="cek", command=cek_user,width=10, height=20)
    cek_data.place(x=250, y=63)
    back_menu = customtkinter.CTkButton(master=frame_check,text="<-Back", command=to_data,width=10, height=20)
    back_menu.place(x=10, y=10)
    delete_user = customtkinter.CTkButton(master=frame_check,text="DELETE", command=delete_data,width=20, height=30)
    delete_user.place(x=250, y=150)
    
"""===============[ DATA LAPANGAN ]================"""
def data_lap():
    frame_lap = customtkinter.CTkFrame(master=root)
    frame_lap.pack(pady=20, padx=20, fill="both", expand=True)

    tabview_1 = customtkinter.CTkTabview(master=frame_lap, width=700, height=500)
    tabview_1.pack(pady=10, padx=10)
    tabview_1.add("BASKET")
    tabview_1.add("VOLI")
    tabview_1.add("BADMINTON")
    tabview_1.add("FUTSAL")

    nama1= customtkinter.CTkLabel(tabview_1.tab("BASKET"),text="Nama : BASKET", justify=tkinter.LEFT).place(x=20, y=60)
    durasi1= customtkinter.CTkLabel(tabview_1.tab("BASKET"),text="Harga/jam : 50.000", justify=tkinter.LEFT).place(x=20, y=110)
    type1= customtkinter.CTkOptionMenu(tabview_1.tab("BASKET"), values=["41","42","43"]).place(x=20, y=160)
    img_lap=customtkinter.CTkImage(Image.open(f"C:\VS CODE FILE FACTORY\latihan phyton\TUGAS Python/tugas 2\gambar_lap/basket.jfif"),size=(250,250))
    img_l = customtkinter.CTkLabel(tabview_1.tab("BASKET"),image=img_lap).place(x= 250, y=10)

    nama2= customtkinter.CTkLabel(tabview_1.tab("VOLI"),text="Nama : VOLI", justify=tkinter.LEFT).place(x=20, y=60)
    durasi2= customtkinter.CTkLabel(tabview_1.tab("VOLI"),text="Harga/jam : 30.000", justify=tkinter.LEFT).place(x=20, y=110)
    type2= customtkinter.CTkOptionMenu(tabview_1.tab("VOLI"), values=["21","22","23"]).place(x=20, y=160)
    img_lap2=customtkinter.CTkImage(Image.open(f"C:\VS CODE FILE FACTORY\latihan phyton\TUGAS Python/tugas 2\gambar_lap/voli.jfif"),size=(250,250))
    img_l = customtkinter.CTkLabel(tabview_1.tab("VOLI"),image=img_lap2).place(x= 250, y=10)

    nama3= customtkinter.CTkLabel(tabview_1.tab("BADMINTON"),text="Nama : BADMINTON", justify=tkinter.LEFT).place(x=20, y=60)
    durasi3= customtkinter.CTkLabel(tabview_1.tab("BADMINTON"),text="Harga/jam : 35.000", justify=tkinter.LEFT).place(x=20, y=110)
    type3= customtkinter.CTkOptionMenu(tabview_1.tab("BADMINTON"), values=["31","32","33"]).place(x=20, y=160)
    img_lap3=customtkinter.CTkImage(Image.open(f"C:\VS CODE FILE FACTORY\latihan phyton\TUGAS Python/tugas 2\gambar_lap/badminton.jfif"),size=(250,250))
    img_l = customtkinter.CTkLabel(tabview_1.tab("BADMINTON"),image=img_lap3).place(x= 250, y=10)
    
    nama4= customtkinter.CTkLabel(tabview_1.tab("FUTSAL"),text="Nama : FUTSAL", justify=tkinter.LEFT).place(x=20, y=60)
    durasi4= customtkinter.CTkLabel(tabview_1.tab("FUTSAL"),text="Harga/jam : 70.000", justify=tkinter.LEFT).place(x=20, y=110)
    type4= customtkinter.CTkOptionMenu(tabview_1.tab("FUTSAL"), values=["11","12","13"]).place(x=20, y=160)
    img_lap4=customtkinter.CTkImage(Image.open(f"C:\VS CODE FILE FACTORY\latihan phyton\TUGAS Python/tugas 2\gambar_lap/futsal.jfif"),size=(250,250))
    img_l = customtkinter.CTkLabel(tabview_1.tab("FUTSAL"),image=img_lap4).place(x= 250, y=10)


    def back_in():
        frame_lap.destroy()
        menu()
    back_menu = customtkinter.CTkButton(master=frame_lap,text="MENU", command=back_in,width=10, height=20)
    back_menu.place(x=10, y=10)

"""===============[ Main Root ]================"""
login_menu()
root.mainloop()