import random

dpil = []
def dadu():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    dr= [d1,d2,d3]
    return dr
    
def di():
    for i in range(3):
        d = int(input(f" masukan dadu {i}:"))
        dpil.append(d)
    
def cek():
    i = 1
    while (True):
            
        if dpil == dadu():
            print(f"anda mendapatkan dadu di percobaan ke {i}")
            break
        i += 1
        
di()
cek()
    