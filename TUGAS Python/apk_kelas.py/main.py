import tkinter
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("data siswa")
root.resizable(False,False)

#membuat jendela full screen
info_lebar = root.winfo_screenwidth()
info_tinggi = root.winfo_screenheight()
print(f"{info_lebar}  {info_tinggi}")
root.geometry(f"{info_lebar}x{info_tinggi}+0+0")

"""===============[ Codingan ]================"""

def menu():
    frame_log = customtkinter.CTkFrame(master=root,width=200, height=710)
    frame_log.place(x=10, y=90)
    
    menu = customtkinter.CTkLabel(frame_log, text="MENU", font=customtkinter.CTkFont(size=25, weight="bold"))
    menu.place(x=55, y=10)
menu()

def roof():
    frame_log = customtkinter.CTkFrame(master=root,width=1500, height=70)
    frame_log.place(x=10, y=5)
    
    menu = customtkinter.CTkLabel(frame_log, text="Roof", font=customtkinter.CTkFont(size=25, weight="bold"))
    menu.place(x=10, y=10)
roof()

def slide1():
    frame_log = customtkinter.CTkFrame(master=root,width=1290, height=710)
    frame_log.place(x=220, y=90)
    
    menu = customtkinter.CTkLabel(frame_log, text="Slide 1", font=customtkinter.CTkFont(size=25, weight="bold"))
    menu.place(x=55, y=10)
slide1()

root.mainloop()