import tkinter
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("CustomTkinter")

# #menentukan Lebar jendela
# Lebar = 500
# Tinggi = 350

# #menentukan posisi jendela saat muncul
# x= 500 #jarak dari kiri
# y = 200 #jarak dari atas

#root.resizable(False,False)
# root.geometry(f"{Lebar}x{Tinggi}+{x}+{y}")

#membuat jendela full screen
info_lebar = root.winfo_screenwidth()
info_tinggi = root.winfo_screenheight()
root.geometry(f"{info_lebar}x{info_tinggi}+0+0")

#buat judul
logo_label = customtkinter.CTkLabel(root, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.pack(pady=10, padx=10)


"""===============[ Codingan ]================"""
label_1 = customtkinter.CTkLabel(master=root,text="label 1", justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=root, placeholder_text="")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(root, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("CTkOptionMenu")


checkbox_1 = customtkinter.CTkCheckBox(master=root)
checkbox_1.pack(pady=10, padx=10)

frame_lap = customtkinter.CTkFrame(master=root)
frame_lap.pack(pady=20, padx=20, fill="both", expand=True)
    
img_lap=customtkinter.CTkImage(Image.open("C:/VS CODE FILE FACTORY\latihan phyton\TKinter_GUI_python/Foto.png"),size=(200,200))
img_l = customtkinter.CTkLabel(master=root,image=img_lap)
img_l.place(x= 10, y=30)

def hasil():
    label_1 = customtkinter.CTkLabel(master=root,text=f"{optionmenu_1.get()}", justify=tkinter.LEFT)
    label_1.pack(pady=10, padx=10)
button_1 = customtkinter.CTkButton(master=root,text="label 1", command=hasil)
button_1.pack(pady=10, padx=10)
root.mainloop()