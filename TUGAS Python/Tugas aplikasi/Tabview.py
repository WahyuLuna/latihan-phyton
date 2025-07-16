import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("CustomTkinter")
root.resizable(False,False)
#menentukan Lebar jendela
Lebar = 500
Tinggi = 350

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas
root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}")

#buat judul
logo_label = customtkinter.CTkLabel(root, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.pack(pady=10, padx=10)


"""===============[ Codingan ]================"""
frame_1 = customtkinter.CTkFrame(master=root)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

tabview_1 = customtkinter.CTkTabview(master=frame_1, width=700, height=500)
tabview_1.pack(pady=10, padx=10)
tabview_1.add("BASKET")
tabview_1.add("VOLI")
tabview_1.add("BADMINTON")
tabview_1.add("FUTSAL")

label_tab_2 = customtkinter.CTkLabel(tabview_1.tab("BASKET"), text="BASKET : 20000")
label_tab_2.grid(row=0, column=0, padx=20, pady=20)
label_tab_2 = customtkinter.CTkLabel(tabview_1.tab("VOLI"), text="BASKET : 20000")
label_tab_2.grid(row=0, column=0, padx=20, pady=20)
label_tab_2 = customtkinter.CTkLabel(tabview_1.tab("BADMINTON"), text="BASKET : 20000")
label_tab_2.grid(row=0, column=0, padx=20, pady=20)

root.mainloop()