
#bentuk standar
print("bentuk standar")
def fungsi(parameter):
    print(parameter)
    
fungsi("1")
fungsi(4)
fungsi(True)

print("bentuk type hints")
def fungsi_hints(argument:int)->int: #(int) dan (->int) agar mendifinisikan type data untuk fungtion
    hasil = 5**argument
    print(hasil)
    
fungsi_hints(4) #maka fungtion hanya boleh di input sesuai type data

def kata(argument:str):#(str)  agar mendifinisikan type data untuk fungtion
    print(argument)
    
kata("luna")
    