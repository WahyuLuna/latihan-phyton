import tkinter
import customtkinter
import numpy as np
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("CustomTkinter")

#menentukan Lebar jendela
Lebar = 500
Tinggi = 350

#menentukan posisi jendela saat muncul
x= 500 #jarak dari kiri
y = 200 #jarak dari atas

root.resizable(False,False)
root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}")

#buat judul
logo_label = customtkinter.CTkLabel(root, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.pack(pady=10, padx=10)


"""===============[ Codingan ]================"""


def hasil():
    harga = np.random.normal(1,2,3)
    plt.hist(harga,2)
    plt.show()
    
button_1 = customtkinter.CTkButton(master=root,text="label 1", command=hasil)
button_1.pack(pady=10, padx=10)
root.mainloop()