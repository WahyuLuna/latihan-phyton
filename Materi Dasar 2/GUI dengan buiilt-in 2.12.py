import tkinter

main_windows = tkinter.Tk()

#   membuat text
label = tkinter.Label(main_windows, text="Hallo semuanya, \nIni adalah contoh text dari tkinter")
label.pack()

#   membuat isi dari command button
def tekan():
    label2 = tkinter.Label(main_windows, text="aku di press")
    label2.pack()

#   membuat membuat button
tombol = tkinter.Button(main_windows, text="press", command=tekan)
tombol.pack()


main_windows.mainloop()   # mainloop akan membuat program berjalan terus hingga di tutup