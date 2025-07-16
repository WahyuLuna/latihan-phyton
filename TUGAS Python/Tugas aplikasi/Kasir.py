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


"""===============[ Codingan ]================"""


optionmenu_1 = customtkinter.CTkOptionMenu(root, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.place(x=20, y=125)
optionmenu_1.set("CTkOptionMenu")


root.mainloop()